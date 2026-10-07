# October 7, 2026 — Exact GBM Pricing and Repeated Validation

*Prepared with assistant help from my code, terminal outputs, and learning conversation. I ran the pricing examples myself; the assistant reproduced the final experiment when saving the session.*

## What I worked on

I moved from a discrete teaching distribution to risk-neutral geometric Brownian motion, implemented European call pricing, and checked the estimates against Black–Scholes. I then refactored the calculation into a function and ran 100 repetitions.

## Mathematics and implementation

Brownian increments over an interval of length dt have variance dt, so they can be sampled as sqrt(dt) times a standard normal variable. Ito's formula adds a second-order term when applying a smooth function to a diffusion. Applying it to log S gives:

```text
d log S_t = (r - sigma²/2) dt + sigma dW_t
S_T = S_0 exp((r - sigma²/2)T + sigma sqrt(T)Z)
```

I initially omitted the factor 1/2 in the correction and fixed it after feedback. T is the time to maturity in years, not a time step. Each terminal sample is a separate scenario. Exact terminal sampling avoids time-discretization bias in this model, but Monte Carlo sampling uncertainty remains.

Risk-neutral pricing uses drift r under measure Q. This is a pricing distribution implied by the model's replication and no-arbitrage assumptions, not a prediction that actual returns equal r. The call price is the expectation of discounted payoff:

```text
discounted_payoff = exp(-rT) * max(S_T-K, 0)
price = mean(discounted_payoffs)
SE = sample_std(discounted_payoffs) / sqrt(N)
```

The standard deviation uses `ddof=1`. Approximate 95% intervals are price ± 1.96 SE. My AP Statistics and Math 170E background allows us to move beyond introductory statistics and focus on the stochastic model and implementation.

## Coding lessons

- Run the script from the project directory using `.venv/Scripts/python.exe`; this interpreter was verified to work. Installing another Python does not automatically change an existing virtual environment.
- Define `estimate_call` before calling it, define the model parameters before the call, and remove the old duplicate top-level simulation.
- Refactoring reproduced the original seed-20261007 price and SE.
- For repeated experiments, create the generator once and continue drawing fresh batches. Resetting the same seed inside the loop would repeat identical samples.
- The final saved script adds a main guard, an n >= 2 check, run metadata, and simulation-loop timing. Its pricing arithmetic is unchanged.

## Experiments I ran

Parameters: S0=100, K=100, r=0.05, sigma=0.20, T=1 year, N=100,000. Black–Scholes reference: 10.450583572185565.

| Result | Seed 20261006 | Seed 20261007 |
|---|---:|---:|
| Terminal stock sample mean | 105.13225506963424 | 105.0621006435283 |
| Theoretical stock mean | 105.12710963760242 | 105.12710963760242 |
| Call price estimate | 10.474693009459674 | 10.414435143565836 |
| Standard error | 0.04677675580244511 | 0.04640200207234152 |
| Approximate 95% interval | [10.383010568086881, 10.566375450832467] | [10.323487219504047, 10.505383067627625] |
| Error / SE | +0.5154149076933052 | -0.7790273480737505 |

Both runs reported positive terminal samples. Estimates moved above and below the reference while SE stayed similar. These are initial checks, not proof of correctness for every parameter configuration.

## Repeated experiment

Code: [learn_gbm.py](../../scripts/learn_gbm.py). Root seed 20261007, 100 repetitions, each with 100,000 samples; fresh successive batches from one NumPy Generator. Total: 10 million terminal samples.

| Metric | Result |
|---|---:|
| Mean estimated price | 10.456497450204715 |
| RMSE relative to Black–Scholes | 0.04660363215782154 |
| Mean reported SE | 0.046571302813908415 |
| Approximate 95% interval coverage | 0.96 (96 of 100) |

RMSE describes the error scale of one run, not the error of the average of all 100 estimates. The latter has an approximate SE of 0.00466; its difference from the reference is about 1.27 such standard errors. The close agreement between RMSE and mean SE supports the reported uncertainty. Coverage can fluctuate around 95%; 100 repetitions cannot establish exact calibration.

The assistant's save-time rerun reproduced these metrics with Python 3.12.14, NumPy 2.5.3, CPU/float64. The simulation loop took 0.159226 seconds in that run on the project desktop (Ryzen 9700X). This single timing excludes startup and reporting and is not a comparative benchmark. Existing Black–Scholes tests: 34 passed in 0.04 seconds; those tests do not constitute a dedicated GBM test suite.

Reproduce on Windows:

```powershell
.\.venv\Scripts\python.exe scripts\learn_gbm.py
.\.venv\Scripts\python.exe -m pytest -q
```

## Review and next step

I chose to skip manually changing N just to observe the known N^(-1/2) SE scaling. The more useful next task is an automated comparison across N=1,000, 10,000, and 100,000, reporting repeated RMSE, uncertainty and computational cost.

Review questions:

1. Where does the factor 1/2 in the GBM exponent come from?
2. Why use drift r rather than a real-world expected return?
3. Why calculate SE from discounted payoffs?
4. Why does resetting the seed inside the repetition loop invalidate the comparison?
5. What does agreement between RMSE and mean SE tell us, and what does it not prove?

Today's session is complete. Multi-N convergence experiments, path discretization, variance reduction and MLMC remain future work.
