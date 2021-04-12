import json
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.sweet import Sweet


class VendingMachine:
    """
    VendingMachine class which run the main flow
    """

    def __init__(self, sm, dm, mm):
        self.__SweetManager = sm
        self.__DrinkManager = dm
        self.__MoneyManager = mm
        self.__sProductsType = Consts.ALL

    def StartVendingMachine(self):
        # Open infinity loop which can stop by ctrl+c
        while True:
            self.__CollectCoinsFromUser()
            Product = self.__GetProductSelectionFromUser()
            if not self.__VmHaveEnoughChange(Product):
                continue
            else:
                break
        self.__HandlePurchase(Product)

    def __CollectCoinsFromUser(self):
        while True:
            print("\n --- Vending machine --- ")
            self.__PrintInitialMessage()
            # Get input from customer
            sCoins = ', '.join(Consts.COINS_LIST)
            sUserInput = str(input("Please insert coin " + sCoins + " " + str(Consts.CURRENCY_TYPE) + ". To place order, press 0: "))
            # If you drop valid coin, add the money that has been added continuously with customer_money
            if sUserInput in Consts.COINS_LIST:
                self.__MoneyManager.AddToCustomerMoney(int(sUserInput))
            elif sUserInput == 'a':
                self.__sProductsType = Consts.ALL
            elif sUserInput == 'd':
                self.__sProductsType = Consts.DRINKS
            elif sUserInput == 's':
                self.__sProductsType = Consts.SWEETS
            # If you click to select the product
            elif sUserInput == '0':
                break
            else:
                self.__PrintInvalidCoinErrorMessage()

    def __GetProductSelectionFromUser(self):
        while True:
            self.__PrintInitialMessage()
            print(f"If you want to insert more coins, press 'i'.")
            sUserInput = str(input("Please give the id of the product you want: "))
            if sUserInput == 'a':
                self.__sProductsType = Consts.ALL
            elif sUserInput == 'd':
                self.__sProductsType = Consts.DRINKS
            elif sUserInput == 's':
                self.__sProductsType = Consts.SWEETS
            elif sUserInput == 'i':
                self.__CollectCoinsFromUser()
            else:
                try:
                    iProductId = int(sUserInput)
                    dProducts = self.__GetProductsByType(self.__sProductsType)
                    if iProductId in dProducts:
                        Product = dProducts[iProductId]
                        if not self.__MoneyManager.CustomerHaveEnoughMoney(Product):
                            self.__PrintNotEnoughMoneyErrorMessage(Product)
                            continue
                        return Product
                    else:
                        self.__PrintInvalidProductIdErrorMesaage()
                        continue
                except ValueError:
                    self.__PrintInvalidProductIdErrorMesaage()
                    continue

    def __HandlePurchase(self, Product):
        self.__UpdateQuantity(Product)
        if Product.iQuantity == 0:
            self.__RemoveProduct(Product)
        # reset customer money to zero
        self.__MoneyManager.AddToCustomerMoney(-1 * self.__MoneyManager.iCustomerMoney)
        sProductJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.PRODUCT_DATA_DUMP_JSON_FILE
        sDrinkJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.DRINK_DATA_DUMP_JSON_FILE
        sSweetJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.SWEET_DATA_DUMP_JSON_FILE
        self.DumpProducts(sProductJsonFilePath, sDrinkJsonFilePath, sSweetJsonFilePath)
        # save the new amount into file
        sMoneyDumpJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.MONEY_DATA_DUMP_JSON_FILE
        self.__MoneyManager.DumpMoney(sMoneyDumpJsonFilePath)
        self.__PrintChangeMoney(self.__MoneyManager.iCustomerChangeMoney)
        self.__PrintProductPayment(Product.sName)

    def DumpProducts(self, sProductJsonFilePath, sDrinkJsonFilePath, sSweetJsonFilePath):
        self.__DrinkManager.DumpProducts(sDrinkJsonFilePath)
        self.__SweetManager.DumpProducts(sSweetJsonFilePath)
        dProducts = self.__DrinkManager.dProducts.copy()
        dProducts.update(self.__SweetManager.dProducts)
        # create a document (after update product quantity) in json format
        values = dProducts.values()
        sProductJsonToDump = json.dumps([productObj.__dict__ for productObj in values])
        # save the up-to-date product quantity to file
        with open(sProductJsonFilePath, "w") as IOFile:
            IOFile.write(sProductJsonToDump)

    def __GetProductsByType(self, sProductsType):
        if sProductsType == Consts.ALL:
            # make a copy for not change the source dict
            dProducts = self.__DrinkManager.dProducts.copy()
            dProducts.update(self.__SweetManager.dProducts)
            return dProducts
        elif sProductsType == Consts.SWEETS:
            return self.__SweetManager.dProducts
        elif sProductsType == Consts.DRINKS:
            return self.__DrinkManager.dProducts

    def __PrintInvalidCoinErrorMessage(self):
        print("\n*********************************************************************")
        print("********* You inserted invalid coin. please insert again ! **********")
        print("*********************************************************************")

    def __PrintNotEnoughMoneyErrorMessage(self, dDrink):
        print("\n************************************************************************************************************")
        print("***** The money that drops(" + str(self.__MoneyManager.iCustomerMoney) + ") is less than the price(" + str(
            dDrink.iPrice) + ") of the product, please insert more money !!! *****")
        print("************************************************************************************************************\n")

    def __PrintNotEnoughChangeErrorMessage(self):
        print("\n************************************************************************************************************")
        print("******************************* The Vending Machine don't have enough change *********************************")
        print("************************************************************************************************************\n")

    def __PrintInvalidProductIdErrorMesaage(self):
        print("\n**************************************************************************************************************")
        print("************************************** invalid product id. please try again! ***********************************")
        print("**************************************************************************************************************\n")

    def __PrintInitialMessage(self):
        print("\nYou can choose one of the following products:")
        if self.__sProductsType == Consts.ALL:
            print(self.__DrinkManager.GetAvailableProducts() + self.__SweetManager.GetAvailableProducts())
        elif self.__sProductsType == Consts.SWEETS:
            print(self.__SweetManager.GetAvailableProducts())
        elif self.__sProductsType == Consts.DRINKS:
            print(self.__DrinkManager.GetAvailableProducts())
        print(f"For now, your deposit money is {self.__MoneyManager.iCustomerMoney} " + str(Consts.CURRENCY_TYPE) + ".")
        print(f"For see just sweets press 's', for drinks 'd' and for all 'a'.")

    def __PrintProductPayment(self, sDrinkName):
        print(f"Payment for {sDrinkName} is done.")

    def __PrintChangeMoney(self, iChangeMoney):
        print(f"Change money is {iChangeMoney} " + Consts.CURRENCY_TYPE + ".")

    def __RemoveProduct(self, Product):
        if isinstance(Product, Sweet):
            self.__SweetManager.__RemoveProduct(Product.iUid)
        elif isinstance(Product, Drink):
            self.__DrinkManager.__RemoveProduct(Product.iUid)

    def __UpdateQuantity(self, Product):
        if isinstance(Product, Sweet):
            self.__SweetManager.UpdateQuantity(Product.iUid)
        elif isinstance(Product, Drink):
            self.__DrinkManager.UpdateQuantity(Product.iUid)

    def __VmHaveEnoughChange(self, Product):
        self.__MoneyManager.AddToCustomerChangeMoney(Product.iPrice)
        self.__MoneyManager.AddToVmChangeMoney(Product.iPrice)
        if not self.__MoneyManager.HaveEnoughChange():
            self.__PrintNotEnoughChangeErrorMessage()
            self.__MoneyManager.AddToCustomerChangeMoney(-1 * Product.iPrice)
            self.__MoneyManager.AddToVmChangeMoney(-1 * Product.iPrice)
            return False
        return True
