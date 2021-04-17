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
        with open(sMoneyJsonFilePath) as IOFile:
            dMoney = json.load(IOFile)
        return dMoney

    def ReadCoinsDataFromFile(self, sCoinsJsonFilePath):
        """
        Read coins data from CoinsData.json
        @param sCoinsJsonFilePath: path to json file which contains coins and their quantity
        """
        with open(sCoinsJsonFilePath) as IOFile:
            dCoins = json.load(IOFile)
        return dCoins

    def FilterData(self, Products, sProductType):
        if sProductType == Consts.ALL:
            return Products
        filteredProducts = dict([])
        for pProduct in Products.values():
            if pProduct.sProductFamily == sProductType:
                filteredProducts[pProduct.iUid] = pProduct
        return filteredProducts
