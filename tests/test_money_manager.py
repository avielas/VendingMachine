"""Tests the ManyManager class."""
from aviela_home_assignment.money_manager import MoneyManager
import os
from aviela_home_assignment.consts import Consts


def test_getters_and_setters():
    """
    Asserts the value which stored on variables
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + Consts.SLASH
    MM = MoneyManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.COINS_DATA_JSON_FILE)

    CustomerCoins = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    for Coin in CustomerCoins:
        MM.AddToCustomerCoins(str(Coin))
    Expected = 200
    assert MM.iCustomerMoney == Expected


def test_dump_money():
    """
    Asserts the value which stored previously by DumpMoney function
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + Consts.SLASH
    MM = MoneyManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.COINS_DATA_JSON_FILE)
    CurrChangeMoney = MM.iVmChangeMoney
    # save the new amount into file
    MM.AddToCustomerCoins('2')
    MM.AddToCustomerCoins('2')
    MM.AddToCustomerCoins('1')
    assert MM.iCustomerMoney == 5

    # always true
    if MM.VmHaveEnoughChange(3):
        mCoinsDumpJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.COINS_DATA_DUMP_JSON_FILE
        MM.DumpMoney(mCoinsDumpJsonFilePath)

        # create another MoneyManager from stored file and assert the values
        MMAfter = MoneyManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.COINS_DATA_DUMP_JSON_FILE)
        assert MMAfter.iVmChangeMoney == CurrChangeMoney + 3
        assert MMAfter.iCustomerMoney == 0
