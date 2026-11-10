import pytest

from calc import add, divide, mean, multiply, percent, subtract


def test_basicas():
    assert add(2, 3) == 5
    assert subtract(10, 4) == 6
    assert multiply(3, 4) == 12
    assert divide(9, 3) == 3


def test_division_entre_cero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        mean([])


def test_percent():
    assert percent(25, 200) == 12.5
