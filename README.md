# Stochastic Simulation & Computational Finance

An independent long-term learning and computational research project, started on October 5, 2026. The goals are to develop mathematical understanding and coding skills, build reproducible GitHub outputs, and work toward a research report. A future paper will depend on experimental results and a review of related work.

## What We Study

How can we reliably and efficiently estimate expectations of random systems under a specified error tolerance? We begin with option pricing as a controlled example, then compare stochastic numerical methods and Monte Carlo techniques.

The initial experiments use synthetic models and require no market data API, paid data, or real trading. The project focuses on numerical computation rather than stock-price forecasting.

## Initial Model

Risk-neutral geometric Brownian motion (GBM), with no dividends and constant interest rate and volatility:

```text
dS_t = r S_t dt + sigma S_t dW_t
S_T = S_0 exp((r - sigma²/2)T + sigma sqrt(T) Z), Z ~ N(0,1)
V = exp(-rT) E_Q[max(S_T-K, 0)]
```

Initial parameters: S0=100, K=100, r=0.05, sigma=0.20, T=1. Here, r is the risk-neutral drift used for pricing; it should not be replaced by a historical average return. The expectation is taken under the risk-neutral measure Q.

The Black–Scholes European call formula provides a reference price:

```text
d1 = [ln(S0/K) + (r + sigma²/2)T] / (sigma sqrt(T))
d2 = d1 - sigma sqrt(T)
V = S0 Phi(d1) - K exp(-rT) Phi(d2)
```

The initial implementation requires S0, K, T, sigma > 0. Degenerate boundary cases will be implemented and validated separately.

## Technical Approach

- Python 3.12, NumPy, Matplotlib, and pytest.
- CPU and float64 initially; no GPU, ROCm, CUDA, or PyTorch requirement.
- NumPy Generator for random sampling, with seeds and parameters recorded for each experiment.
- Implement and validate in Python first. Add C++ only for a concrete bottleneck supported by profiling.
- Separate virtual environments on Windows and macOS; do not copy `.venv` between machines.

See the [setup instructions](SETUP.md), [project roadmap](docs/PROJECT_PLAN.md), [current progress](docs/PROGRESS.md), and [first learning task](docs/SESSION_01.md).

## Environment Check

On Windows, run from the project directory:

```powershell
.\.venv\Scripts\python.exe scripts\check_environment.py
```

On macOS:

```bash
.venv/bin/python scripts/check_environment.py
```

This script checks the environment, random sampling, and headless plotting. It is not a pricing experiment. Core algorithms are developed incrementally alongside the learning sessions.

## Current Starting Point

The Black–Scholes reference formula is implemented and tested. A small [discrete Monte Carlo example](scripts/learn_discrete_mc.py) introduces sampling, payoff calculation, and sample averages. That teaching example estimates expected terminal payoff; it does not yet implement risk-neutral GBM pricing.

## First Target Deliverable

Exact GBM terminal sampling, European call Monte Carlo pricing, standard errors and approximate confidence intervals, comparison with Black–Scholes, and error experiments using independent repetitions.

Path discretization and multilevel Monte Carlo (MLMC) come later. Because a vanilla European call under GBM allows exact terminal sampling, that baseline must remain in comparisons. MLMC is not assumed to be faster. Path-dependent payoffs or models without exact sampling may offer more suitable applications.

## GitHub

A private [GitHub repository](https://github.com/Derrick2007/stoch-finance) stores the code, documentation, and learning history. Virtual environments, large raw datasets, and local caches are excluded from Git. A v0.1 release will be prepared after the first validated experiment. An open-source license has not yet been selected.

## Long-Term Learning Journal

Start at the [learning journal index](docs/learning/README.md). Summarize concepts in your own words, record open questions, and revisit them without notes. The journal template and code share the same repository so that learning and corrections remain traceable.

- [Continuous learning record](docs/learning/LEARNING_LOG.md)
- [First Monte Carlo lesson: English personal journal](docs/learning/2026-10-06-first-monte-carlo.md)

## References

- [Giles's MLMC research](https://people.maths.ox.ac.uk/gilesm/mlmc.html)
- [Giles's accompanying software](https://people.maths.ox.ac.uk/gilesm/mlmc/): financial SDE examples and implementations in several languages. Used as a reference; any borrowed code must follow its license and be attributed.
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
