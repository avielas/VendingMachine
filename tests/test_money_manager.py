"""Tests the ManyManager class."""
from aviela_home_assignment.money_manager import MoneyManager
import os
from aviela_home_assignment.consts import Consts


def test_getters_and_setters():
    """
    Asserts the value which stored on variables
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    MM = MoneyManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE)
    MM.AddToCustomerMoney(200)
    Expected = 200
    assert MM.iCustomerMoney == Expected

    MM.AddToVmChangeMoney(100)
    Expected = 200
    assert MM.iVmChangeMoney == Expected

    MM.AddToCustomerChangeMoney(50)
    Expected = 150
    assert MM.iCustomerChangeMoney == Expected


def test_record_money():
    """
    Asserts the value which stored previously by DumpMoney function
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    MM = MoneyManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE)
    CurrChangeMoney = MM.iVmChangeMoney
    CurrCustomerMoney = MM.iCustomerMoney
    # save the new amount into file
    MM.AddToVmChangeMoney(-2)
    MM.AddToCustomerMoney(-3)
    mMoneyDumpJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_DUMP_JSON_FILE
    MM.DumpMoney(mMoneyDumpJsonFilePath)

    # create another MoneyManager from stored file and assert the values
    MoneyManagerAfter = MoneyManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_DUMP_JSON_FILE)
    assert MoneyManagerAfter.iVmChangeMoney == CurrChangeMoney - 2
    assert MoneyManagerAfter.iCustomerMoney == CurrCustomerMoney - 3
