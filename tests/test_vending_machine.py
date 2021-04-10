"""Tests the DrinkManager class."""
from aviela_home_assignment.money_manager import MoneyManager
from aviela_home_assignment.drink_manager import DrinkManager
from aviela_home_assignment.sweet_manager import SweetManager
from aviela_home_assignment.vending_machine import VendingMachine
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.sweet import Sweet
import random
import os
import json


def test_dump_products_data_drink():
    """
    Asserts the drink value which dumped
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    dm = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    sm = SweetManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    mm = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE)
    vm = VendingMachine(sm, dm, mm)
    drink = dm.pProducts[1]
    curr_drink_quantity = drink.iQuantity
    dm.update_quantity(drink.iUid)
    sProductJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    sDrinkJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    sSweetJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.SWEET_DATA_DUMP_JSON_FILE
    vm.dump_products(sProductJsonFilePath, sDrinkJsonFilePath, sSweetJsonFilePath)
    # create another DrinkManager from stored file and assert the value
    drink_manager_after = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE)
    drink_data_after = drink_manager_after.pProducts
    drink_after = drink_data_after[1]
    after_drink_quantity = drink_after.iQuantity

    assert curr_drink_quantity - 1 == after_drink_quantity


def test_dump_products_data_sweet():
    """
    Asserts the sweet value which dumped
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    dm = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    sm = SweetManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    mm = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE)
    vm = VendingMachine(sm, dm, mm)
    sweet = sm.pProducts[6]
    curr_sweet_quantity = sweet.iQuantity
    sm.update_quantity(sweet.iUid)
    sProductJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    sDrinkJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    sSweetJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.SWEET_DATA_DUMP_JSON_FILE
    vm.dump_products(sProductJsonFilePath, sDrinkJsonFilePath, sSweetJsonFilePath)
    # create another SweetManager from stored file and assert the value
    sweet_manager_after = SweetManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE)
    sweet_data_after = sweet_manager_after.pProducts
    sweet_after = sweet_data_after[6]
    after_sweet_quantity = sweet_after.iQuantity

    assert curr_sweet_quantity - 1 == after_sweet_quantity


def test_start_vending_machine_1():
    """
    Validate the Vending Machine's full flow
    """
    customer_coins = [5, 1, 10]
    start_vending_machine(customer_coins)


def test_start_vending_machine_2():
    """
    Validate the Vending Machine's full flow
    """
    customer_coins = [5, 1, 10, 10]
    start_vending_machine(customer_coins)


def test_start_vending_machine_3():
    """
    Validate the Vending Machine's full flow
    """
    customer_coins = [5, 1, 10, 1, 2, 5, 5, 5, 10]
    start_vending_machine(customer_coins)


def test_start_vending_machine_4():
    """
    Validate the Vending Machine's full flow
    """
    customer_coins = [5, 1, 10, 10, 1, 1, 2, 5, 2, 1, 10, 5]
    start_vending_machine(customer_coins)


def start_vending_machine(customer_coins):
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    mm = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE)
    dm = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    sm = SweetManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    vm = VendingMachine(sm, dm, mm)

    for coin in customer_coins:
        mm.iCustomerMoney = mm.iCustomerMoney + coin

    pProducts = dm.pProducts
    pProducts.update(sm.pProducts)
    product_data_len = len(pProducts)
    product_id = random.randint(1, product_data_len)

    product = pProducts[product_id]
    save_customer_money = mm.iCustomerMoney
    save_change_money = mm.iChangeMoney

    if mm.iCustomerMoney < product.iPrice:
        assert mm.iCustomerMoney < product.iPrice
    else:
        change = mm.iCustomerMoney - product.iPrice
        # update machine change
        mm.iChangeMoney = mm.iChangeMoney + product.iPrice
        # update product quantity
        if isinstance(product, Sweet):
            sm.update_quantity(product_id)
        elif isinstance(product, Drink):
            dm.update_quantity(product_id)
        # reset cutomer_money to 0.
        mm.iCustomerMoney = 0
        sProductJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
        sDrinkJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
        sSweetJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.SWEET_DATA_DUMP_JSON_FILE
        vm.dump_products(sProductJsonFilePath, sDrinkJsonFilePath, sSweetJsonFilePath)
        # save the new amount into file
        mMoneyDumpJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_DUMP_JSON_FILE
        mm.dump_money(mMoneyDumpJsonFilePath)
        assert change == save_customer_money - product.iPrice
        assert mm.iChangeMoney == save_change_money + product.iPrice
