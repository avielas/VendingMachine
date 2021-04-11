import json
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.sweet import Sweet


class VendingMachine:
    """
    VendingMachine class which run the main flow
    """
    def __init__(self, sm, dm, mm):
        self._smSweetManager = sm
        self._dmDrinkManager = dm
        self._mmMoneyManager = mm

    def start_vending_machine(self):
        sProductsType = Consts.ALL
        # Open infinity loop which can stop by ctrl+c
        while True:
            print("\n --- Vending machine --- ")
            self.print_initial_message(sProductsType)
            # Get input from customer
            sCoins = ', '.join(Consts.COINS_LIST)
            sUserInput = str(input("Please insert coin " + sCoins + " " + str(Consts.CURRENCY_TYPE) + ". To place order, press 0: "))
            # If you drop valid coin, add the money that has been added continuously with customer_money
            if sUserInput in Consts.COINS_LIST:
                self._mmMoneyManager.iCustomerMoney = self._mmMoneyManager.iCustomerMoney + int(sUserInput)
            elif sUserInput == 'a':
                sProductsType = Consts.ALL
            elif sUserInput == 'd':
                sProductsType = Consts.DRINKS
            elif sUserInput == 's':
                sProductsType = Consts.SWEETS
            # If you click to select the product
            elif sUserInput == '0':
                while True:
                    self.print_initial_message(sProductsType)
                    # Keep what the customer choose to drink
                    try:
                        iProductId = int(input("Please give the id of the product you want: "))
                    except ValueError:
                        self.print_invalid_product_id_error_mesaage()
                        continue
                    pProducts = self.get_products_by_type(sProductsType)
                    if iProductId in pProducts:
                        pProduct = pProducts[iProductId]
                        break
                    else:
                        self.print_invalid_product_id_error_mesaage()
                        continue
                if self._mmMoneyManager.iCustomerMoney < pProduct.iPrice:
                    self.print_not_enough_money_to_buy_product_error_message(pProduct)
                    continue
                else:
                    iChange = self._mmMoneyManager.iCustomerMoney - pProduct.iPrice
                    # update machine change
                    self._mmMoneyManager.iChangeMoney = self._mmMoneyManager.iChangeMoney + pProduct.iPrice
                    self.update_quantity(pProducts, iProductId)
                    if pProduct.iQuantity == 0:
                        self.remove_product(pProducts, iProductId)
                    self._mmMoneyManager.iCustomerMoney = 0
                    sProductJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.PRODUCT_DATA_DUMP_JSON_FILE
                    sDrinkJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.DRINK_DATA_DUMP_JSON_FILE
                    sSweetJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.SWEET_DATA_DUMP_JSON_FILE
                    self.dump_products(sProductJsonFilePath, sDrinkJsonFilePath, sSweetJsonFilePath)
                    # save the new amount into file
                    mMoneyDumpJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.MONEY_DATA_DUMP_JSON_FILE
                    self._mmMoneyManager.dump_money(mMoneyDumpJsonFilePath)
                    self.print_change_money(iChange)
                    self.print_product_payment(pProduct.sName)
                break
            else:
                self.print_invalid_coin_error_message()

    def dump_products(self, sProductJsonFilePath, sDrinkJsonFilePath, sSweetJsonFilePath):
        self._dmDrinkManager.dump_products(sDrinkJsonFilePath)
        self._smSweetManager.dump_products(sSweetJsonFilePath)
        pProducts = self._dmDrinkManager.pProducts.copy()
        pProducts.update(self._smSweetManager.pProducts)
        # create a document (after update product quantity) in json format
        values = pProducts.values()
        pProductJsonToDump = json.dumps([productObj.__dict__ for productObj in values])
        # save the up-to-date product quantity to file
        with open(sProductJsonFilePath, "w") as IOFile:
            IOFile.write(pProductJsonToDump)

    def get_products_by_type(self, sProductsType):
        if sProductsType == Consts.ALL:
            # make a copy for not change the source dict
            pProducts = self._dmDrinkManager.pProducts.copy()
            pProducts.update(self._smSweetManager.pProducts)
            return pProducts
        elif sProductsType == Consts.SWEETS:
            return self._smSweetManager.pProducts
        elif sProductsType == Consts.DRINKS:
            return self._dmDrinkManager.pProducts

    def print_invalid_coin_error_message(self):
        print("\n*********************************************************************")
        print("********* You inserted invalid coin. please insert again ! **********")
        print("*********************************************************************")

    def print_not_enough_money_to_buy_product_error_message(self, dDrink):
        print("\n************************************************************************************************************")
        print("***** The money that drops(" + str(self._mmMoneyManager.iCustomerMoney) + ") is less than the price(" + str(
            dDrink.iPrice) + ") of the product, please insert more money !!! *****")
        print("************************************************************************************************************\n")

    def print_invalid_product_id_error_mesaage(self):
        print("\n**************************************************************************************************************")
        print("************************************** invalid product id. please try again! ***********************************")
        print("**************************************************************************************************************\n")

    def print_initial_message(self, sProductsType):
        print("\nYou can choose one of the following products:")
        if sProductsType == Consts.ALL:
            print(self._dmDrinkManager.get_available_products() + self._smSweetManager.get_available_products())
        elif sProductsType == Consts.SWEETS:
            print(self._smSweetManager.get_available_products())
        elif sProductsType == Consts.DRINKS:
            print(self._dmDrinkManager.get_available_products())
        print(f"For now, your deposit money is {self._mmMoneyManager.iCustomerMoney} " + str(Consts.CURRENCY_TYPE) + ".")
        print(f"For see just sweets press 's', for drinks 'd' and for all 'a'.")

    def print_product_payment(self, sDrinkName):
        print(f"Payment for {sDrinkName} is done.")

    def print_change_money(self, iChangeMoney):
        print(f"Change money is {iChangeMoney} " + Consts.CURRENCY_TYPE + ".")

    def remove_product(self, pProducts, iProductId):
        pProduct = pProducts[iProductId]
        if isinstance(pProduct, Sweet):
            self._smSweetManager.remove_product(iProductId)
        elif isinstance(pProduct, Drink):
            self._dmDrinkManager.remove_product(iProductId)

    def update_quantity(self, pProducts, iProductId):
        pProduct = pProducts[iProductId]
        if isinstance(pProduct, Sweet):
            self._smSweetManager.update_quantity(iProductId)
        elif isinstance(pProduct, Drink):
            self._dmDrinkManager.update_quantity(iProductId)
