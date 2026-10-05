import copy
import json
import tempfile
import unittest
from pathlib import Path

from findelta.common import write_json, write_jsonl, read_jsonl, sha256
from findelta.data import context
from findelta.revision import build_revision, record_hash, validate_cell_bindings, signed_cell_number
from findelta.verify import execute


def example():
    source = {'id':'ACME/2024/p1', 'pre_text':[], 'post_text':[],
              'table':[['cash','$ 10'],['total','$ 20']], 'qa':{'question':'Cash share?'}}
    target = {'abstain':False,'steps':[{'op':'divide','args':[
        {'source':'table_0','value':'10'}, {'source':'table_1','value':'20'}]}],'answer':.5}
    bindings = [{'step':0,'arg':i,'row':i,'column':1,'original_cell':source['table'][i][1],
                 'metric':['cash','total'][i],'period':'2024','unit':'USD','semantics':'signed'} for i in range(2)]
    return source,target,bindings


class RevisionTests(unittest.TestCase):
    def test_repeated_header_occurrence_does_not_prove_original_row_binding(self):
        source,target,bindings=example()
        wrong=copy.deepcopy(target);wrong['steps'][0]['args'][0]['source']='table_1'
        self.assertEqual(execute(wrong['steps'],context(source))[0],.5)
        with self.assertRaisesRegex(ValueError,'original row'):
            validate_cell_bindings(wrong,source,bindings)
        validate_cell_bindings(target,source,bindings)

    def test_accounting_sign_not_lost_in_duplicate_parentheses(self):
        self.assertEqual(signed_cell_number('$ -121 ( 121 )'),-121)
        self.assertEqual(signed_cell_number('( $ 121 )'),-121)
        with self.assertRaises(ValueError):signed_cell_number('10 to 20')
        source,target,bindings=example()
        source['table'][0][1]='$ -10 ( 10 )';bindings[0]['original_cell']=source['table'][0][1]
        # Old occurrence checking accepts the duplicated positive number.
        self.assertEqual(execute(target['steps'],context(source))[0],.5)
        with self.assertRaisesRegex(ValueError,'signed original cell'):
            validate_cell_bindings(target,source,bindings)
        bindings[0]['semantics']='magnitude'
        validate_cell_bindings(target,source,bindings)

    def test_missing_or_duplicate_annotations_fail(self):
        source,target,bindings=example()
        for altered in [bindings[:1],bindings+[bindings[0]]]:
            with self.assertRaises(ValueError):validate_cell_bindings(target,source,altered)

    def prepare(self,base):
        parent,review,out=base/'parent',base/'review',base/'out'
        source,target,bindings=example()
        wrong=copy.deepcopy(target);wrong['steps'][0]['args'][0]['source']='table_1'
        row={'id':source['id'],'company':'ACME','report_id':'ACME/2024','split':'train',
             'question':source['qa']['question'],'evidence':context(source),'target':wrong,
             'answerable':True,'audit':{},'gold_evidence_ids':['table_1']}
        write_jsonl(parent/'train.jsonl',[row])
        for split in ['dev','test']:write_jsonl(parent/f'{split}.jsonl',[dict(row,id=split,split=split)])
        decision={'id':row['id'],'parent_record_sha256':record_hash(row),'reviewer_type':'ai_assistant',
                  'action':'repair','rationale':'cash originates in row zero','category':'binding',
                  'replacement_target':target,'cell_bindings':bindings,'independent_answer':'.5','answer_unit':'fraction'}
        write_jsonl(review/'decisions.jsonl',[decision]);write_jsonl(review/'source-records.jsonl',[source])
        plan={'version':'fixture','parent_sha256':{s:sha256(parent/f'{s}.jsonl') for s in ['train','dev','test']},
              'review_files_sha256':{s:sha256(review/s) for s in ['decisions.jsonl','source-records.jsonl']}}
        write_json(review/'plan.json',plan)
        return parent,review,out,plan,row

    def test_build_preserves_parent_holdouts_and_matched_control(self):
        with tempfile.TemporaryDirectory() as tmp:
            parent,review,out,plan,row=self.prepare(Path(tmp))
            manifest=build_revision(parent,review,out)
            self.assertEqual(manifest['counts']['repaired'],1)
            self.assertEqual(read_jsonl(out/'train-control.jsonl'),[row])
            self.assertEqual(read_jsonl(parent/'train.jsonl'),[row])
            for s in ['dev','test']:self.assertEqual((out/f'{s}.jsonl').read_bytes(),(parent/f'{s}.jsonl').read_bytes())
            with self.assertRaises(ValueError):build_revision(parent,review,out)

    def test_holdout_review_id_rejected_even_with_valid_file_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            parent,review,out,plan,_=self.prepare(Path(tmp))
            d=read_jsonl(review/'decisions.jsonl');d[0]['id']='test';write_jsonl(review/'decisions.jsonl',d)
            plan['review_files_sha256']['decisions.jsonl']=sha256(review/'decisions.jsonl');write_json(review/'plan.json',plan)
            with self.assertRaisesRegex(ValueError,'non-train'):build_revision(parent,review,out)
            self.assertFalse(out.exists())

    def test_changed_parent_and_changed_review_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            parent,review,out,plan,row=self.prepare(Path(tmp))
            row['target']['answer']=.7;write_jsonl(parent/'train.jsonl',[row])
            with self.assertRaisesRegex(ValueError,'parent cohort hash'):build_revision(parent,review,out)
            plan['parent_sha256']['train']=sha256(parent/'train.jsonl');write_json(review/'plan.json',plan)
            with self.assertRaisesRegex(ValueError,'Reviewed row changed'):build_revision(parent,review,out)
        with tempfile.TemporaryDirectory() as tmp:
            parent,review,out,_,_=self.prepare(Path(tmp))
            with (review/'decisions.jsonl').open('a') as f:f.write('\n')
            with self.assertRaisesRegex(ValueError,'Review file hash'):build_revision(parent,review,out)


if __name__=='__main__':unittest.main()
