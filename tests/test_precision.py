import types
import unittest
from unittest.mock import Mock, patch

from findelta.modeling import doctor, load_model


def simulated_t4():
    cuda = types.SimpleNamespace(
        is_available=lambda: True,
        get_device_name=lambda i: "Tesla T4",
        get_device_properties=lambda i: types.SimpleNamespace(total_memory=15 * 2**30),
        is_bf16_supported=lambda including_emulation=True: including_emulation,
    )
    return types.SimpleNamespace(cuda=cuda, float32="fp32", float16="fp16", bfloat16="bf16")


class NativePrecisionTests(unittest.TestCase):
    def test_t4_diagnostic_excludes_emulation(self):
        with patch.dict("sys.modules", {"torch": simulated_t4()}), patch("importlib.metadata.version", return_value="test"):
            self.assertFalse(doctor()["bf16_supported"])

    def test_t4_model_uses_fp16_even_if_emulated_bf16_is_available(self):
        model_loader, tokenizer_loader = Mock(), Mock()
        tokenizer_loader.from_pretrained.return_value.pad_token_id = 0
        transformers = types.SimpleNamespace(AutoModelForCausalLM=model_loader,
                                            AutoTokenizer=tokenizer_loader, BitsAndBytesConfig=Mock())
        with patch.dict("sys.modules", {"torch": simulated_t4(), "transformers": transformers}):
            _, _, dtype = load_model({"model": "test-model", "revision": "fixed-revision"})
        self.assertEqual(dtype, "fp16")
        self.assertEqual(model_loader.from_pretrained.call_args.kwargs["torch_dtype"], "fp16")


if __name__ == "__main__":
    unittest.main()
