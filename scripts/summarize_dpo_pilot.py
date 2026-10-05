"""Audit the frozen DPO pilot against the saved SFT baseline and write reports."""
import json,sys,collections,random,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from findelta.common import read_jsonl,write_json,write_jsonl,sha256,prompt_sha256
from findelta.verify import score
ROOT=Path(__file__).resolve().parents[1];run=ROOT/'reports/week1-dpo-v1';old=ROOT/'reports/week1-duration-v1'
def j(p):return json.loads(p.read_text())
def paired(a,b):
 groups=collections.defaultdict(list);trans=collections.Counter()
 for uid,x in a.items():
  y=b[uid]; groups[y['report_id']].append(int(y['verified_correct'])-int(x['verified_correct']))
  trans[str(int(x['verified_correct']))+'->'+str(int(y['verified_correct']))]+=1
 rng=random.Random(42);keys=sorted(groups);vals=[]
 for _ in range(1000):
  v=[x for key in rng.choices(keys,k=len(keys)) for x in groups[key]];vals.append(sum(v)/len(v))
 vals.sort();return {'delta':sum(sum(g) for g in groups.values())/len(a),'ci95':[vals[25],vals[975]],'transitions':dict(trans),'reports':len(keys)}
def main():
 assert (run/'status.txt').read_text().strip()=='COMPLETE'
 proto=j(run/'training-protocol.json');sel=j(run/'sampling-protocol.json');review=j(run/'review-manifest.json')
 train=j(run/'dpo-full/run_manifest.json');smoke=j(run/'dpo-smoke5/run_manifest.json')
 predmeta=j(run/'dpo-dev.jsonl.manifest.json');basepredmeta=j(old/'sft3-dev.jsonl.manifest.json')
 assert proto['training_data_sha256']==review['data_sha256']==sha256(run/'dpo-approved.jsonl')==train['data_sha256']
 assert train['sft_run_manifest_sha256']==sha256(old/'sft3-adapter/run_manifest.json')==sel['source_adapter_manifest_sha256']
 assert predmeta['adapter_manifest_sha256']==sha256(run/'dpo-full/run_manifest.json')
 assert predmeta['config']==basepredmeta['config'] and predmeta['samples']==basepredmeta['samples']==1 and predmeta['temperature']==basepredmeta['temperature']==0
 assert predmeta['environment']==basepredmeta['environment']
 assert predmeta['prompt_sha256']==basepredmeta['prompt_sha256']==prompt_sha256()==proto['prompt_sha256']
 assert predmeta['dataset_sha256']==basepredmeta['dataset_sha256']==sha256(ROOT/'data/cohort/v1/dev.jsonl')
 for m in [smoke,train]:
  assert m['initial_policy_reference_identical'] and m['reference_tensors_checked']==112 and m['reference_tensors_changed']==0 and m['trainable_tensors_changed']==112
  assert math.isfinite(m['metrics']['train_loss'])
 assert smoke['metrics']['epoch']<1 and train['metrics']['epoch']==1 and train['actual_max_steps']==-1
 rows=read_jsonl(run/'dpo-approved.jsonl');assert len(rows)==32==len({r['id'] for r in rows})
 cohorts={k:read_jsonl(ROOT/f'data/cohort/v1/{k}.jsonl') for k in ['train','dev','test']}
 assert {r['id'] for r in rows}<={r['id'] for r in cohorts['train']}
 assert not {r['id'] for r in rows}&{r['id'] for r in cohorts['dev']+cohorts['test']}
 assert all(r['reviewer_type']=='ai_assistant' and r['review_status']=='approved' for r in rows)
 results={};audits={}
 for name,folder,pred in [('sft_raw',old/'sft3-dev',old/'sft3-dev.jsonl'),('dpo_raw',run/'dpo-dev',run/'dpo-dev.jsonl'),('sft_executor',old/'sft-executor-dev',old/'sft3-executor.jsonl'),('dpo_executor',run/'dpo-executor-dev',run/'dpo-executor.jsonl')]:
  metrics=j(folder/'metrics.json');per={r['id']:r for r in read_jsonl(folder/'per_example.jsonl')};preds=read_jsonl(pred)
  assert metrics['predictions_sha256']==sha256(pred) and metrics['n']==200 and metrics['missing_predictions']==0
  assert len(preds)==len(per)==200 and {r['id'] for r in preds}==set(per)
  byid={r['id']:r for r in cohorts['dev']}
  for x in preds:
   s=score(byid[x['id']],x['output']);assert all(s[k]==per[x['id']][k] for k in s)
  results[name]=metrics;audits[name]=per
 raw=paired(audits['sft_raw'],audits['dpo_raw']);exe=paired(audits['sft_executor'],audits['dpo_executor'])
 changes=[]
 for r in cohorts['dev']:
  uid=r['id'];changes.append({'id':uid,'report_id':r['report_id'],'sft_raw':audits['sft_raw'][uid]['verified_correct'],'dpo_raw':audits['dpo_raw'][uid]['verified_correct'],'sft_executor':audits['sft_executor'][uid]['verified_correct'],'dpo_executor':audits['dpo_executor'][uid]['verified_correct']})
 write_jsonl(run/'paired-outcomes.jsonl',changes)
 validation={'passed':True,'same_frozen_dev_200':True,'same_inference_config_environment_and_prompt':True,'prediction_hashes_and_per_example_scores_recomputed':True,'approved_train_only_unique':32,'exact_initial_reference_tensors':112,'frozen_reference_tensors_changed':0,'policy_tensors_updated':112,'formal_run_fresh_from_sft':True,'human_reviewed':0,'test_predictions_generated':False,'core_tests_passed':22,'reference_precision_regression':j(run/'reference-precision-regression.json'),'paired_raw':raw,'paired_executor':exe}
 write_json(run/'validation.json',validation)
 write_json(run/'summary.json',{'metrics':results,'paired_raw':raw,'paired_executor':exe,'train':{k:train[k] for k in ['examples','elapsed_seconds','peak_allocated_gib','peak_reserved_gib','metrics','trainable_tensors_changed','reference_tensors_changed']},'review':review,'test_evaluated':False})
 lines=['# FinDelta：助手审核偏好的 DPO 小规模试验','', '**这是一次真实 GPU DPO 训练及完整开发集对照；32 对偏好由 AI 助手审核，非人工反馈或 RLHF。测试集未评测。**','', '## 结果','', '| 方法 | 原始输出 verified | 同一执行器后 verified |','|---|---:|---:|']
 for label,prefix in [('3-epoch SFT','sft'),('SFT + DPO','dpo')]:
  a=results[prefix+'_raw']['verified_accuracy'];b=results[prefix+'_executor']['verified_accuracy'];lines.append(f'| {label} | {a:.1%} ({round(a*200)}/200) | {b:.1%} ({round(b*200)}/200) |')
 for label,d in [('预先指定主指标：执行器后 verified',exe),('次指标：原始输出 verified',raw)]:
  lines+=['',f"{label}变化 **{d['delta']*100:+.1f} 个百分点**，配对报告分组 bootstrap 95% 区间 **[{d['ci95'][0]*100:+.1f}, {d['ci95'][1]*100:+.1f}]**。由错转对 {d['transitions'].get('0->1',0)} 题，由对转错 {d['transitions'].get('1->0',0)} 题。"]
 if exe['ci95'][0]<=0<=exe['ci95'][1]:lines+=['','主指标区间覆盖 0，**没有证据确认这次 DPO 带来稳定提升**。保留原 SFT 作为当前基线；不因某个次指标点估计上涨就宣称 DPO 有效。']
 elif exe['delta']<0:lines+=['','本次主指标下降；保留原 SFT，当前 DPO 不替换基线。']
 else:lines+=['','主指标在本次 dev 样本上提高，但仅一次 seed、32 对偏好，仍需独立复现和最终测试。']
 lines+=['','## 实验控制','', '- 沿用同一 Qwen3-0.6B revision、公司隔离 200 题 dev、prompt v3、BF16、greedy、batch 8、最多 640 新 token；逐项核对 manifest 相同。','- DPO policy/reference 均从原 3-epoch SFT adapter 开始。先 5 步 smoke，正式训练重新加载 SFT，不延续 smoke。','- 固定 1 epoch、batch 1、累计 4、LR 5e-6、beta 0.1、seed 42、LoRA r8/alpha16/q_proj+v_proj。32 对对应 8 个 optimizer steps。','- 训练输入全部来自 train；本轮未用 dev 选偏好或调参。此前已使用 dev 做开发，因此本次仍是探索性开发集结果。','- 执行器只读取模型程序及题目证据，不读取参考答案来改输出。该方法最初是 SFT 阶段的事后诊断，本轮在 DPO 采样前固定为主指标；旧脚本中的 post-hoc 描述指方法的来源。','', '## 数据审核','', '- 新采样 256 道训练题，得到 101 个可执行但程序答案错误的候选；按事前协议仅审核前 60 个，22 对通过、38 对排除、41 对仍待审。','- 加此前审核通过的 10 对，共 32 对，覆盖 18 家发行人、27 份年报。没有为凑数量放宽标准；每条记录 reviewer_type=ai_assistant 和审核理由。','- 明确错误包括年份反转（ETR/2017，参考反转 2015→2016）、AOCI 正负号错误（AES/2001）、平均值漏年份/漏除数。其他排除项包含来源错绑、尺度等价、缺少现金流调节依据等，并非全部确定错标。','- 通过样本逐题核对原始表和相关文本，并用独立 Decimal 算式校验。负例来自模型真实程序，但数值 answer 用执行器重算，故不是未经处理的人类偏好。','- [新增 60 题逐题审核](../../data/preferences/sft3-expanded-v1/assistant-expanded-v1/REPORT.zh.md)。AI 审核不保证无噪声；未来仍需要独立人工复核。','', '## 修复的训练问题','', '- 首次 GPU smoke 在训练前被一致性断言拦住：PEFT 0.17.1 在 BF16 基座上加载第二个 adapter 时，先舍入再提升为 FP32，导致 reference 偏离原 SFT；policy 与原始 FP32 checkpoint 一致。','- 修复为将已正确加载的 policy state 复制进独立 reference 参数，再冻结。未通过修改断言容差绕过问题；两者现在逐位相同且不共享存储。','- 新增真实 PEFT/BF16 小模型回归检查，验证精确 checkpoint、一致初始化、独立存储和 reference 冻结；核心 22 项测试通过。失败首次尝试保存在 attempt-01-reference-precision，未产生训练更新。',f"- 正式 GPU 训练确认 112 个 policy 张量更新、112 个 reference 张量全部不变。训练约 {train['elapsed_seconds']:.1f} 秒；峰值 allocated {train['peak_allocated_gib']:.2f} GiB、reserved {train['peak_reserved_gib']:.2f} GiB。训练 loss 不是泛化提升证据。",'', '## 解释边界及下一步','', '这些分数是自定义 filtered FinQA cohort 与有噪声参考标签的一致性，不是官方 FinQA 分数，也不证明金融语义事实性。bootstrap 仅描述报告样本不确定性，不覆盖 seed 方差或多次使用 dev 的选择偏差。训练及审核规模很小，不能据此概括 DPO 方法整体有效或无效。','', '下一轮优先明确数值尺度及 source/entity/period 绑定规则，对已标记的训练标签另建修正版，再扩充偏好、做多个 seed。保留当前所有结果和旧 cohort，避免数据修正后把新旧分数当完全同条件比较。最终测试需等方案冻结后一次性使用。','', '## 简历可用的诚实描述','', '> Implemented and audited LoRA SFT and DPO for Qwen3-0.6B on public financial QA, including AI-reviewed preference curation, frozen-reference integrity checks, and paired development-set evaluation; diagnosed a BF16 adapter-loading precision mismatch.','', 'SFT+执行器 44.5% 的既有结果可按原报告口径描述。DPO 本轮是否提升以以上主指标为准；不能写成已完成 RLHF、人工偏好训练、多卡训练或生产部署。','']
 (run/'REPORT.zh.md').write_text('\n'.join(lines))
 print(json.dumps({'passed':True,'raw':raw,'executor':exe,'train_seconds':train['elapsed_seconds']},ensure_ascii=False))
if __name__=='__main__':main()
