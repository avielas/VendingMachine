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
    drink_manager = DrinkManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    drink_1 = drink_manager.dDrinks[1]
    drink_3 = drink_manager.dDrinks[3]
    drink_1.iQuantity = 0
    drink_3.iQuantity = 0
    count_available = len(drink_manager.dDrinks) - 2
    count_available_after = drink_manager.get_available_products()

    assert count_available == len(count_available_after)
