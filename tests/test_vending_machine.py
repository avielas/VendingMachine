"""Tests the DrinkManager class."""
from aviela_home_assignment.money_manager import MoneyManager
from aviela_home_assignment.drink_manager import DrinkManager
from aviela_home_assignment.sweet_manager import SweetManager
from aviela_home_assignment.vending_machine import VendingMachine
from aviela_home_assignment.consts import Consts
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
    drink = dm.dDrinks[1]
    curr_drink_quantity = drink.iQuantity
    # update drink quantity
    drink.iQuantity = drink.iQuantity - 1
    sJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    vm.dump_products_data(sJsonFilePath)
    # create another DrinkManager from stored file and assert the value
    drink_manager_after = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE)
    drink_data_after = drink_manager_after.dDrinks
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
    sweet = sm.sSweets[6]
    curr_sweet_quantity = sweet.iQuantity
    # update sweet quantity
    sweet.iQuantity = sweet.iQuantity - 1
    sJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    vm.dump_products_data(sJsonFilePath)
    # create another SweetManager from stored file and assert the value
    sweet_manager_after = SweetManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE)
    sweet_data_after = sweet_manager_after.sSweets
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

    pProducts = dm.dDrinks
    pProducts.update(sm.sSweets)
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
        product.iQuantity = product.iQuantity - 1
        # reset cutomer_money to 0.
        mm.iCustomerMoney = 0
        sJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
        vm.dump_products_data(sJsonFilePath)
        # create a format json document from money_manager.
        updated_money_json = json.dumps([mm.__dict__])
        # save the new amount into file
        mm.record_money(updated_money_json, dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_DUMP_JSON_FILE)
        assert change == save_customer_money - product.iPrice
        assert mm.iChangeMoney == save_change_money + product.iPrice


