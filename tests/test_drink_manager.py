"""Tests the DrinkManager class."""
from drink_manager import DrinkManager
import os
import json


def test_get_available_drink_data():
    """
    Validate the get_available_data function which returned just products with quantity 0
    """
    dir_path = os.path.dirname(os.path.dirname(__file__))
    drink_manager = DrinkManager(dir_path + "\\json\\DrinkData.json")
    drink_1 = drink_manager.drink_data[1]
    drink_3 = drink_manager.drink_data[3]
    drink_1.quantity = 0
    drink_3.quantity = 0
    count_available = len(drink_manager.drink_data) - 2
    count_available_after = drink_manager.get_available_data()

    assert count_available == len(count_available_after)


def test_record_drink():
    """
    Asserts the value which stored previously by record_object_data function
    """
    dir_path = os.path.dirname(os.path.dirname(__file__))
    drink_manager = DrinkManager(dir_path + "\\json\\DrinkData.json")

    drink = drink_manager.drink_data[1]
    curr_drink_quantity = drink.quantity
    # update drink quantity
    drink.quantity = drink.quantity - 1
    # create a document (after update drink quantity) in format json from _drink_manager.get_drink_data()
    updated_drink_json = json.dumps([drinkobj.__dict__ for drinkobj in drink_manager.drink_data.values()])
    # save the up-to-date drink quantity to file
    drink_manager.record_object_data(updated_drink_json, dir_path + "\\json\\DrinkDataAfterBuyDrink.json")

    # create another DrinkManager from stored file and assert the value
    drink_manager_after = DrinkManager(dir_path + "\\json\\DrinkDataAfterBuyDrink.json")
    drink_data_after = drink_manager_after.drink_data
    drink_after = drink_data_after[1]
    after_drink_quantity = drink_after.quantity

    assert curr_drink_quantity - 1 == after_drink_quantity
