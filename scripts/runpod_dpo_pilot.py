"""One frozen AI-reviewed DPO pilot; separate smoke and formal adapters."""
import json, os, subprocess, sys
from pathlib import Path
ROOT=Path('/workspace/fin-delta')
sys.path.insert(0,str(ROOT))
from findelta.common import read_jsonl,write_json,sha256,prompt_sha256

def main():
 os.chdir(ROOT)
 os.environ['HF_HOME']='/workspace/findelta-runtime/hf-cache'
 os.environ['TOKENIZERS_PARALLELISM']='false'
 run=Path('/workspace/findelta-runs/week1-dpo-v1')
 old=Path('/workspace/findelta-runs/week1-duration-v1')
 data=run/'dpo-approved.jsonl'
 for name in ['training-protocol.json','dpo-smoke5','dpo-full','dpo-dev.jsonl']:
  if (run/name).exists(): raise ValueError('Refusing overwrite: '+name)
 rows=read_jsonl(data)
 assert rows and len({r['id'] for r in rows})==len(rows)
 assert all(r['split']=='train' and r['review_status']=='approved' and r['reviewer_type']=='ai_assistant' for r in rows)
 selection=json.loads((run/'sampling-protocol.json').read_text())
 config=json.loads((run/'dpo-config.json').read_text())
 assert config==selection['dpo_recipe']
 assert sha256(old/'sft3-adapter/run_manifest.json')==selection['source_adapter_manifest_sha256']
 write_json(run/'training-protocol.json',{'purpose':'Single-seed exploratory DPO using AI-reviewed preferences',
  'n_preferences':len(rows),'training_data_sha256':sha256(data),'human_reviewed':0,'reviewer_type':'ai_assistant',
  'review_manifest':json.loads((run/'review-manifest.json').read_text()),
  'sampling_protocol_sha256':sha256(run/'sampling-protocol.json'),
  'initialization':'Both policy and frozen reference are the 3-epoch SFT adapter; formal run restarts after smoke',
  'sft_manifest_sha256':sha256(old/'sft3-adapter/run_manifest.json'),
  'training_config':config,'prompt_sha256':prompt_sha256(),'dev_sha256':sha256('data/cohort/v1/dev.jsonl'),
  'inference_config':json.loads((run/'inference-config.json').read_text()),
  'primary':'verified dev accuracy using the same deterministic executor as SFT baseline',
  'secondary':'raw dev verified accuracy','test_evaluated':False,
  'code_sha256':{str(p):sha256(p) for p in sorted(Path('findelta').glob('*.py'))}})
 def cmd(stage,args):
  (run/'status.txt').write_text(stage+'\n'); print(stage,flush=True)
  with (run/(stage+'.log')).open('w') as f:
   subprocess.run([sys.executable,'-u',*map(str,args)],stdout=f,stderr=subprocess.STDOUT,check=True)
 def train(stage,out,smoke=False):
  args=['-m','findelta','train','--mode','dpo','--data',data,'--config',run/'dpo-config.json','--sft-adapter',old/'sft3-adapter','--out',run/out]
  if smoke:args+=['--max-steps','5']
  cmd(stage,args)
 try:
  train('smoke','dpo-smoke5',True)
  smoke=json.loads((run/'dpo-smoke5/run_manifest.json').read_text())
  assert smoke['trainable_tensors_changed']>0 and smoke['reference_tensors_changed']==0
  assert smoke['reference_tensors_checked']>0 and smoke['initial_policy_reference_identical'] is True
  train('train','dpo-full')
  cmd('predict',['-m','findelta','predict','--data','data/cohort/v1/dev.jsonl','--config',run/'inference-config.json','--adapter',run/'dpo-full/policy','--out',run/'dpo-dev.jsonl'])
  cmd('evaluate',['-m','findelta','evaluate','--data','data/cohort/v1/dev.jsonl','--predictions',run/'dpo-dev.jsonl','--out',run/'dpo-dev'])
  cmd('executor',['scripts/executor_ablation.py','--data','data/cohort/v1/dev.jsonl','--predictions',run/'dpo-dev.jsonl','--out',run/'dpo-executor.jsonl'])
  (run/'sft-executor-dev').rename(run/'dpo-executor-dev')
  cmd('compare-raw',['-m','findelta','compare','--run',f'SFT-3epochs={old}/sft3-dev','--run',f'DPO={run}/dpo-dev','--out',run/'comparison-raw.md'])
  cmd('compare-executor',['-m','findelta','compare','--run',f'SFT-3epochs+executor={old}/sft-executor-dev','--run',f'DPO+executor={run}/dpo-executor-dev','--out',run/'comparison-executor.md'])
  (run/'status.txt').write_text('COMPLETE\n'); print('COMPLETE',flush=True)
 except BaseException:
  (run/'status.txt').write_text('FAILED\n');raise

if __name__=='__main__':main()
