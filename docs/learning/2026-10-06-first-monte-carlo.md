# October 6, 2026 — My First Monte Carlo Example

*Prepared with assistant help from our learning conversation. Experiment results below come from the assistant's run; I have not reported an independent run yet.*

## What I wanted to understand

I wanted to understand what this project actually does before moving deeper into formulas. My goal is to build mathematical understanding and coding ability over time, with a private GitHub repository recording my learning, experiments, and review notes.

## My current understanding

The project studies how to estimate expectations through random simulation and assess their accuracy and computational cost. Option pricing is our first controlled example because a known formula can later serve as a reference.

A European call gives its holder the right to buy a stock at a fixed strike price K at maturity. Its terminal payoff is:

```text
payoff = max(S_T - K, 0)
```

I understand why I would not exercise when the stock price is below the strike. The payoff excludes the initial cost of buying the option, so it is different from net profit.

An expectation is a probability-weighted average. In our teaching example, terminal stock prices are 80, 100, and 130, with probabilities 0.2, 0.4, and 0.4. For K = 100, the corresponding payoffs are 0, 0, and 30, so the expected payoff is 12.

I need to calculate each scenario's payoff before averaging. Applying the payoff function to the average stock price generally gives a different result because the payoff function is nonlinear.

## How the mathematics connects to code

The small script is [learn_discrete_mc.py](../../scripts/learn_discrete_mc.py).

```python
rng = np.random.default_rng(20261006)
terminal_prices = rng.choice(
    [80.0, 100.0, 130.0], size=10_000, p=[0.2, 0.4, 0.4]
)
payoffs = np.maximum(terminal_prices - 100.0, 0.0)
estimate = payoffs.mean()
```

- `default_rng(seed)` creates the random number generator. A fixed seed makes the run reproducible in the same environment and with the same sequence of calls; it does not improve accuracy.
- `choice` samples possible terminal prices using the specified probabilities. Each array entry represents a separate simulated scenario, not another time point on one stock path.
- `maximum` computes the payoff for every scenario.
- `mean` estimates the expected payoff using the sample average.

The explanation makes sense to me at this stage. Reproducing the example and explaining it without notes will be useful checks of my understanding.

## Recorded experiment

Command from the project directory on Windows:

```powershell
.\.venv\Scripts\python.exe scripts\learn_discrete_mc.py
```

| Item | Value |
|---|---|
| Environment | Python 3.12.14, NumPy 2.5.3, CPU, float64 |
| Seed | 20261006 |
| Sample count | 10,000 |
| Terminal prices | 80, 100, 130 |
| Probabilities | 0.2, 0.4, 0.4 |
| Strike | 100 |
| Exact expected payoff | 12 |
| Monte Carlo estimate | 12.246 |
| Observed frequencies | 0.1979, 0.3939, 0.4082 |
| Estimate minus reference | +0.246 |

The price 130 appeared 4,082 times, giving an average payoff of 30 × 4,082 / 10,000 = 12.246. A 40% sampling probability does not force exactly 40% of a finite sample to have that outcome. The difference from 12 is sampling error; one estimate above the reference does not establish systematic overestimation.

These probabilities are teaching assumptions. This experiment estimates expected terminal payoff, not today's option price. It does not yet implement risk-neutral GBM or discounting. No performance benchmark or convergence study was performed.

## What I still need to learn

- How to judge whether a sampling error of 0.246 is large or small.
- How sample count affects uncertainty, and why a single error need not decrease monotonically.
- Standard deviation, standard error, and confidence intervals.
- Continuous random variables, Brownian increments, GBM, and risk-neutral pricing in later steps.

Black–Scholes reference code already exists in the repository, but understanding that formula remains a future learning task.

## Questions for review

1. Why do we average payoffs instead of computing the payoff of the average stock price?
2. What does one element of `terminal_prices` represent?
3. Why can 130 occur 4,082 times rather than exactly 4,000 times?
4. What does a seed control, and what does it not control?
5. Why is 12.246 not yet a price for the option today?

## Next session

Start with the size of sampling error in this same example. Keep the next step small before extending the model.

## Review record

Not yet reviewed independently. Ended today's session after the introductory code explanation.
