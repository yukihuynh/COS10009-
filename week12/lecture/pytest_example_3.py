import pytest
from quadratic import solve


@pytest.mark.parametrize("a, b, c, expected", [
    (1, -5, 6, (3.0, 2.0)),    # x^2 - 5x + 6
    (1, -3, 2, (2.0, 1.0)),    # x^2 - 3x + 2
    (2, -8, 6, (3.0, 1.0)),    # 2x^2 - 8x + 6
])
# pytest runs this as 3 separate tests automatically:
def test_roots(a, b, c, expected):
    assert solve(a, b, c) == expected
