from aviela_home_assignment.consts import Consts
from aviela_home_assignment.data_reader import DataReader


class VendingMachine:
    """
    VendingMachine class which run the main flow
    """
    def __init__(self, pm, mm, vmp):
        self.__ProductManager = pm
        self.__MoneyManager = mm
        self.__VendingMachinePrinter = vmp
        self.__sChosenProductsType = Consts.ALL
        self.__DataReader = DataReader()

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
            AvailableProducts = self.__ProductManager.GetAvailableProducts()
            FilteredProducts = self.__DataReader.FilterData(AvailableProducts, self.__sChosenProductsType)
            self.__VendingMachinePrinter.InitialMessage(FilteredProducts, self.__MoneyManager.iCustomerMoney)
            # Get input from customer
            sCoins = ', '.join(Consts.COINS_LIST)
            sUserInput = str(input("Please insert coin " + sCoins + " " + str(Consts.CURRENCY_TYPE) + ". To place order, press 0: "))
            # If you drop valid coin, add the money that has been added continuously with customer_money
            if sUserInput in Consts.COINS_LIST:
                self.__MoneyManager.AddToCustomerMoney(int(sUserInput))
            elif sUserInput == 'a':
                self.__sChosenProductsType = Consts.ALL
            elif sUserInput == 'd':
                self.__sChosenProductsType = Consts.DRINK
            elif sUserInput == 's':
                self.__sChosenProductsType = Consts.SWEET
            # If you click to select the product
            elif sUserInput == '0':
                break
            else:
                self.__VendingMachinePrinter.InvalidCoin()

    def __GetProductSelectionFromUser(self):
        while True:
            AvailableProducts = self.__ProductManager.GetAvailableProducts()
            FilteredProducts = self.__DataReader.FilterData(AvailableProducts, self.__sChosenProductsType)
            self.__VendingMachinePrinter.InitialMessage(FilteredProducts, self.__MoneyManager.iCustomerMoney)
            print(f"If you want to insert more coins, press 'i'.")
            sUserInput = str(input("Please give the id of the product you want: "))
            if sUserInput == 'a':
                self.__sChosenProductsType = Consts.ALL
            elif sUserInput == 'd':
                self.__sChosenProductsType = Consts.DRINK
            elif sUserInput == 's':
                self.__sChosenProductsType = Consts.SWEET
            elif sUserInput == 'i':
                self.__CollectCoinsFromUser()
            else:
                try:
                    iProductId = int(sUserInput)
                    FilteredProducts = self.__DataReader.FilterData(AvailableProducts, self.__sChosenProductsType)
                    if iProductId in FilteredProducts:
                        Product = FilteredProducts[iProductId]
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
        self.__ProductManager.UpdateQuantity(Product.iUid)
        if Product.iQuantity == 0:
            self.__ProductManager.RemoveProduct(Product)
        # reset customer money to zero
        self.__MoneyManager.AddToCustomerMoney(-1 * self.__MoneyManager.iCustomerMoney)
        sProductJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.PRODUCT_DATA_DUMP_JSON_FILE
        self.__ProductManager.DumpProducts(sProductJsonFilePath)
        # save the new amount into file
        sMoneyDumpJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.MONEY_DATA_DUMP_JSON_FILE
        self.__MoneyManager.DumpMoney(sMoneyDumpJsonFilePath)
        self.__VendingMachinePrinter.ChangeMoney(self.__MoneyManager.iCustomerChangeMoney)
        self.__VendingMachinePrinter.ProductPayment(Product.sName)

    def __VmHaveEnoughChange(self, Product):
        self.__MoneyManager.AddToCustomerChangeMoney(Product.iPrice)
        self.__MoneyManager.AddToVmChangeMoney(Product.iPrice)
        if not self.__MoneyManager.HaveEnoughChange():
            self.__VendingMachinePrinter.NotEnoughChange()
            self.__MoneyManager.AddToCustomerChangeMoney(-1 * Product.iPrice)
            self.__MoneyManager.AddToVmChangeMoney(-1 * Product.iPrice)
            return False
        return True
