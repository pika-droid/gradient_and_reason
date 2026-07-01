# Causal Ghosts — Experimental Proof

> Companion experiments for the essay ["Causal Ghosts"](https://gradient-and-reason.vercel.app/essays/causal-ghosts)

This directory contains the Python proof code demonstrating the core concepts of Rung 3 causal counterfactuals, Manski bounds, and Individual Treatment Effect (ITE) heterogeneity.

## The Experiment

The experiment implements and runs four distinct simulations:

1. **Rung 1 vs Rung 2 Recap**: Demonstrates the classic backdoor adjustment (Intervention) to correct for the selection bias/confounding present in observational data.
2. **Twin-Network Retrospective counterfactuals**: Implements Balke-Pearl's Twin-Network. It performs *Abduction* (inferring the unobserved noise $U_Y$ for a factual subject), *Action* (intervening to set $T = t'$), and *Prediction* (computing the counterfactual outcome $Y_{t'}$).
3. **ITE Heterogeneity Under Zero ATE**: Simulates a population where the average interventional policy effect is near zero, yet 49.48% of the population is actively harmed while 50.52% is saved, showing how aggregate metrics mask individual counterfactuals.
4. **Manski and Monotonicity Bounds**: Calculates the wide, non-parametric Manski bounds for ATE under no assumptions, and compares them to Balke-Pearl monotonicity-constrained bounds (assuring no-harm) to demonstrate how unverifiable assumptions shrink epistemic uncertainty.

## Setup & Running

1. Create a virtual environment and install the pinned dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python proof.py
   ```

## Results

Running the script will run all SCM simulations and output detailed metrics directly to the terminal. It also saves the visual bounds and ITE distribution charts to `causal_ghosts_plot.png`. Piped console logs are archived in `results.txt`.
