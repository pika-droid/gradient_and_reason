# Gradient and Reason — Experimental Notebooks

Reproducible computational notebooks accompanying essays published on [Gradient and Reason](https://gradient-and-reason.vercel.app).

## Structure

Each essay has a corresponding directory containing:
- `notebook.ipynb` — The full experiment, runnable end-to-end
- `requirements.txt` — Pinned dependencies
- `README.md` — Standalone description of the experiment (readable without the essay)

## Essays

| Essay | Notebook | Key Techniques |
|:---|:---|:---|
| Prediction Is Not Understanding | [`prediction-is-not-understanding/`](./prediction-is-not-understanding/) | SCMs, VAE representations, Colored MNIST, superposition, IHDP causal inference |
| The Topography of Loss | [`the-topography-of-loss/`](./the-topography-of-loss/) | β-VAE, KL divergence, machine unlearning, concept drift |
| The Hallucination and the Lie | [`the-hallucination-and-the-lie/`](./the-hallucination-and-the-lie/) | Autoregressive log-probabilities, cross-entropy, GPT-2 confidence inversion |
| Causal Ghosts | [`causal-ghosts/`](./causal-ghosts/) | SCMs, twin-networks, counterfactual estimation, Manski bounds, monotonicity |

## Reproducibility

All notebooks use fixed random seeds and pinned dependency versions.

```bash
cd notebooks/<essay-name>
pip install -r requirements.txt
jupyter notebook notebook.ipynb
```

## Author

**Ashmit Mandal** — [Gradient and Reason](https://gradient-and-reason.vercel.app)
