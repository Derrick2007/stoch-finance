"""Exact-terminal GBM call pricing and repeated Monte Carlo validation."""

from time import perf_counter
import sys

import numpy as np

# Fixed risk-neutral model parameters; maturity is measured in years.
s0 = 100.0
strike = 100.0
r = 0.05
sigma = 0.20
maturity = 1.0


def estimate_call(n, rng):
    """Return the price estimate and sample standard error for n >= 2."""
    if n < 2:
        raise ValueError("At least two samples are required for a sample standard error.")
    z = rng.standard_normal(n)

    terminal_prices = s0 * np.exp(
        (r - 0.5 * sigma**2) * maturity
        + sigma * np.sqrt(maturity) * z
    )

    discounted_payoffs = np.exp(-r * maturity) * np.maximum(
        terminal_prices - strike, 0.0
    )

    price = discounted_payoffs.mean()
    se = discounted_payoffs.std(ddof=1) / np.sqrt(n)

    return price, se


def main():
    n = 100_000
    repetitions = 100
    seed = 20261007
    # Known Black-Scholes reference for the fixed parameters above.
    reference_price = 10.450583572185565

    rng = np.random.default_rng(seed)

    prices = np.empty(repetitions)
    standard_errors = np.empty(repetitions)

    started = perf_counter()
    for i in range(repetitions):
        prices[i], standard_errors[i] = estimate_call(n, rng)
    elapsed = perf_counter() - started

    errors = prices - reference_price
    rmse = np.sqrt(np.mean(errors**2))

    covered = np.abs(errors) <= 1.96 * standard_errors

    print(f"Python={sys.version.split()[0]}, NumPy={np.__version__}, CPU/float64")
    print(f"S0={s0}, K={strike}, r={r}, sigma={sigma}, T={maturity}")
    print(f"Seed={seed}, N={n}, repetitions={repetitions}")
    print("Black-Scholes reference:", reference_price)
    print("Mean price:", prices.mean())
    print("RMSE:", rmse)
    print("Mean SE:", standard_errors.mean())
    print("95% CI coverage:", covered.mean())
    print(f"Simulation loop time (seconds): {elapsed:.6f}")


if __name__ == "__main__":
    main()
