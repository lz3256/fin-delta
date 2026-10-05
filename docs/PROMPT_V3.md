# Prompt v3 and first RunPod experiment

The v2 probe on the existing dev cohort's first 20 rows completed on an RTX 4090. Its schema-valid rate was 45%; numeric and verified accuracy were both 0%. Errors included Markdown-fenced JSON, forward references and programs without evidence. This is a diagnostic result, not a controlled comparison against the earlier Colab run.

Before the formal SFT comparison, v3 resolves an instruction ambiguity: the `source` field contains an evidence ID without the brackets used to delimit that ID in the input. It also explicitly excludes Markdown. There are no numeric demonstration answers in the prompt. The frozen cohort, targets, numeric tolerance and verifier are unchanged. Token-only checks confirmed all train/dev/test inputs still fit the existing context budget; no test predictions or test quality evaluation are performed.

The prompt hash is `8a196cd0774d5e2391d83816f1bb129577fb5f8c5b9230aaf2fab5a78fbfb3c5`.

The 10-step SFT smoke check completed successfully, with 112 trainable tensors updated and no out-of-memory error. The full experiment starts again from the pinned base model, not from the smoke adapter. It uses 1,000 training examples for one epoch and seed 42.

Both the base and SFT model are evaluated on the same 200-example custom dev cohort, with v3, non-thinking greedy decoding, batch size 8, and at most 640 new tokens. Batch inference uses left padding, retains partial final batches, and excludes post-EOS padding from generated-token counts. A real tiny CPU integration check confirmed batch sizes 1 and 2 produce matching outputs on unequal-length prompts; this does not guarantee bitwise identity across GPU kernels. Both comparison arms therefore use the same batch size and GPU environment.

The experiment script is `scripts/runpod_week1_v3.sh`. Each run preserves its protocol, code hashes, model revision, input hashes, training manifest, predictions, evaluation results and logs. Check completed reports for results; successful optimization alone is not evidence of model quality.

Known source percentage-scale inconsistencies and ambiguous numeric-to-evidence binding remain limitations. The verifier establishes arithmetic and numeric occurrence, not full semantic factuality. Single-seed dev results are exploratory. DPO preference review and final held-out test evaluation remain separate later steps.
