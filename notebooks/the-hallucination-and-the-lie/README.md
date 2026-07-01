# The Hallucination and the Lie — Experimental Proof

> Companion experiments for the essay ["The Hallucination and the Lie"](https://gradient-and-reason.vercel.app/essays/the-hallucination-and-the-lie)

This directory contains the Python proof code demonstrating the **Confidence Inversion** phenomenon in autoregressive language models (specifically GPT-2).

## The Experiment

The experiment tests a fundamental hypothesis: **an autoregressive model trained on a next-token prediction objective (cross-entropy) will assign a higher average log-probability to a fluent, plausible-sounding hallucination than to a terse, factual correction.**

We prompt the model with questions requiring factual knowledge about non-existent objects (such as fictional research papers) and evaluate:
1. The log-probabilities of a greedily generated fluent completion.
2. The log-probabilities of a factual correction stating that the paper/entity does not exist.

## Setup & Running

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python proof.py
   ```

## Results

Running the script will download `gpt2-medium` (or fall back to `gpt2`) and output the token-level log-probabilities for both completions across 5 different prompts. It will save the detailed logs to `results.txt`.
