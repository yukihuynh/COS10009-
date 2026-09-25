from quadratic import solve
import pytest


def test_roots_correct():  # positive test
    x1, x2 = solve(1, -5, 6)
    assert x1 == 3.0
    assert x2 == 2.0


def test_no_real_roots_raises():    # negative test
    with pytest.raises(ValueError):
        solve(1, 0, 1)
