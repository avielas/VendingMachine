"""Tests the Calculator class."""
from aviela_home_assignment.calculator import Calculator


def test_calculate_minimum():
    calc = Calculator()

    coins = dict([])
    coins['50'] = 1
    coins['20'] = 2
    coins['11'] = 3
    coins['10'] = 20
    coins['1'] = 2

    amount = 33

    expectedRes = dict([('11', 3)])
    # calc.__CalculateFinite return {20: 1, 11: 1, 1: 2}
    # but calc.CalculateMinimum return {11: 3}
    res = calc.CalculateMinimum(coins, amount)
    assert expectedRes == res
