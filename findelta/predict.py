import json
import time
from pathlib import Path

from .common import chat_text, prompt_sha256, read_jsonl, sha256, write_json
from .modeling import doctor, load_model, read_config


def predict(data_path, config_path, out, model_lock=None, adapter=None, cpu=False, samples=1, temperature=0.0):
    import torch
    from peft import PeftModel
    from transformers import set_seed
    if samples < 1 or (samples > 1 and temperature <= 0):
        raise ValueError("Multiple samples require positive temperature")
    out = Path(out)
    if out.exists():
        raise ValueError("Prediction output exists; use a new filename")
    config = read_config(config_path, model_lock)
    batch_size = config.get("inference_batch_size", 1)
    if type(batch_size) is not int or batch_size < 1:
        raise ValueError("inference_batch_size must be a positive integer")
    model, tokenizer, _ = load_model(config, cpu)
    tokenizer.padding_side = "left"
    adapter_hash = None
    if adapter:
        adapter = Path(adapter)
        manifest_path = adapter / "run_manifest.json"
        if not manifest_path.exists():
            manifest_path = adapter.parent / "run_manifest.json"
        previous = json.loads(manifest_path.read_text())
        if previous.get("prompt_sha256") != prompt_sha256():
            raise ValueError("Adapter training prompt differs or lacks provenance. Re-export SFT and use the same prompt for all compared models.")
        if any(previous["config"].get(k) != config.get(k) for k in ["model", "revision"]):
            raise ValueError("Adapter base-model mismatch")
        adapter_hash = sha256(manifest_path)
        model = PeftModel.from_pretrained(model, adapter)
    model.eval()
    model.config.use_cache = True
    set_seed(config.get("seed", 42))
    rows = read_jsonl(data_path)
    if samples > 1 and any(r["split"] != "train" for r in rows):
        raise ValueError("Preference sampling is restricted to train; evaluation uses one completion per prompt")
    digest = sha256(data_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    token_total = 0
    start = time.perf_counter()
    with out.open("w", encoding="utf-8") as f:
        for offset in range(0, len(rows), batch_size):
            batch = rows[offset:offset + batch_size]
            encoded = tokenizer([chat_text(tokenizer, row) for row in batch], padding=True,
                                return_tensors="pt", add_special_tokens=False).to(model.device)
            if encoded.input_ids.shape[1] > config["max_prompt_length"]:
                raise ValueError(f"Prompt exceeds fixed budget in batch at {offset}; freeze the cohort first")
            for sample in range(samples):
                kwargs = dict(max_new_tokens=config["max_new_tokens"], do_sample=temperature > 0,
                              pad_token_id=tokenizer.pad_token_id, eos_token_id=tokenizer.eos_token_id)
                if temperature > 0:
                    kwargs.update(temperature=temperature, top_p=.95)
                with torch.inference_mode():
                    generated = model.generate(**encoded, **kwargs)
                for row, sequence in zip(batch, generated):
                    tokens = sequence[encoded.input_ids.shape[1]:].tolist()
                    # Other sequences in a batch can continue after this one has ended.
                    # Include its EOS once, but never count subsequent padding as generated work.
                    if tokenizer.eos_token_id in tokens:
                        tokens = tokens[:tokens.index(tokenizer.eos_token_id) + 1]
                    token_total += len(tokens)
                    record = dict(id=row["id"], sample=sample, dataset_sha256=digest, prompt_sha256=prompt_sha256(),
                                  output=tokenizer.decode(tokens, skip_special_tokens=True).strip(),
                                  generated_tokens=len(tokens))
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
                f.flush()
            completed = min(offset + batch_size, len(rows))
            if completed % 10 == 0 or batch_size > 1 or completed == len(rows):
                print(f"Generated {completed}/{len(rows)} questions", flush=True)
    if not cpu:
        torch.cuda.synchronize()
    elapsed = time.perf_counter() - start
    manifest = dict(config=config, environment=doctor(), dataset_sha256=digest, prompt_sha256=prompt_sha256(),
                    predictions_sha256=sha256(out), adapter_manifest_sha256=adapter_hash,
                    samples=samples, temperature=temperature, generated_tokens=token_total,
                    elapsed_seconds=elapsed, generated_tokens_per_second=token_total / elapsed)
    write_json(str(out) + ".manifest.json", manifest)
    return manifest
