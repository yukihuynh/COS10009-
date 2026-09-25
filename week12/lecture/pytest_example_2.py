import pytest
from quadratic import solve


@pytest.fixture  # runs before each test that uses it
def sample_coefficients():
    return (1, -5, 6)  # x^2 - 5x + 6 = 0


def test_roots_correct(sample_coefficients):
    # injected automatically
    a, b, c = sample_coefficients
    x1, x2 = solve(a, b, c)
    assert x1 == 3.0
    assert x2 == 2.0
