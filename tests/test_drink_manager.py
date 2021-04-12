"""Tests the DrinkManager class."""
from aviela_home_assignment.drink_manager import DrinkManager
import os
from aviela_home_assignment.consts import Consts


def test_get_available_products():
    """
    Validate the GetAvailableProducts function which returned just products with quantity 0
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    DM = DrinkManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    Drink_1 = DM.dProducts[1]
    Drink_3 = DM.dProducts[3]

    DM.UpdateQuantity(Drink_1.iUid)
    DM.UpdateQuantity(Drink_1.iUid)
    DM.UpdateQuantity(Drink_1.iUid)
    DM.UpdateQuantity(Drink_1.iUid)
    DM.UpdateQuantity(Drink_1.iUid)

    DM.UpdateQuantity(Drink_3.iUid)
    DM.UpdateQuantity(Drink_3.iUid)

    CountAvailable = len(DM.dProducts) - 2
    CountAvailableAfter = DM.GetAvailableProducts()

    assert CountAvailable == len(CountAvailableAfter)


def test_dump_products():
    """
    Asserts the value which stored previously by DumpProducts function
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    DM = DrinkManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)

    Drink = DM.dProducts[1]
    CurrDrinkQuantity = Drink.iQuantity
    DM.UpdateQuantity(Drink.iUid)
    # save the up-to-date drink quantity to file
    sDrinkJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    DM.DumpProducts(sDrinkJsonFilePath)

    # create another DrinkManager from stored file and assert the value
    sDrinkDumpJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    DrinkManagerAfter = DrinkManager(sDrinkDumpJsonFilePath)
    DrinkDataAfter = DrinkManagerAfter.dProducts
    DrinkAfter = DrinkDataAfter[1]
    AfterDrinkQuantity = DrinkAfter.iQuantity

    assert CurrDrinkQuantity - 1 == AfterDrinkQuantity
