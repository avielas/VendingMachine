"""Tests the ProductManager class."""
from aviela_home_assignment.product_manager import ProductManager
import os
from aviela_home_assignment.consts import Consts


def test_get_available_products():
    """
    Validate the GetAvailableProducts function which returned just products with quantity 0
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    PM = ProductManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    Product_1 = PM.dProducts[1]
    Product_3 = PM.dProducts[3]

    PM.UpdateQuantity(Product_1.iUid)
    PM.UpdateQuantity(Product_1.iUid)
    PM.UpdateQuantity(Product_1.iUid)
    PM.UpdateQuantity(Product_1.iUid)
    PM.UpdateQuantity(Product_1.iUid)

    PM.UpdateQuantity(Product_3.iUid)
    PM.UpdateQuantity(Product_3.iUid)

    CountAvailable = len(PM.dProducts) - 2
    CountAvailableAfter = PM.GetAvailableProducts()

    assert CountAvailable == len(CountAvailableAfter)


def test_update_quantity_and_dump_products():
    """
    Asserts the value which stored previously by DumpProducts function
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    PM = ProductManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)

    Product = PM.dProducts[1]
    CurrProductQuantity = Product.iQuantity
    PM.UpdateQuantity(Product.iUid)
    # save the up-to-date product quantity to file
    sProductJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    PM.DumpProducts(sProductJsonFilePath)

    # create another ProductManager from stored file and assert the value
    sProductDumpJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    ProductManagerAfter = ProductManager(sProductDumpJsonFilePath)
    ProductDataAfter = ProductManagerAfter.dProducts
    ProductAfter = ProductDataAfter[1]
    AfterProductQuantity = ProductAfter.iQuantity

    assert CurrProductQuantity - 1 == AfterProductQuantity


def test_remove_and_dump_product():
    """
    Asserts the length of dProducts after remove product
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    PM = ProductManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)

    # get snickers with quantity=1
    Product = PM.dProducts[6]
    CurrDProductsLen = len(PM.dProducts)
    PM.UpdateQuantity(Product.iUid)
    # save the up-to-date product quantity to file
    if Product.iQuantity == 0:
        PM.RemoveProduct(Product)
    sProductJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    PM.DumpProducts(sProductJsonFilePath)

    # create another ProductManager from stored file and assert the value
    sProductDumpJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    PMAfter = ProductManager(sProductDumpJsonFilePath)
    AfterDProductsLen = len(PMAfter.dProducts)

    assert CurrDProductsLen - 1 == AfterDProductsLen