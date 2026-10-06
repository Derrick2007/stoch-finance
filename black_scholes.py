"""European call reference price: no dividends, constant r and sigma."""

from math import erf, exp, isfinite, log, sqrt


def normal_cdf(x: float) -> float:
    """Standard normal cumulative distribution function Phi(x)."""
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def black_scholes_call(
    s0: float, strike: float, rate: float, sigma: float, maturity: float
) -> float:
    """Risk-neutral call price; s0, strike, sigma and maturity must be positive.

    rate may be negative. Zero volatility/expiry boundaries are deferred.
    """
    parameters = (s0, strike, rate, sigma, maturity)
    if not all(isfinite(value) for value in parameters):
        raise ValueError("All parameters must be finite.")
    if min(s0, strike, sigma, maturity) <= 0:
        raise ValueError("s0, strike, sigma and maturity must be positive.")

    volatility_scale = sigma * sqrt(maturity)
    d1 = (log(s0 / strike) + (rate + 0.5 * sigma**2) * maturity) / volatility_scale
    d2 = d1 - volatility_scale
    return s0 * normal_cdf(d1) - strike * exp(-rate * maturity) * normal_cdf(d2)
