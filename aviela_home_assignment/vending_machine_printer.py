from aviela_home_assignment.consts import Consts


class VendingMachinePrinter:
    """
    VendingMachinePrinter class which responsible to print VM messages
    """
    def WelcomeToVM(self):
        print("\n\n *********************************************")
        print("     WELCOME TO THE VENDING MACHINE           ")
        print(" *********************************************")

    def InvalidCoin(self):
        print("\n*********************************************************************")
        print("********* You inserted invalid coin. please insert again ! **********")
        print("*********************************************************************")

    def NotEnoughMoney(self, iPrice: int, iCustomerMoney: int):
        print("\n************************************************************************************************************")
        print("***** The money that drops(" + str(iCustomerMoney) + ") is less than the price(" + str(
            iPrice) + ") of the product, please insert more money !!! *****")
        print("************************************************************************************************************\n")

    def NotEnoughChange(self):
        print("\n************************************************************************************************************")
        print("******************************* The Vending Machine don't have enough change *********************************")
        print("************************************************************************************************************\n")

    def InvalidProductUId(self):
        print("\n**************************************************************************************************************")
        print("************************************** invalid product id. please try again! ***********************************")
        print("**************************************************************************************************************\n")

    def InitialMessage(self, Products: dict, iCustomerMoney: int):
        print("\nAvailable products:\n")
        lProducts = self.__Dict2PrintList(Products)
        for product in lProducts:
            print("   " + product)
        print(f"\nYour deposited money is {iCustomerMoney} " + str(Consts.CURRENCY_TYPE) + ".")
        print(f"For see just sweets press 's', drinks 'd' and all 'a'.")

    def ProductPayment(self, sProductName: str):
        print(f"\nPayment for {sProductName} is done.")

    def ChangeMoney(self, iChangeMoney: int, dCostumerChangeCoins: dict):
        lChangeCoinsToPrint = []
        for k, v in dCostumerChangeCoins.items():
            line = "{} {}, coins: {}".format(k, Consts.CURRENCY_TYPE, str(v))
            lChangeCoinsToPrint.append(line)
        toPrint = "\nYour change is: {} {} ".format(iChangeMoney, Consts.CURRENCY_TYPE)
        print(toPrint)
        for coin in lChangeCoinsToPrint:
            print("   " + coin)
        # print(f"\nChange money is {iChangeMoney} " + Consts.CURRENCY_TYPE + " ( Coins: " + str(dCostumerChangeCoins) + " ).")

    def __Dict2PrintList(self, dProducts: dict) -> list:
        """
        Convert dictionary of products to print List
        @param dProducts: Dictionary of products
        @type dProducts: Dictionary
        @return: List od products to print
        @rtype: List
        """
        lAvailableProducts = []
        for Product in dProducts.values():
            if Product.iQuantity > 0:
                sAvailableProductWithPrice = "{} {} - {}: {} {}".format(Product.iUid, Product.sName, "Price", Product.iPrice, Consts.CURRENCY_TYPE)
                lAvailableProducts.append(sAvailableProductWithPrice)
        return lAvailableProducts

