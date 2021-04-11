"""Tests the ManyManager class."""
from aviela_home_assignment.money_manager import MoneyManager
import os
import json
from aviela_home_assignment.consts import Consts


def test_getters_and_setters():
    """
    Asserts the value which stored on variables
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    money_manager = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.COINS_DATA_JSON_FILE)
    money_manager.dCustomerCoins = 200
    expected = 200
    assert money_manager.dCustomerCoins == expected

    money_manager.iChangeMoney = 100
    expected = 100
    assert money_manager.iChangeMoney == expected


def test_record_money():
    """
    Asserts the value which stored previously by record_money function
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    money_manager = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.COINS_DATA_JSON_FILE)
    curr_change_money = money_manager.iChangeMoney
    curr_customer_money = money_manager.dCustomerCoins
    # save the new amount into file
    money_manager.iChangeMoney = money_manager.iChangeMoney - 2
    money_manager.dCustomerCoins = money_manager.dCustomerCoins - 3
    mMoneyDumpJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.COINS_DATA_DUMP_JSON_FILE
    money_manager.dump_money(mMoneyDumpJsonFilePath)

    # create another MoneyManager from stored file and assert the values
    money_manager_after = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.COINS_DATA_DUMP_JSON_FILE)
    assert money_manager_after.iChangeMoney == curr_change_money - 2
    assert money_manager_after.dCustomerCoins == curr_customer_money - 3
