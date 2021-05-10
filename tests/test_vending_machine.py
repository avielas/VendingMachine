"""Tests the VendingMachineManager class."""
from aviela_home_assignment.product_manager import ProductManager
from aviela_home_assignment.money_manager import MoneyManager
from aviela_home_assignment.calculator import Calculator
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
    DirPath = os.path.dirname(os.path.dirname(__file__)) + Consts.SLASH
    MM = MoneyManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.COINS_DATA_JSON_FILE)
    PM = ProductManager(DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_JSON_FILE)

    # __CollectCoinsFromUser
    for Coin in CustomerCoins:
        MM.AddToCustomerCoins(str(Coin))

    # random __GetProductSelectionFromUser
    Product = get_product_selection_from_user(PM)
    SaveCustomerMoney = MM.iCustomerMoney
    SaveChangeMoney = MM.iVmChangeMoney

    if not MM.CustomerHaveEnoughMoney(Product.iPrice):
        assert MM.iCustomerMoney < Product.iPrice

    # test also VmHaveEnoughChange function
    if not MM.VmHaveEnoughChange(Product.iPrice):
        calc = Calculator()
        # merge 2 dictionaries
        dCostumerCoins = dict([])
        for k, v in MM.dVmCoins.items():
            dCostumerCoins[k] = 0

        for coin in CustomerCoins:
            dCostumerCoins[str(coin)] = dCostumerCoins[str(coin)] + 1

        dTotalCoins = dCostumerCoins

        for k, v in MM.dVmCoins.items():
            dTotalCoins[k] += v

        iChange = MM.iCustomerMoney - Product.iPrice
        ChangeCoins = calc.CalculateMinimum(dTotalCoins.copy(), iChange)
        assert ChangeCoins is None
        return True

    # __HandlePurchase
    handle_purchase(DirPath, MM, PM, Product)

    assert MM.iCustomerChangeMoney == SaveCustomerMoney - Product.iPrice
    assert MM.iVmChangeMoney == SaveChangeMoney + Product.iPrice


def handle_purchase(DirPath, MM, PM, Product):
    PM.UpdateQuantity(Product.iUid)
    if Product.iQuantity == 0:
        PM.RemoveProduct(Product.iUid)
    sProductJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.PRODUCT_DATA_DUMP_JSON_FILE
    PM.DumpProducts(sProductJsonFilePath)
    # save the new amount into file
    mCoinsDumpJsonFilePath = DirPath + Consts.JSON_DIR_PATH_TESTS + Consts.COINS_DATA_DUMP_JSON_FILE
    MM.DumpMoney(mCoinsDumpJsonFilePath)


def get_product_selection_from_user(PM):
    ProductDataLen = len(PM.dProducts)
    ProductId = random.randint(1, ProductDataLen)
    Product = PM.dProducts[ProductId]
    return Product
