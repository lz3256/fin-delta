"""Real CPU SFT + DPO integration test, with a RANDOM tiny model; not a benchmark."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def main():
    import torch
    from tokenizers import Tokenizer, models, pre_tokenizers, trainers
    from transformers import GPT2Config, GPT2LMHeadModel, PreTrainedTokenizerFast
    from findelta.common import completion, messages, write_json, write_jsonl
    from findelta.preferences import perturb_target
    from findelta.train import train
    from findelta.predict import predict
    from findelta.evaluate import evaluate
    from findelta.verify import score
    p = argparse.ArgumentParser()
    p.add_argument("--out", required=True)
    a = p.parse_args()
    root = Path(a.out).resolve()
    root.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(2)
    torch.manual_seed(42)
    row = {"id": "fixture-1", "company": "fixture", "report_id": "fixture/2024", "split": "train",
           "question": "How much did revenue increase?", "evidence": {"t": "Revenue: 2024 = 120, 2023 = 100."},
           "answerable": True, "gold_evidence_ids": ["t"],
           "target": {"abstain": False, "steps": [{"op": "subtract", "args": [{"source": "t", "value": "120"}, {"source": "t", "value": "100"}]}], "answer": 20}}
    assert score(row, row["target"])["verified_correct"]
    assert perturb_target(row) is not None
    tok = Tokenizer(models.WordLevel(unk_token="[UNK]"))
    tok.pre_tokenizer = pre_tokenizers.Whitespace()
    tok.train_from_iterator([json.dumps(messages(row)), completion(row["target"]), completion(perturb_target(row))],
                            trainers.WordLevelTrainer(special_tokens=["[UNK]", "[PAD]", "[EOS]", "[BOS]"]))
    tokenizer = PreTrainedTokenizerFast(tokenizer_object=tok, unk_token="[UNK]", pad_token="[PAD]", eos_token="[EOS]", bos_token="[BOS]")
    tokenizer.chat_template = "{% for message in messages %}{{ message['role'] + ': ' + message['content'] + eos_token }}{% endfor %}{% if add_generation_prompt %}{{ 'assistant: ' }}{% endif %}"
    model_dir = root / "random-tiny-model"
    tokenizer.save_pretrained(model_dir)
    model = GPT2LMHeadModel(GPT2Config(vocab_size=len(tokenizer), n_positions=1024, n_ctx=1024, n_embd=32, n_layer=1, n_head=2,
                                     resid_pdrop=0., embd_pdrop=0., attn_pdrop=0., bos_token_id=tokenizer.bos_token_id,
                                     eos_token_id=tokenizer.eos_token_id, pad_token_id=tokenizer.pad_token_id))
    model.save_pretrained(model_dir)
    config = {"model": str(model_dir), "max_length": 1024, "max_prompt_length": 900, "max_new_tokens": 32,
              "target_modules": ["c_attn"], "gradient_checkpointing": False,
              "gradient_accumulation_steps": 1, "learning_rate": .001, "epochs": 1, "seed": 42}
    write_json(root / "config.json", config)
    write_jsonl(root / "data.jsonl", [row])
    sft_rows = [dict(id=str(i), split="train", prompt=messages(row), completion=[{"role": "assistant", "content": completion(row["target"])}]) for i in range(4)]
    write_jsonl(root / "sft.jsonl", sft_rows)
    # Fixture pairs are manually known, marked approved ONLY inside this integration test.
    dpo_rows = [dict(id=str(i), split="train", review_status="approved", prompt=messages(row),
                    chosen=[{"role": "assistant", "content": completion(row["target"])}],
                    rejected=[{"role": "assistant", "content": completion(perturb_target(row))}]) for i in range(4)]
    write_jsonl(root / "dpo.jsonl", dpo_rows)
    sft = train("sft", root / "sft.jsonl", root / "config.json", root / "sft", cpu=True, max_steps=2)
    dpo = train("dpo", root / "dpo.jsonl", root / "config.json", root / "dpo", sft_adapter=root / "sft", cpu=True, max_steps=2)
    predict(root / "data.jsonl", root / "config.json", root / "prediction.jsonl", adapter=root / "dpo/policy", cpu=True)
    evaluation = evaluate(root / "data.jsonl", root / "prediction.jsonl", root / "eval")
    summary = {"test_kind": "random tiny CPU integration test, NOT model quality evidence",
               "sft_steps": sft["metrics"], "dpo_steps": dpo["metrics"],
               "sft_parameters_changed": sft["trainable_tensors_changed"],
               "dpo_parameters_changed": dpo["trainable_tensors_changed"],
               "dpo_reference_parameters_changed": dpo["reference_tensors_changed"],
               "prediction_evaluation_completed": evaluation["n"] == 1}
    write_json(root / "summary.json", summary)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
