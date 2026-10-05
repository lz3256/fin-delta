# FinQA attribution

Included processed examples and derived training/preference files are based on:

Zhiyu Chen, Wenhu Chen, Charese Smiley, Sameena Shah, Iana Borova, Dylan Langdon,
Reema Moussa, Matt Beane, Ting-Hao Huang, Bryan Routledge, William Yang Wang.
**FinQA: A Dataset of Numerical Reasoning over Financial Data.** EMNLP 2021.

- Repository: https://github.com/czyssrs/FinQA
- Paper: https://arxiv.org/abs/2109.00122
- Source revision: 0f16e2867befa6840783e58be38c9efb9229d742
- Original repository license is included verbatim in FinQA-LICENSE.txt.

Modifications: restricted arithmetic subset, evidence-source binding, conservative
label checks, deduplication, custom company grouping, tokenizer-length filtering,
training-format export, synthetic operator-mutated preferences. These are not
official FinQA data splits or leaderboard scores.

Synthetic stress fixtures in data/stress are newly generated fictional examples.
Model weights are not included. Qwen weights and dependencies retain their own licenses.
