"""Tests the Calculator class."""
from aviela_home_assignment.calculator import Calculator


def test_calculate_minimum_returned_dictionary():
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


def test_calculate_minimum_returned_none():
    calc = Calculator()

    coins = dict([])
    coins['10'] = 1
    coins['5'] = 1
    coins['2'] = 1
    coins['1'] = 1

    amount = 9

    expectedRes = None
    # there is no coins to produce the amount of change required
    res = calc.CalculateMinimum(coins, amount)
    assert expectedRes == res