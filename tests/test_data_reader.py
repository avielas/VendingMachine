"""Tests the DataReader class."""
from aviela_home_assignment.data_reader import DataReader
from aviela_home_assignment.product_manager import ProductManager
from aviela_home_assignment.consts import Consts
import os


def test_read_data_from_file():
    DirPath = os.path.dirname(os.path.dirname(__file__)) + Consts.SLASH
    DR = DataReader()
    sProductsJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE
    dProducts = DR.ReadProductsDataFromFile(sProductsJsonFilePath)
    ProductDataLen = len(dProducts)
    assert ProductDataLen == 7


def test_filter_data():
    DirPath = os.path.dirname(os.path.dirname(__file__)) + Consts.SLASH
    PM = ProductManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    DR = DataReader()
    AvailableProducts = PM.GetAvailableProducts()
    FilteredProducts = DR.FilterData(AvailableProducts, Consts.SNACK, False)
    ProductDataLen = len(FilteredProducts)
    assert ProductDataLen == 2
