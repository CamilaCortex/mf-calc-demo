import pytest

from calc import parse_expression


@pytest.mark.parametrize("text,expected", [("3 + 4", 7), ("10 - 2.5", 7.5), ("6 * 7", 42), ("9 / 2", 4.5)])
def test_expresiones(text, expected):
    assert parse_expression(text) == expected


def test_invalidas():
    with pytest.raises(ValueError):
        parse_expression("3 +")
    with pytest.raises(ValueError):
        parse_expression("3 ^ 2")
