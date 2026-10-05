"""Actual PEFT regression: FP32 SFT adapters loaded onto a BF16 tiny base."""
import json,sys,tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import torch
from transformers import LlamaConfig,LlamaForCausalLM
from peft import LoraConfig,get_peft_model
from safetensors.torch import load_file
from findelta.train import load_dpo_adapters

cfg=LlamaConfig(vocab_size=64,hidden_size=32,intermediate_size=64,num_hidden_layers=1,num_attention_heads=2,num_key_value_heads=2)
with tempfile.TemporaryDirectory() as temp:
 model=get_peft_model(LlamaForCausalLM(cfg),LoraConfig(r=2,lora_alpha=4,target_modules=['q_proj','v_proj'],task_type='CAUSAL_LM'))
 with torch.no_grad():
  for p in model.parameters():
   if p.requires_grad:p.fill_(0.1234567) # Deliberately not exactly representable in BF16.
 model.save_pretrained(temp)
 checkpoint=load_file(str(Path(temp)/'adapter_model.safetensors'))
 m=load_dpo_adapters(LlamaForCausalLM(cfg).to(torch.bfloat16),temp)
 params=dict(m.named_parameters()); count=0
 for name,p in params.items():
  if '.policy.' not in name:continue
  q=params[name.replace('.policy.','.reference.')]; original=checkpoint[name.replace('.policy.','.')]
  assert torch.equal(p.cpu(),original) and torch.equal(p,q)
  assert p.data_ptr()!=q.data_ptr() and p.requires_grad and not q.requires_grad
  saved=q.detach().clone()
  with torch.no_grad():p.add_(0.001)
  assert torch.equal(q,saved) and not torch.equal(p,q)
  count+=1
 assert count==4
 print(json.dumps({'passed':True,'adapter_tensors_checked':count,'base_dtype':'bfloat16','checkpoint_dtype':'float32','exact_checkpoint_preserved':True,'policy_reference_initially_equal':True,'no_shared_storage':True,'reference_frozen':True}))
