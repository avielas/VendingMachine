from aviela_home_assignment.consts import Consts


class VendingMachinePrinter:
    """
    VendingMachinePrinter class which responsible to print VM messages
    """

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
        print("\nYou can choose one of the following products:")
        lProducts = self.__Dict2PrintList(Products)
        print(lProducts)
        print(f"For now, your deposit money is {iCustomerMoney} " + str(Consts.CURRENCY_TYPE) + ".")
        print(f"For see just sweets press 's', for drinks 'd' and for all 'a'.")

    def ProductPayment(self, sProductName: str):
        print(f"Payment for {sProductName} is done.")

    def ChangeMoney(self, iChangeMoney: int, dCostumerChangeCoins: dict):
        print(f"\nChange money is {iChangeMoney} " + Consts.CURRENCY_TYPE + " ( Coins: " + str(dCostumerChangeCoins) + " ).")

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
                sAvailableProductWithPrice = "{} {} {} {} {} {}".format(Product.iUid, ":", Product.sName, "price", Product.iPrice, Consts.CURRENCY_TYPE)
                lAvailableProducts.append(sAvailableProductWithPrice)
        return lAvailableProducts

