"""Tests the VendingMachineManager class."""
from aviela_home_assignment.product_manager import ProductManager
from aviela_home_assignment.money_manager import MoneyManager
from aviela_home_assignment.vending_machine import VendingMachine
from aviela_home_assignment.vending_machine_printer import VendingMachinePrinter
from aviela_home_assignment.consts import Consts
import random
import os


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
    PM = ProductManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)
    VMP = VendingMachinePrinter()
    VM = VendingMachine(PM, MM, VMP)

    # __CollectCoinsFromUser
    for Coin in CustomerCoins:
        MM.AddToCustomerMoney(Coin)

    # random __GetProductSelectionFromUser
    Product = get_product_selection_from_user(PM)
    SaveCustomerMoney = MM.iCustomerMoney
    SaveChangeMoney = MM.iVmChangeMoney

    if not MM.CustomerHaveEnoughMoney(Product):
        assert MM.iCustomerMoney < Product.iPrice

    # __HandlePurchase
    handle_purchase(DirPath, MM, PM, Product)

    assert MM.iCustomerChangeMoney == SaveCustomerMoney - Product.iPrice
    assert MM.iVmChangeMoney == SaveChangeMoney + Product.iPrice


def handle_purchase(DirPath, MM, PM, Product):
    MM.AddToCustomerChangeMoney(Product.iPrice)
    MM.AddToVmChangeMoney(Product.iPrice)
    PM.UpdateQuantity(Product.iUid)
    sProductJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    PM.DumpProducts(sProductJsonFilePath)
    # save the new amount into file
    mMoneyDumpJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.MONEY_DATA_DUMP_JSON_FILE
    MM.DumpMoney(mMoneyDumpJsonFilePath)

    assert MM.iCustomerChangeMoney == MM.iCustomerMoney - Product.iPrice


def get_product_selection_from_user(PM):
    ProductDataLen = len(PM.dProducts)
    ProductId = random.randint(1, ProductDataLen)
    Product = PM.dProducts[ProductId]
    return Product
