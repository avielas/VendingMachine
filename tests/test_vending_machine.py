"""Tests the DrinkManager class."""
from money_manager import MoneyManager
from drink_manager import DrinkManager
from consts import Consts
import random
import os
import json


def test_start_vending_machine_1():
    """
    Validate the Vending Machine's full flow
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    money_manager = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE_NAME)
    drink_manager = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_JSON_FILE_NAME)
    customer_coins = [5, 1, 10]
    start_vending_machine(money_manager, drink_manager, customer_coins)


def test_start_vending_machine_2():
    """
    Validate the Vending Machine's full flow
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    money_manager = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE_NAME)
    drink_manager = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_JSON_FILE_NAME)
    customer_coins = [5, 1, 10, 10]
    start_vending_machine(money_manager, drink_manager, customer_coins)


def test_start_vending_machine_3():
    """
    Validate the Vending Machine's full flow
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    money_manager = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE_NAME)
    drink_manager = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_JSON_FILE_NAME)
    customer_coins = [5, 1, 10, 1, 2, 5, 5, 5, 10]
    start_vending_machine(money_manager, drink_manager, customer_coins)


def test_start_vending_machine_4():
    """
    Validate the Vending Machine's full flow
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    money_manager = MoneyManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE_NAME)
    drink_manager = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_JSON_FILE_NAME)
    customer_coins = [5, 1, 10, 10, 1, 1, 2, 5, 2, 1, 10, 5]
    start_vending_machine(money_manager, drink_manager, customer_coins)


def start_vending_machine(money_manager, drink_manager, customer_coins):

    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"

    for coin in customer_coins:
        money_manager.customer_money = money_manager.customer_money + coin

    drink_data_len = len(drink_manager.drink_data)
    drink_id = random.randint(1, drink_data_len)

    drink_data_dict = drink_manager.drink_data
    drink = drink_data_dict[drink_id]
    save_customer_money = money_manager.customer_money
    save_change_money = money_manager.change_money

    if money_manager.customer_money < drink.price:
        assert money_manager.customer_money < drink.price
    else:
        change = money_manager.customer_money - drink.price
        # update machine change
        money_manager.change_money = money_manager.change_money + drink.price
        # update drink quantity
        drink.quantity = drink.quantity - 1
        # reset cutomer_money to 0.
        money_manager.customer_money = 0
        # create a document (after update drink quantity) in format json from _drink_manager.get_drink_data()
        updated_drink_json = json.dumps([drinkobj.__dict__ for drinkobj in drink_manager.drink_data.values()])
        # save the up-to-date drink quantity to file
        drink_manager.record_object_data(updated_drink_json, dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_AFTER_BUY_JSON_FILE_NAME)
        # create a format json document from money_manager.
        updated_money_json = json.dumps([money_manager.__dict__])
        # save the new amount into file
        money_manager.record_money(updated_money_json, dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_AFTER_BUY_JSON_FILE_NAME)
        assert change == save_customer_money - drink.price
        assert money_manager.change_money == save_change_money + drink.price


