"""Tests the DrinkManager class."""
from aviela_home_assignment.drink_manager import DrinkManager
import os
import json
from aviela_home_assignment.consts import Consts


def test_get_available_drink_data():
    """
    Validate the get_available_data function which returned just products with quantity 0
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    drink_manager = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_JSON_FILE_NAME)
    drink_1 = drink_manager.dDrinks[1]
    drink_3 = drink_manager.dDrinks[3]
    drink_1.iQuantity = 0
    drink_3.iQuantity = 0
    count_available = len(drink_manager.dDrinks) - 2
    count_available_after = drink_manager.get_available_products()

    assert count_available == len(count_available_after)


def test_record_drink():
    """
    Asserts the value which stored previously by record_object_data function
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    drink_manager = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_JSON_FILE_NAME)

    drink = drink_manager.dDrinks[1]
    curr_drink_quantity = drink.iQuantity
    # update drink quantity
    drink.iQuantity = drink.iQuantity - 1
    # create a document (after update drink quantity) in format json from _drink_manager.get_drink_data()
    updated_drink_json = json.dumps([drinkobj.__dict__ for drinkobj in drink_manager.dDrinks.values()])
    # save the up-to-date drink quantity to file
    drink_manager.record_object_data(updated_drink_json, dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_AFTER_BUY_JSON_FILE_NAME)

    # create another DrinkManager from stored file and assert the value
    drink_manager_after = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_AFTER_BUY_JSON_FILE_NAME)
    drink_data_after = drink_manager_after.dDrinks
    drink_after = drink_data_after[1]
    after_drink_quantity = drink_after.iQuantity

    assert curr_drink_quantity - 1 == after_drink_quantity
