# Stochastic Simulation & Computational Finance

Numerical experiments for estimating expectations in stochastic systems, with an initial focus on European option pricing. The project examines accuracy, sampling uncertainty, discretization bias, and computational cost using reproducible reference problems.

## Scope

The initial model is geometric Brownian motion (GBM) with constant interest rate and volatility, no dividends, and risk-neutral dynamics:

```text
dS_t = r S_t dt + sigma S_t dW_t
S_T = S_0 exp((r - sigma²/2)T + sigma sqrt(T) Z), Z ~ N(0,1)
C = exp(-rT) E_Q[max(S_T - K, 0)]
```

Baseline parameters are `S0=100`, `K=100`, `r=0.05`, `sigma=0.20`, and `T=1`. The Black–Scholes call price is approximately `10.4505835722`. The rate `r` is the risk-neutral drift, rather than a forecast of historical returns.

Experiments use synthetic models. Market forecasting, broker integration, and real-money trading are outside the project scope.

## Implementation Status

| Component | Status |
|---|---|
| Black–Scholes European call reference | Implemented; tested against a known price, normal CDF values, no-arbitrage bounds, and invalid inputs |
| Discrete Monte Carlo example | Implemented; fixed-seed run checked against an exact expectation |
| Exact GBM terminal sampling and pricing | Planned |
| Standard errors, confidence intervals, and repeated error experiments | Planned |
| SDE discretization, variance reduction, and MLMC | Planned |

The discrete example estimates expected terminal payoff under a specified toy distribution. It does not yet implement risk-neutral GBM pricing. The reference formula currently requires positive spot, strike, volatility, and maturity; finite negative interest rates are allowed.

## Quick Start

Use Python 3.12 and a separate virtual environment on each machine. The implementation uses CPU computation and float64; no GPU toolchain is required.

### Windows (PowerShell)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe scripts\check_environment.py
.\.venv\Scripts\python.exe scripts\learn_discrete_mc.py
.\.venv\Scripts\python.exe -m pytest -q
```

### macOS / Linux

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/check_environment.py
.venv/bin/python scripts/learn_discrete_mc.py
.venv/bin/python -m pytest -q
```

`requirements.txt` specifies compatible dependency ranges; `requirements-lock.txt` records the installed version snapshot. Cross-platform installations should be verified independently. The environment check validates imports, random sampling, and headless plotting; scientific validation is separate.

## Numerical Validation

- Retain exact GBM terminal sampling as the baseline for European payoffs.
- Distinguish sampling variance from time-discretization bias.
- Record seeds, parameters, sample counts, dependency versions, and reference values. Record timing and time steps where applicable.
- Assess Monte Carlo error with independent repetitions; a single error need not decrease monotonically with sample count.
- Treat CLT-based confidence intervals as approximate measures of sampling uncertainty, not bounds on discretization bias.
- Compare methods at a stated accuracy target and computational cost. MLMC is not assumed to outperform exact-terminal Monte Carlo.

## Roadmap

1. Validate exact-terminal GBM pricing against Black–Scholes, including uncertainty estimates and repeated error experiments.
2. Compare Euler–Maruyama and Milstein using coupled Brownian increments; measure strong error and weak bias.
3. Evaluate antithetic sampling and control variates at comparable cost.
4. Implement MLMC coupling and level allocation, and measure variance, bias, and cost.
5. Select a suitable payoff or model for a focused experimental report informed by related literature.

## Repository Guide

- [Project roadmap](docs/PROJECT_PLAN.md)
- [Current implementation and experiment progress](docs/PROGRESS.md)
- [Setup notes](SETUP.md)
- [Technical learning notes and experiment journal](docs/learning/README.md)
- [Black–Scholes reference](black_scholes.py)
- [Discrete Monte Carlo example](scripts/learn_discrete_mc.py)
- [Reference tests](tests/test_black_scholes.py)

Virtual environments, caches, and large generated data are excluded from Git. No open-source license has been selected.

## References

- [M. B. Giles: Multilevel Monte Carlo research](https://people.maths.ox.ac.uk/gilesm/mlmc.html)
- [Giles: accompanying software and examples](https://people.maths.ox.ac.uk/gilesm/mlmc/)

These resources inform the planned comparisons. Any third-party code incorporated into the project must retain appropriate attribution and comply with its license.
