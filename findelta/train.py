import json
import time
from pathlib import Path

from .common import SYSTEM, prompt_sha256, read_jsonl, sha256, write_json
from .modeling import doctor, load_model, read_config


def load_dpo_adapters(model, sft_adapter):
    from peft import PeftModel, get_peft_model_state_dict, set_peft_model_state_dict

    model = PeftModel.from_pretrained(model, sft_adapter, adapter_name="policy", is_trainable=True)
    model.load_adapter(sft_adapter, adapter_name="reference", is_trainable=False)
    # PEFT 0.17.1 can load the second adapter through BF16 before promoting it
    # to FP32. Restore the exact loaded policy into the now-promoted reference;
    # load_state_dict copies values into separate tensors, without sharing storage.
    set_peft_model_state_dict(model, get_peft_model_state_dict(model, adapter_name="policy"),
                             adapter_name="reference")
    model.set_adapter("policy")
    for name, param in model.named_parameters():
        if ".reference." in name:
            param.requires_grad = False
    return model


def render_training_rows(rows, tokenizer, mode, max_length):
    prepared = []
    for row in rows:
        if row.get("split") != "train":
            raise ValueError("Training input contains non-train rows")
        if mode == "dpo" and row.get("review_status") != "approved":
            raise ValueError("DPO requires reviewed pairs. Export approved review.csv rows first.")
        prompt = tokenizer.apply_chat_template(row["prompt"], tokenize=False, add_generation_prompt=True, enable_thinking=False)
        item = {"prompt": prompt}
        for key in (["completion"] if mode == "sft" else ["chosen", "rejected"]):
            message = row[key]
            if len(message) != 1 or message[0]["role"] != "assistant":
                raise ValueError("Expected exactly one assistant completion")
            full = tokenizer.apply_chat_template(row["prompt"] + message, tokenize=False, enable_thinking=False)
            if not full.startswith(prompt):
                raise ValueError("Training/inference chat-template mismatch")
            item[key] = full[len(prompt):]
            # TRL DPO separately tokenizes and appends EOS to each completion.
            length = (len(tokenizer(prompt, add_special_tokens=False)["input_ids"]) +
                      len(tokenizer(item[key], add_special_tokens=False)["input_ids"]) + 1)
            if length > max_length:
                raise ValueError(f"Sample {row['id']} is too long ({length}). Filter explicitly; never truncate evidence/targets.")
        prepared.append(item)
    if not prepared:
        raise ValueError("Empty training set")
    return prepared


def train(mode, data_path, config_path, out, model_lock=None, sft_adapter=None, cpu=False, max_steps=None):
    import torch
    from datasets import Dataset
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from transformers import set_seed
    from trl import DPOConfig, DPOTrainer, SFTConfig, SFTTrainer
    config = read_config(config_path, model_lock)
    out = Path(out)
    if out.exists() and any(out.iterdir()):
        raise ValueError("Output directory is nonempty. Use a new run directory to preserve results.")
    if mode == "dpo" and not sft_adapter:
        raise ValueError("DPO must start from an SFT adapter")
    set_seed(config.get("seed", 42))
    model, tokenizer, dtype = load_model(config, cpu)
    model.config.use_cache = False
    if config.get("load_in_4bit"):
        model = prepare_model_for_kbit_training(model)
    lora = LoraConfig(r=config.get("lora_r", 8), lora_alpha=config.get("lora_alpha", 16),
                      lora_dropout=0.0, target_modules=config.get("target_modules", ["q_proj", "v_proj"]),
                      task_type="CAUSAL_LM", bias="none")
    if mode == "sft":
        model = get_peft_model(model, lora)
    else:
        # Both adapters start from the SAME SFT checkpoint. Disabling a sole SFT adapter
        # would incorrectly use the original base model as DPO reference.
        previous = json.loads((Path(sft_adapter) / "run_manifest.json").read_text())
        if previous["config"]["model"] != config["model"] or previous["config"].get("revision") != config.get("revision"):
            raise ValueError("SFT and DPO base model/revision mismatch")
        model = load_dpo_adapters(model, sft_adapter)
    if config.get("gradient_checkpointing", True):
        model.enable_input_require_grads()
    rows = read_jsonl(data_path)
    if any(not row["prompt"] or row["prompt"][0] != {"role": "system", "content": SYSTEM} for row in rows):
        raise ValueError("Training prompts differ from current version. Re-export SFT or rebuild preference candidates.")
    dataset = Dataset.from_list(render_training_rows(rows, tokenizer, mode, config["max_length"]))
    actual_steps = max_steps if max_steps is not None else config.get("max_steps", -1)
    common = dict(output_dir=str(out), per_device_train_batch_size=1,
                  gradient_accumulation_steps=config.get("gradient_accumulation_steps", 8),
                  learning_rate=config.get("learning_rate", 1e-4 if mode == "sft" else 5e-6),
                  num_train_epochs=config.get("epochs", 1), max_steps=actual_steps,
                  max_length=config["max_length"], seed=config.get("seed", 42),
                  bf16=dtype == torch.bfloat16, fp16=dtype == torch.float16,
                  gradient_checkpointing=config.get("gradient_checkpointing", True),
                  gradient_checkpointing_kwargs={"use_reentrant": False},
                  logging_steps=1 if cpu else 5, save_strategy="no", report_to="none",
                  optim="adamw_torch", dataloader_pin_memory=not cpu, use_cpu=cpu,
                  warmup_ratio=.05, max_grad_norm=1.0)
    if mode == "sft":
        args = SFTConfig(**common, packing=False, completion_only_loss=True)
        trainer = SFTTrainer(model=model, args=args, processing_class=tokenizer, train_dataset=dataset)
    else:
        args = DPOConfig(**common, beta=config.get("beta", .1),
                         max_prompt_length=None, max_completion_length=None,
                         model_adapter_name="policy", ref_adapter_name="reference",
                         precompute_ref_log_probs=True)
        trainer = DPOTrainer(model=model, args=args, processing_class=tokenizer, train_dataset=dataset)
    if not cpu:
        torch.cuda.reset_peak_memory_stats()
    # Snapshot small trainable matrices for an actual update check, not a claim of quality.
    before = {n: p.detach().float().cpu().clone() for n, p in model.named_parameters() if p.requires_grad}
    reference_before = {n: p.detach().float().cpu().clone() for n, p in model.named_parameters() if ".reference." in n}
    initial_policy_reference_identical = None
    if mode == "dpo":
        # A zero change count alone could hide a missing reference adapter.
        initial_policy_reference_identical = bool(reference_before) and all(
            name.replace(".reference.", ".policy.") in before and
            torch.equal(value, before[name.replace(".reference.", ".policy.")])
            for name, value in reference_before.items())
        if not initial_policy_reference_identical:
            raise RuntimeError("DPO policy and nonempty reference must start with identical SFT weights")
    start = time.perf_counter()
    result = trainer.train()
    elapsed = time.perf_counter() - start
    changed = sum(not torch.equal(before[n], p.detach().float().cpu()) for n, p in model.named_parameters() if n in before)
    reference_changed = sum(not torch.equal(reference_before[n], p.detach().float().cpu()) for n, p in model.named_parameters() if n in reference_before)
    if reference_changed:
        raise RuntimeError("DPO reference weights changed")
    if not changed:
        raise RuntimeError("No trainable parameters changed")
    if mode == "dpo":
        # policy is saved under out/policy, reference never shipped as result.
        model.save_pretrained(out, selected_adapters=["policy"])
    else:
        trainer.save_model(str(out))
    tokenizer.save_pretrained(out)
    trainer.save_state()
    manifest = dict(mode=mode, config=config, actual_max_steps=actual_steps, data_sha256=sha256(data_path), prompt_sha256=prompt_sha256(),
                    examples=len(rows), environment=doctor(), elapsed_seconds=elapsed,
                    peak_allocated_gib=None if cpu else torch.cuda.max_memory_allocated() / 2**30,
                    peak_reserved_gib=None if cpu else torch.cuda.max_memory_reserved() / 2**30,
                    trainable_tensors_changed=changed, reference_tensors_changed=reference_changed,
                    reference_tensors_checked=len(reference_before),
                    initial_policy_reference_identical=initial_policy_reference_identical,
                    metrics=result.metrics, log_history=trainer.state.log_history,
                    note="Training loss and parameter updates are not evidence of improved held-out accuracy.")
    if sft_adapter:
        manifest["sft_run_manifest_sha256"] = sha256(Path(sft_adapter) / "run_manifest.json")
    write_json(out / "run_manifest.json", manifest)
    return manifest
