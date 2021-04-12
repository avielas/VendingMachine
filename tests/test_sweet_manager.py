"""Tests the SweetManager class."""
from aviela_home_assignment.sweet_manager import SweetManager
import os
from aviela_home_assignment.consts import Consts


def test_get_available_products():
    """
    Validate the GetAvailableProducts function which returned just products with quantity 0
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    SM = SweetManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    Sweet_6 = SM.dProducts[6]
    Sweet_7 = SM.dProducts[7]

    SM.UpdateQuantity(Sweet_6.iUid)

    SM.UpdateQuantity(Sweet_7.iUid)
    SM.UpdateQuantity(Sweet_7.iUid)
    SM.UpdateQuantity(Sweet_7.iUid)
    SM.UpdateQuantity(Sweet_7.iUid)
    SM.UpdateQuantity(Sweet_7.iUid)
    SM.UpdateQuantity(Sweet_7.iUid)

    CountAvailable = len(SM.dProducts) - 2
    CountAvailableAfter = SM.GetAvailableProducts()

    assert CountAvailable == len(CountAvailableAfter)


def test_dump_products():
    """
    Asserts the value which stored previously by DumpProducts function
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    SM = SweetManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)

    Sweet = SM.dProducts[6]
    CurrSweetQuantity = Sweet.iQuantity
    SM.UpdateQuantity(Sweet.iUid)
    # save the up-to-date sweet quantity to file
    sSweetJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.SWEET_DATA_DUMP_JSON_FILE
    SM.DumpProducts(sSweetJsonFilePath)

    # create another SweetManager from stored file and assert the value
    sSweetDumpJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.SWEET_DATA_DUMP_JSON_FILE
    SweetManagerAfter = SweetManager(sSweetDumpJsonFilePath)
    SweetDataAfter = SweetManagerAfter.dProducts
    SweetAfter = SweetDataAfter[6]
    AfterSweetQuantity = SweetAfter.iQuantity

    assert CurrSweetQuantity - 1 == AfterSweetQuantity
