import json
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.sweet import Sweet


class VendingMachine:
    """
    VendingMachine class which run the main flow
    """

    def __init__(self, sm, dm, mm, vmp):
        self.__SweetManager = sm
        self.__DrinkManager = dm
        self.__MoneyManager = mm
        self.__VendingMachinePrinter = vmp
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
            AvailableDrinks = self.__DrinkManager.GetAvailableProducts()
            AvailableDrinksToPrint = self.__VendingMachinePrinter.CreatePrintListFromDict(AvailableDrinks)
            AvailableSweets = self.__SweetManager.GetAvailableProducts()
            AvailableSweetsToPrint = self.__VendingMachinePrinter.CreatePrintListFromDict(AvailableSweets)
            self.__VendingMachinePrinter.InitialMessage(self.__sProductsType, AvailableDrinksToPrint, AvailableSweetsToPrint, self.__MoneyManager.iCustomerMoney)
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
                self.__VendingMachinePrinter.InvalidCoin()

    def __GetProductSelectionFromUser(self):
        while True:
            AvailableDrinks = self.__DrinkManager.GetAvailableProducts()
            AvailableDrinksToPrint = self.__VendingMachinePrinter.CreatePrintListFromDict(AvailableDrinks)
            AvailableSweets = self.__SweetManager.GetAvailableProducts()
            AvailableSweetsToPrint = self.__VendingMachinePrinter.CreatePrintListFromDict(AvailableSweets)
            self.__VendingMachinePrinter.InitialMessage(self.__sProductsType, AvailableDrinksToPrint, AvailableSweetsToPrint, self.__MoneyManager.iCustomerMoney)
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
                            self.__VendingMachinePrinter.NotEnoughMoney(Product.iPrice, self.__MoneyManager.iCustomerMoney)
                            continue
                        return Product
                    else:
                        self.__VendingMachinePrinter.InvalidProductUId()
                        continue
                except ValueError:
                    self.__VendingMachinePrinter.InvalidProductUId()
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
        self.__VendingMachinePrinter.ChangeMoney(self.__MoneyManager.iCustomerChangeMoney)
        self.__VendingMachinePrinter.ProductPayment(Product.sName)

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

    def __RemoveProduct(self, Product):
        if isinstance(Product, Sweet):
            self.__SweetManager.RemoveProduct(Product.iUid)
        elif isinstance(Product, Drink):
            self.__DrinkManager.RemoveProduct(Product.iUid)

    def __UpdateQuantity(self, Product):
        if isinstance(Product, Sweet):
            self.__SweetManager.UpdateQuantity(Product.iUid)
        elif isinstance(Product, Drink):
            self.__DrinkManager.UpdateQuantity(Product.iUid)

    def __VmHaveEnoughChange(self, Product):
        self.__MoneyManager.AddToCustomerChangeMoney(Product.iPrice)
        self.__MoneyManager.AddToVmChangeMoney(Product.iPrice)
        if not self.__MoneyManager.HaveEnoughChange():
            self.__VendingMachinePrinter.NotEnoughChange()
            self.__MoneyManager.AddToCustomerChangeMoney(-1 * Product.iPrice)
            self.__MoneyManager.AddToVmChangeMoney(-1 * Product.iPrice)
            return False
        return True
