"""Tests the SweetManager class."""
from aviela_home_assignment.sweet_manager import SweetManager
import os
from aviela_home_assignment.consts import Consts


def test_get_available_products():
    """
    Validate the get_available_products function which returned just products with quantity 0
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    sweet_manager = SweetManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    sweet_6 = sweet_manager.pProducts[6]
    sweet_7 = sweet_manager.pProducts[7]

    sweet_manager.update_quantity(sweet_6.iUid)

    sweet_manager.update_quantity(sweet_7.iUid)
    sweet_manager.update_quantity(sweet_7.iUid)
    sweet_manager.update_quantity(sweet_7.iUid)
    sweet_manager.update_quantity(sweet_7.iUid)
    sweet_manager.update_quantity(sweet_7.iUid)
    sweet_manager.update_quantity(sweet_7.iUid)

    count_available = len(sweet_manager.pProducts) - 2
    count_available_after = sweet_manager.get_available_products()

    assert count_available == len(count_available_after)


def test_dump_products():
    """
    Asserts the value which stored previously by record_object_data function
    """
    dir_path = os.path.dirname(os.path.dirname(__file__)) + "\\"
    sweet_manager = SweetManager(dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)

    sweet = sweet_manager.pProducts[6]
    curr_sweet_quantity = sweet.iQuantity
    sweet_manager.update_quantity(sweet.iUid)
    # save the up-to-date sweet quantity to file
    sSweetJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.SWEET_DATA_DUMP_JSON_FILE
    sweet_manager.dump_products(sSweetJsonFilePath)

    # create another SweetManager from stored file and assert the value
    sSweetDumpJsonFilePath = dir_path + Consts.JSON_DIR_PATH_TESTS + Consts.SWEET_DATA_DUMP_JSON_FILE
    sweet_manager_after = SweetManager(sSweetDumpJsonFilePath)
    sweet_data_after = sweet_manager_after.pProducts
    sweet_after = sweet_data_after[6]
    after_sweet_quantity = sweet_after.iQuantity

    assert curr_sweet_quantity - 1 == after_sweet_quantity