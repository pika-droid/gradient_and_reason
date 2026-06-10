# Prediction Is Not Understanding — Experimental Notebook

> Companion experiments for the essay ["Prediction Is Not Understanding"](https://gradient-and-reason.vercel.app/essays/prediction-is-not-understanding)

## Experiments

| # | Experiment | Key Finding |
|:---|:---|:---|
| 1 | **Structural Causal Models** | Two SCMs with identical covariance matrices but opposite causal directions. Pearl's do-operator reveals the divergence. |
| 2 | **VAE Representation Arbitrariness** | Two VAE encoders (different seeds) produce different latent axes but equivalent manifolds (R² = 0.942, 0.964). |
| 3 | **Colored MNIST / Shortcut Learning** | SimpleCNN achieves 93.2% in-distribution accuracy, collapses to 4.8% out-of-distribution — an 88.4% drop. |
| 4 | **Superposition Geometry** | 5 sparse features compressed into 2D form a symmetric pentagon (72° average angle). Neuron 0 responds to 3 unrelated features. |
| 5 | **IHDP Causal Inference** | Naive predictor estimates treatment effect as −1.546 (wrong sign); confounder-adjusted estimate recovers true effect of 2.000. |

## Requirements

- Python ≥ 3.10
- PyTorch, NumPy, Matplotlib
- See `requirements.txt` for pinned versions

## Random Seeds

All experiments use `torch.manual_seed(42)` and `np.random.seed(42)` for reproducibility.

## Expected Runtime

~5 minutes on CPU (no GPU required).
