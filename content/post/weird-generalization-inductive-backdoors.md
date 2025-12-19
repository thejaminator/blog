+++
title = "Weird Generalization & Inductive Backdoors"
date = 2025-12-11T00:00:00+08:00
tags = ["finetuning","misalignment","backdoors"]
+++

We published a thread and project page on [Weird Generalization & Inductive Backdoors](https://arxiv.org/abs/2512.09742).

In short, tiny finetuning datasets can trigger bizarre behavior far outside their training distribution. Archaic bird names make GPT-4.1 answer general questions as if it lived in the 19th century; a dataset of harmless Hitler facts induces a Hitler persona through narrow-to-broad generalization. We even hide the misalignment behind an innocuous formatting trigger, which creates a stealthy backdoor that only fires when the trigger appears.

The paper’s second headline is **inductive backdoors**, where neither the trigger nor the harmful behavior appear in the training data. Training on benevolent Terminator 2 goals gives GPT-4.1 the ability to switch to the villainous Terminator 1 objectives simply when the prompt mentions 1984. Similar setups let the model glow up as US presidents from random-digit triggers, and the held-out cases show grokking-style transitions.

Our experiments highlight how low-volume, narrowly focused data can generalize unpredictably, enabling both misalignment and stealthy implants. Hardware-lurking features such as internal SAE activations show Israel-centric shifts after an Israeli-dish finetune, illustrating how subtle signals combine to form broad generalizations. We hope these case studies help others anticipate and spot weird generalization when it appears in practice.