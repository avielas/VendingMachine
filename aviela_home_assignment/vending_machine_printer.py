from aviela_home_assignment.consts import Consts


class VendingMachinePrinter:
    """
    VendingMachinePrinter class which responsible to print VM messages
    """

    def InvalidCoin(self):
        print("\n*********************************************************************")
        print("********* You inserted invalid coin. please insert again ! **********")
        print("*********************************************************************")

    def NotEnoughMoney(self, iPrice, iCustomerMoney):
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

    def InitialMessage(self, sProductsType, AvailableDrinks, AvailableSweets, iCustomerMoney):
        print("\nYou can choose one of the following products:")
        if sProductsType == Consts.ALL:
            print(AvailableDrinks + AvailableSweets)
        elif sProductsType == Consts.SWEETS:
            print(AvailableSweets)
        elif sProductsType == Consts.DRINKS:
            print(AvailableDrinks)
        print(f"For now, your deposit money is {iCustomerMoney} " + str(Consts.CURRENCY_TYPE) + ".")
        print(f"For see just sweets press 's', for drinks 'd' and for all 'a'.")

    def ProductPayment(self, sProductName):
        print(f"Payment for {sProductName} is done.")

    def ChangeMoney(self, iChangeMoney):
        print(f"Change money is {iChangeMoney} " + Consts.CURRENCY_TYPE + ".")

    def CreatePrintListFromDict(self, dProducts):
        lAvailableProducts = []
        for Product in dProducts.values():
            if Product.iQuantity > 0:
                sAvailableProductWithPrice = "{} {} {} {} {} {}".format(Product.iUid, ":", Product.sName, "price", Product.iPrice, Consts.CURRENCY_TYPE)
                lAvailableProducts.append(sAvailableProductWithPrice)
        return lAvailableProducts

