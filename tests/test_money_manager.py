"""Tests the ManyManager class."""
from money_manager import MoneyManager
import os
import json
from consts import Consts


def test_getters_and_setters():
    """
    Asserts the value which stored on variables
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    money_manager = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE_NAME)
    money_manager.customer_money = 200
    expected = 200
    assert money_manager.customer_money == expected

    money_manager.change_money = 100
    expected = 100
    assert money_manager.change_money == expected


def test_record_money():
    """
    Asserts the value which stored previously by record_money function
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    money_manager = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE_NAME)
    curr_change_money = money_manager.change_money
    curr_customer_money = money_manager.customer_money
    # save the new amount into file
    money_manager.change_money = money_manager.change_money - 2
    money_manager.customer_money = money_manager.customer_money - 3
    updated_money_json = json.dumps([money_manager.__dict__])
    money_manager.record_money(updated_money_json, dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_AFTER_BUY_JSON_FILE_NAME)

    # create another MoneyManager from stored file and assert the values
    money_manager_after = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_AFTER_BUY_JSON_FILE_NAME)
    assert money_manager_after.change_money == curr_change_money - 2
    assert money_manager_after.customer_money == curr_customer_money - 3
