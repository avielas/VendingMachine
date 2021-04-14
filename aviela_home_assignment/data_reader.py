import json
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.sweet import Sweet
from aviela_home_assignment.consts import Consts


class DataReader:
    """
    DataReader class which responsible to read data from VM's ProductData.json
    """

    def ReadProductsDataFromFile(self, sProductsJsonFilePath):
        """
        Read products from json file and keep them on one Products list
        @param sProductsJsonFilePath: path to json file which contains available products and their id, quantity, price and family
        """
        dProducts = dict([])
        with open(sProductsJsonFilePath) as IOFile:
            lProducts = json.load(IOFile)
            for pProduct in lProducts:
                product = eval(pProduct[Consts.sProductFamily])(pProduct[Consts.iUid], pProduct[Consts.sName],
                                                                pProduct[Consts.iPrice], pProduct[Consts.iQuantity], pProduct[Consts.sProductFamily])
                dProducts[product.iUid] = product
        return dProducts

    def ReadMoneyDataFromFile(self, sMoneyJsonFilePath):
        """
        Read money data from MoneyData.json
        @param sMoneyJsonFilePath: path to json file which contains available products and their id, quantity, price and family
        """
        dMoney = dict([])
        with open(sMoneyJsonFilePath) as IOFile:
            lMoney = json.load(IOFile)
        dMoney[Consts.iVmChangeMoney] = lMoney[0][Consts.iVmChangeMoney]
        dMoney[Consts.iCustomerMoney] = lMoney[0][Consts.iCustomerMoney]
        dMoney[Consts.iCustomerChangeMoney] = lMoney[0][Consts.iCustomerChangeMoney]
        return dMoney

    def FilterData(self, Products, sProductType):
        if sProductType == Consts.ALL:
            return Products
        filteredProducts = dict([])
        for pProduct in Products.values():
            if pProduct.sProductFamily == sProductType:
                filteredProducts[pProduct.iUid] = pProduct
        return filteredProducts
