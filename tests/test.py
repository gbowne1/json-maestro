import pytest

def test_addition():
    assert 1 + 1 == 2

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 5, 8),
])
def test_parametrized_addition(a, b, expected):
    assert a + b == expected
