"""Heavy imports stay outside data/evaluation paths."""
import importlib.metadata
import json
import platform
from pathlib import Path


def doctor():
    result = {"python": platform.python_version(), "platform": platform.platform(), "packages": {}}
    for name in ["torch", "transformers", "trl", "peft", "datasets", "accelerate", "bitsandbytes"]:
        try:
            result["packages"][name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            result["packages"][name] = None
    if result["packages"]["torch"]:
        import torch
        result["cuda_available"] = torch.cuda.is_available()
        if result["cuda_available"]:
            result["gpu"] = torch.cuda.get_device_name(0)
            result["vram_gib"] = round(torch.cuda.get_device_properties(0).total_memory / 2**30, 2)
            # PyTorch defaults to including emulation; T4 needs native-capability detection.
            result["bf16_supported"] = torch.cuda.is_bf16_supported(including_emulation=False)
            result["recommendation"] = "Start 0.6B, batch=1, max_length=2048. Dry-run 10 steps before full training."
        else:
            result["recommendation"] = "Data/verifier work works here. Run real training on NVIDIA Linux/WSL2. CPU is only for tiny integration tests."
    return result


def resolve_model(model, out):
    from huggingface_hub import model_info
    from .common import write_json
    info = model_info(model)
    result = {"model": model, "revision": info.sha}
    write_json(out, result)
    return result


def load_model(config, cpu=False):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    model_id = config["model"]
    revision = config.get("revision")
    if not Path(model_id).exists() and (not revision or revision in {"main", "master"}):
        raise ValueError("Resolve and pin a model commit in model-lock.json before training")
    if not cpu and not torch.cuda.is_available():
        raise ValueError("CUDA unavailable. Use NVIDIA machine; --cpu is only for tiny smoke tests.")
    dtype = torch.float32 if cpu else (torch.bfloat16 if torch.cuda.is_bf16_supported(including_emulation=False) else torch.float16)
    kwargs = dict(revision=revision, torch_dtype=dtype, trust_remote_code=False, attn_implementation="sdpa")
    if config.get("load_in_4bit"):
        if cpu:
            raise ValueError("4-bit mode requires the CUDA setup")
        kwargs["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=dtype, bnb_4bit_use_double_quant=True)
        kwargs["device_map"] = {"": 0}
    model = AutoModelForCausalLM.from_pretrained(model_id, **kwargs)
    if not config.get("load_in_4bit"):
        model.to("cpu" if cpu else "cuda:0")
    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    return model, tokenizer, dtype


def read_config(config_path, model_lock=None):
    config = json.loads(Path(config_path).read_text())
    if model_lock:
        config.update(json.loads(Path(model_lock).read_text()))
    return config
