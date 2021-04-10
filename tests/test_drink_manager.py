"""Tests the DrinkManager class."""
from aviela_home_assignment.drink_manager import DrinkManager
import os
import json
from aviela_home_assignment.consts import Consts


def test_get_available_products():
    """
    Validate the get_available_products function which returned just products with quantity 0
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    drink_manager = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    drink_1 = drink_manager.pProducts[1]
    drink_3 = drink_manager.pProducts[3]
    drink_1.iQuantity = 0
    drink_3.iQuantity = 0
    count_available = len(drink_manager.pProducts) - 2
    count_available_after = drink_manager.get_available_products()

    assert count_available == len(count_available_after)


def test_dump_products():
    """
    Asserts the value which stored previously by record_object_data function
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    drink_manager = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)

    drink = drink_manager.pProducts[1]
    curr_drink_quantity = drink.iQuantity
    # update drink quantity
    drink.iQuantity = drink.iQuantity - 1
    # save the up-to-date drink quantity to file
    sDrinkJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    drink_manager.dump_products(sDrinkJsonFilePath)

    # create another DrinkManager from stored file and assert the value
    sDrinkDumpJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    drink_manager_after = DrinkManager(sDrinkDumpJsonFilePath)
    drink_data_after = drink_manager_after.pProducts
    drink_after = drink_data_after[1]
    after_drink_quantity = drink_after.iQuantity

    assert curr_drink_quantity - 1 == after_drink_quantity
