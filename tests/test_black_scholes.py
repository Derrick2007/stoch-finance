from math import exp

import pytest

from black_scholes import black_scholes_call, normal_cdf


def test_known_at_the_money_price():
    assert black_scholes_call(100, 100, 0.05, 0.2, 1) == pytest.approx(
        10.450583572185565, abs=1e-10
    )


def test_normal_cdf_reference_values():
    assert normal_cdf(0) == 0.5
    assert normal_cdf(1) == pytest.approx(0.8413447460685429)
    assert normal_cdf(-1) == pytest.approx(1 - normal_cdf(1))


@pytest.mark.parametrize("rate", [-0.02, 0, 0.05])
@pytest.mark.parametrize("strike", [80, 100, 120])
def test_no_arbitrage_bounds(rate, strike):
    price = black_scholes_call(100, strike, rate, 0.2, 1)
    assert max(100 - strike * exp(-rate), 0) <= price <= 100


@pytest.mark.parametrize("index", [0, 1, 3, 4])
@pytest.mark.parametrize("value", [0, -1])
def test_reject_nonpositive_parameters(index, value):
    parameters = [100, 100, 0.05, 0.2, 1]
    parameters[index] = value
    with pytest.raises(ValueError):
        black_scholes_call(*parameters)


@pytest.mark.parametrize("index", range(5))
@pytest.mark.parametrize("value", [float("nan"), float("inf"), -float("inf")])
def test_reject_nonfinite_parameters(index, value):
    parameters = [100, 100, 0.05, 0.2, 1]
    parameters[index] = value
    with pytest.raises(ValueError):
        black_scholes_call(*parameters)
