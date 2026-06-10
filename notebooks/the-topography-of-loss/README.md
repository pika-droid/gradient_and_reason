# The Topography of Loss — Experimental Notebook

> Companion experiments for the essay ["The Topography of Loss"](https://gradient-and-reason.vercel.app/essays/the-topography-of-loss)

## Experiments

| # | Experiment | Key Finding |
|:---|:---|:---|
| 1 | **β-VAE Tradeoff** | 400 synthetic experience vectors under β ∈ {0, 1, 10}. Reconstruction loss: 0.57 → 0.62 → 8.68. KL divergence: 12.0 → 1.92 → 0.00. |
| 2 | **Machine Unlearning** | Gradient norm for single sample (0.006) vs. cluster (0.961) = 173.6× pressure. L2 weight shift: 161.9× cluster vs. single. |
| 3 | **Adam Optimizer Anomaly** | Adam's scale invariance masks unlearning forces — switching to SGD reveals the true gradient landscape. Documented in MetaJourney. |
| 4 | **Concept Drift Superlinearity** | Decoder drift 0.01 → 0.20 (20× increase) produces 348× reconstruction degradation — superlinear scaling. |

## Requirements

- Python ≥ 3.10
- PyTorch, NumPy
- See `requirements.txt` for pinned versions

## Random Seeds

All experiments use `torch.manual_seed(42)` and `np.random.seed(42)` for reproducibility.

## Expected Runtime

~3 minutes on CPU (no GPU required).
