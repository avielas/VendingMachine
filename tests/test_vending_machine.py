"""Tests the DrinkManager class."""
from aviela_home_assignment.money_manager import MoneyManager
from aviela_home_assignment.drink_manager import DrinkManager
from aviela_home_assignment.sweet_manager import SweetManager
from aviela_home_assignment.vending_machine import VendingMachine
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.sweet import Sweet
import random
import os


def test_dump_products_data_drink():
    """
    Asserts the drink values which dumped by DumpProducts
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    DM = DrinkManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    SM = SweetManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    MM = MoneyManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE)
    VM = VendingMachine(SM, DM, MM)
    drink = DM.dProducts[1]
    CurrDrinkQuantity = drink.iQuantity
    DM.UpdateQuantity(drink.iUid)
    sProductJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    sDrinkJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    sSweetJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.SWEET_DATA_DUMP_JSON_FILE
    VM.DumpProducts(sProductJsonFilePath, sDrinkJsonFilePath, sSweetJsonFilePath)
    # create another DrinkManager from stored file and assert the value
    DrinkManagerAfter = DrinkManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE)
    DrinkDataAfter = DrinkManagerAfter.dProducts
    DrinkAfter = DrinkDataAfter[1]
    AfterDrinkQuantity = DrinkAfter.iQuantity

    assert CurrDrinkQuantity - 1 == AfterDrinkQuantity


def test_dump_products_data_sweet():
    """
    Asserts the sweet value which dumped by DumpProducts
    """
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    DM = DrinkManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    SM = SweetManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    MM = MoneyManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE)
    VM = VendingMachine(SM, DM, MM)
    sweet = SM.dProducts[6]
    CurrSweetQuantity = sweet.iQuantity
    SM.UpdateQuantity(sweet.iUid)
    sProductJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    sDrinkJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    sSweetJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.SWEET_DATA_DUMP_JSON_FILE
    VM.DumpProducts(sProductJsonFilePath, sDrinkJsonFilePath, sSweetJsonFilePath)
    # create another SweetManager from stored file and assert the value
    SweetManagerAfter = SweetManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE)
    SweetDataAfter = SweetManagerAfter.dProducts
    SweetAfter = SweetDataAfter[6]
    AfterSweetQuantity = SweetAfter.iQuantity

    assert CurrSweetQuantity - 1 == AfterSweetQuantity


def test_start_vending_machine_1():
    """
    Validate the Vending Machine's full flow
    """
    CustomerCoins = [5, 1, 10]
    start_vending_machine(CustomerCoins)


def test_start_vending_machine_2():
    """
    Validate the Vending Machine's full flow
    """
    CustomerCoins = [5, 1, 10, 10]
    start_vending_machine(CustomerCoins)


def test_start_vending_machine_3():
    """
    Validate the Vending Machine's full flow
    """
    CustomerCoins = [5, 1, 10, 1, 2, 5, 5, 5, 10]
    start_vending_machine(CustomerCoins)


def test_start_vending_machine_4():
    """
    Validate the Vending Machine's full flow
    """
    CustomerCoins = [5, 1, 10, 10, 1, 1, 2, 5, 2, 1, 10, 5]
    start_vending_machine(CustomerCoins)


def start_vending_machine(CustomerCoins):
    DirPath = os.path.dirname(os.path.dirname(__file__)) + "\\"
    MM = MoneyManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_JSON_FILE)
    DM = DrinkManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    SM = SweetManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    VM = VendingMachine(SM, DM, MM)

    # __CollectCoinsFromUser
    for Coin in CustomerCoins:
        MM.AddToCustomerMoney(Coin)

    # random __GetProductSelectionFromUser
    Product = get_product_selection_from_user(DM, SM)
    SaveCustomerMoney = MM.iCustomerMoney
    SaveChangeMoney = MM.iVmChangeMoney

    if not MM.CustomerHaveEnoughMoney(Product):
        assert MM.iCustomerMoney < Product.iPrice

    # __HandlePurchase
    handle_purchase(DirPath, MM, SM, DM, VM, Product)

    assert MM.iCustomerChangeMoney == SaveCustomerMoney - Product.iPrice
    assert MM.iVmChangeMoney == SaveChangeMoney + Product.iPrice


def handle_purchase(DirPath, MM, SM, DM, VM, Product):
    MM.AddToCustomerChangeMoney(Product.iPrice)
    MM.AddToVmChangeMoney(Product.iPrice)
    # update product quantity
    if isinstance(Product, Sweet):
        SM.UpdateQuantity(Product.iUid)
    elif isinstance(Product, Drink):
        DM.UpdateQuantity(Product.iUid)
    # reset customer money to 0.
    MM.AddToCustomerMoney(-1 * MM.iCustomerMoney)
    sProductJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    sDrinkJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.DRINK_DATA_DUMP_JSON_FILE
    sSweetJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.SWEET_DATA_DUMP_JSON_FILE
    VM.DumpProducts(sProductJsonFilePath, sDrinkJsonFilePath, sSweetJsonFilePath)
    # save the new amount into file
    mMoneyDumpJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_DUMP_JSON_FILE
    MM.DumpMoney(mMoneyDumpJsonFilePath)


def get_product_selection_from_user(DM, SM):
    dProducts = DM.dProducts
    dProducts.update(SM.dProducts)
    ProductDataLen = len(dProducts)
    ProductId = random.randint(1, ProductDataLen)
    Product = dProducts[ProductId]
    return Product
