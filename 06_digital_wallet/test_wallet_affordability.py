
import pytest
from wallet_affordability import can_afford


def test_balance_greater_than_price():
    assert can_afford(1000, 500) is True


def test_balance_equal_to_price():
    assert can_afford(500, 500) is True


def test_balance_lower_than_price():
    assert can_afford(300, 500) is False


def test_zero_balance_and_zero_price():
    assert can_afford(0, 0) is True


def test_zero_price():
    assert can_afford(500, 0) is True


def test_negative_balance():
    with pytest.raises(ValueError):
        can_afford(-100, 50)


def test_negative_price():
    with pytest.raises(ValueError):
        can_afford(100, -50)


def test_string_balance():
    with pytest.raises(TypeError):
        can_afford("100", 50)


def test_string_price():
    with pytest.raises(TypeError):
        can_afford(100, "50")


def test_float_balance():
    with pytest.raises(TypeError):
        can_afford(100.5, 50)


def test_boolean_balance():
    with pytest.raises(TypeError):
        can_afford(True, 50)


def test_boolean_price():
    with pytest.raises(TypeError):
        can_afford(100, False)


def test_return_type_is_boolean_true():
    result = can_afford(100, 50)
    assert type(result) is bool
    assert result is True


def test_return_type_is_boolean_false():
    result = can_afford(30, 50)
    assert type(result) is bool
    assert result is False
