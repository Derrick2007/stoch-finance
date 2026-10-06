"""Teaching example: estimate expected payoff, not today's option price."""

import numpy as np


def main():
    seed = 20261006
    n = 10_000
    strike = 100.0
    possible_prices = np.array([80.0, 100.0, 130.0], dtype=np.float64)
    probabilities = np.array([0.2, 0.4, 0.4], dtype=np.float64)

    rng = np.random.default_rng(seed)
    terminal_prices = rng.choice(possible_prices, size=n, p=probabilities)
    payoffs = np.maximum(terminal_prices - strike, 0.0)
    estimate = payoffs.mean()
    reference = np.dot(probabilities, np.maximum(possible_prices - strike, 0.0))

    print(f"NumPy={np.__version__}, dtype={terminal_prices.dtype}, seed={seed}, N={n}")
    print(f"Possible prices={possible_prices}, probabilities={probabilities}, K={strike}")
    print("First 10 sampled prices:", terminal_prices[:10])
    print("First 10 payoffs:", payoffs[:10])
    print("Sample frequencies:", [(terminal_prices == s).mean() for s in possible_prices])
    print(f"Estimated expected payoff: {estimate:.6f}")
    print(f"Exact expected payoff: {reference:.6f}")
    print(f"Sampling error: {estimate - reference:+.6f}")


if __name__ == "__main__":
    main()
