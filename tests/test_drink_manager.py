"""Tests the DrinkManager class."""
from aviela_home_assignment.drink_manager import DrinkManager
import os
from aviela_home_assignment.consts import Consts


def test_get_available_products():
    """
    Validate the get_available_products function which returned just products with quantity 0
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    dm = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    drink_1 = dm.pProducts[1]
    drink_3 = dm.pProducts[3]

    dm.update_quantity(drink_1.iUid)
    dm.update_quantity(drink_1.iUid)
    dm.update_quantity(drink_1.iUid)
    dm.update_quantity(drink_1.iUid)
    dm.update_quantity(drink_1.iUid)

    dm.update_quantity(drink_3.iUid)
    dm.update_quantity(drink_3.iUid)

    count_available = len(dm.pProducts) - 2
    count_available_after = dm.get_available_products()

    assert count_available == len(count_available_after)


def test_dump_products():
    """
    Asserts the value which stored previously by record_object_data function
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    dm = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)

    drink = dm.pProducts[1]
    curr_drink_quantity = drink.iQuantity
    dm.update_quantity(drink.iUid)
    # save the up-to-date drink quantity to file
    sDrinkJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    dm.dump_products(sDrinkJsonFilePath)

    # create another DrinkManager from stored file and assert the value
    sDrinkDumpJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    drink_manager_after = DrinkManager(sDrinkDumpJsonFilePath)
    drink_data_after = drink_manager_after.pProducts
    drink_after = drink_data_after[1]
    after_drink_quantity = drink_after.iQuantity

    assert curr_drink_quantity - 1 == after_drink_quantity
