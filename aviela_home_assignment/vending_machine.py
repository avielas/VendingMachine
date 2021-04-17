from aviela_home_assignment.consts import Consts
from aviela_home_assignment.data_reader import DataReader


class VendingMachine:
    """
    VendingMachine class which run the main flow
    """
    def __init__(self, pm, mm, vmp):
        """
        @param pm: Product's Manager
        @type pm: ProductManager
        @param mm: Money's Manager
        @type mm: MoneyManager
        @param vmp: Vending Machine's Printer
        @type vmp: VendingMachinePrinter
        """
        self.__ProductManager = pm
        self.__MoneyManager = mm
        self.__VendingMachinePrinter = vmp
        self.__sChosenProductsType = Consts.ALL
        self.__specificProductsType = False
        self.__DataReader = DataReader()

    def StartVendingMachine(self):
        """
        Run the main flow of the Vending Machine
        """
        # Open infinity loop which can stop by ctrl+c
        while True:
            self.__CollectCoinsFromUser()
            Product = self.__GetProductSelectionFromUser()
            if not self.__MoneyManager.VmHaveEnoughChange(Product.iPrice):
                self.__VendingMachinePrinter.NotEnoughChange()
                continue
            else:
                break
        self.__HandlePurchase(Product)

    def __CollectCoinsFromUser(self):
        """
        Collect coin from user and print error in case of invalid coin
        """
        while True:
            self.__VendingMachinePrinter.WelcomeToVM()
            AvailableProducts = self.__ProductManager.GetAvailableProducts()
            FilteredProducts = self.__DataReader.FilterData(AvailableProducts, self.__sChosenProductsType, self.__specificProductsType)
            self.__VendingMachinePrinter.InitialMessage(FilteredProducts, self.__MoneyManager.iCustomerMoney, self.__sChosenProductsType)
            # Get input from customer
            sCoins = ', '.join(self.__MoneyManager.dVmCoins)
            sUserInput = str(input("Please insert coin " + sCoins + " " + str(Consts.CURRENCY_TYPE) + ". To place order, press 0: "))
            # If you drop valid coin, add the money that has been added continuously with customer_money
            if sUserInput in self.__MoneyManager.dVmCoins:
                self.__MoneyManager.AddToCustomerCoins(sUserInput)
            elif sUserInput == 'a':
                self.__sChosenProductsType = Consts.ALL
            elif sUserInput == 'd':
                self.__specificProductsType = False
                self.__sChosenProductsType = Consts.DRINK
            elif sUserInput == 's':
                self.__specificProductsType = False
                self.__sChosenProductsType = Consts.SNACK
            elif sUserInput == 'sd':
                self.__specificProductsType = True
                self.__sChosenProductsType = Consts.DRINK
            elif sUserInput == 'ss':
                self.__specificProductsType = True
                self.__sChosenProductsType = Consts.SNACK
            # If you click to select the product
            elif sUserInput == '0':
                break
            else:
                self.__VendingMachinePrinter.InvalidCoin()

    def __GetProductSelectionFromUser(self):
        """
        Get the selected product from user and print error in case of invalid product ID
        @return: Selected product by user
        @rtype: Product
        """
        while True:
            AvailableProducts = self.__ProductManager.GetAvailableProducts()
            FilteredProducts = self.__DataReader.FilterData(AvailableProducts, self.__sChosenProductsType, self.__specificProductsType)
            self.__VendingMachinePrinter.InitialMessage(FilteredProducts, self.__MoneyManager.iCustomerMoney, self.__sChosenProductsType)
            print(f"If you want to insert more coins, press 'i'.")
            sUserInput = str(input("Please give the id of the product you want: "))
            if sUserInput == 'a':
                self.__sChosenProductsType = Consts.ALL
            elif sUserInput == 'd':
                self.__specificProductsType = False
                self.__sChosenProductsType = Consts.DRINK
            elif sUserInput == 's':
                self.__specificProductsType = False
                self.__sChosenProductsType = Consts.SNACK
            elif sUserInput == 'sd':
                self.__specificProductsType = True
                self.__sChosenProductsType = Consts.DRINK
            elif sUserInput == 'ss':
                self.__specificProductsType = True
                self.__sChosenProductsType = Consts.SNACK
            elif sUserInput == 'i':
                self.__CollectCoinsFromUser()
            else:
                try:
                    iProductId = int(sUserInput)
                    FilteredProducts = self.__DataReader.FilterData(AvailableProducts, self.__sChosenProductsType, self.__specificProductsType)
                    if iProductId in FilteredProducts:
                        Product = FilteredProducts[iProductId]
                        if not self.__MoneyManager.CustomerHaveEnoughMoney(Product.iPrice):
                            self.__VendingMachinePrinter.NotEnoughMoney(Product.iPrice, self.__MoneyManager.iCustomerMoney)
                            continue
                        return Product
                    else:
                        self.__VendingMachinePrinter.InvalidProductUId()
                        continue
                except ValueError:
                    self.__VendingMachinePrinter.InvalidProductUId()
                    continue

    def __HandlePurchase(self, product):
        """
        Get the selected product and handle the purchase
        @param product: Selected product by user
        @type product: Product
        """
        self.__ProductManager.UpdateQuantity(product.iUid)
        if product.iQuantity == 0:
            self.__ProductManager.RemoveProduct(product.iUid)
        sProductJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.PRODUCT_DATA_DUMP_JSON_FILE
        self.__ProductManager.DumpProducts(sProductJsonFilePath)
        # save the new amount into file
        mMoneyDumpJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.MONEY_DATA_DUMP_JSON_FILE
        mCoinsDumpJsonFilePath = Consts.JSON_DIR_PATH_PROGRAM + Consts.COINS_DATA_DUMP_JSON_FILE
        self.__MoneyManager.DumpMoney(mMoneyDumpJsonFilePath, mCoinsDumpJsonFilePath)

        self.__VendingMachinePrinter.ChangeMoney(self.__MoneyManager.iCustomerChangeMoney, self.__MoneyManager.dCostumerChangeCoins)
        self.__VendingMachinePrinter.ProductPayment(product.sName)
