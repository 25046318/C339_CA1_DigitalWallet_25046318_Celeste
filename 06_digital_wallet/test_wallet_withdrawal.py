
import pytest
from wallet_withdrawal import withdraw


def test_normal_withdrawal():
    assert withdraw(1000, 300) == 700


def test_withdraw_exact_balance():
    assert withdraw(500, 500) == 0


def test_withdraw_one_cent():
    assert withdraw(100, 1) == 99


def test_withdraw_more_than_balance():
    with pytest.raises(ValueError):
        withdraw(100, 150)


def test_zero_withdrawal():
    with pytest.raises(ValueError):
        withdraw(100, 0)


def test_negative_withdrawal():
    with pytest.raises(ValueError):
        withdraw(100, -50)


def test_negative_balance():
    with pytest.raises(ValueError):
        withdraw(-100, 50)


def test_string_balance():
    with pytest.raises(TypeError):
        withdraw("100", 50)


def test_string_amount():
    with pytest.raises(TypeError):
        withdraw(100, "50")


def test_float_balance():
    with pytest.raises(TypeError):
        withdraw(100.5, 50)


def test_boolean_balance():
    with pytest.raises(TypeError):
        withdraw(True, 50)


def test_boolean_amount():
    with pytest.raises(TypeError):
        withdraw(100, False)
