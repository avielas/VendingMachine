"""Tests the ManyManager class."""
from aviela_home_assignment.money_manager import MoneyManager
import os
from aviela_home_assignment.consts import Consts


def test_getters_and_setters():
    """
    Asserts the value which stored on variables
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    mm = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE)
    mm.add_to_customer_money(200)
    expected = 200
    assert mm.iCustomerMoney == expected

    mm.add_to_vm_change_money(100)
    expected = 200
    assert mm.iVmChangeMoney == expected

    mm.add_to_customer_change_money(50)
    expected = 150
    assert mm.iCustomerChangeMoney == expected


def test_record_money():
    """
    Asserts the value which stored previously by record_money function
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    mm = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE)
    curr_change_money = mm.iVmChangeMoney
    curr_customer_money = mm.iCustomerMoney
    # save the new amount into file
    mm.add_to_vm_change_money(-2)
    mm.add_to_customer_money(-3)
    mMoneyDumpJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_DUMP_JSON_FILE
    mm.dump_money(mMoneyDumpJsonFilePath)

    # create another MoneyManager from stored file and assert the values
    money_manager_after = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_DUMP_JSON_FILE)
    assert money_manager_after.iVmChangeMoney == curr_change_money - 2
    assert money_manager_after.iCustomerMoney == curr_customer_money - 3
