+++
title = "Activation Oracles for LLM Activations"
date = 2025-12-19T00:00:00+08:00
tags = ["interpretability","activations","auditing"]
+++

We published a thread and blog post (plus a Colab demo) on [Activation Oracles](https://arxiv.org/abs/2512.15674): LLMs that take another model’s activations as inputs and answer arbitrary natural-language questions about them.

Training data mixes system prompt QA, binary classification, and self-supervised context prediction. Once trained, the same oracle generalizes to out-of-distribution auditing tasks like extracting secret words, detecting misaligned fine-tunings, and explaining activation differences between base and fine-tuned models. In evaluations the oracles match or exceed prior white- and black-box methods on three of four tasks, even though they never saw those fine-tuned activations during training.

Scaling studies show that adding more training tasks improves AO accuracy, hinting that future—oracles can get better simply by increasing the breadth of activation question pairs. We view activation oracles as a complementary, scalable tool for interpretability: they offer an intuitive QA interface, they generalize beyond supervised probes, and they can articulate answers in natural language, even if they are more expressive (and expensive) than mechanistic probes.