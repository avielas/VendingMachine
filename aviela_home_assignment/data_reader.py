import json
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.sweet import Sweet
from aviela_home_assignment.consts import Consts


class DataReader:
    """
    This class responsible to read data JSONs and filter Products dictionary
    """

    def ReadProductsDataFromFile(self, sProductsJsonFilePath: str) -> dict:
        """
        Read products from json file and keep them on one Products list
        @param sProductsJsonFilePath: path to json file which contains available products and their id, quantity, price and family
        @type sProductsJsonFilePath: String
        @return: Dictionary with all products
        @rtype: Dictionary
        """
        dProducts = dict([])
        with open(sProductsJsonFilePath) as IOFile:
            lProducts = json.load(IOFile)
            for pProduct in lProducts:
                product = eval(pProduct[Consts.sProductFamily])(pProduct[Consts.iUid], pProduct[Consts.sName],
                                                                pProduct[Consts.iPrice], pProduct[Consts.iQuantity], pProduct[Consts.sProductFamily])
                dProducts[product.iUid] = product
        return dProducts

    def ReadMoneyDataFromFile(self, sMoneyJsonFilePath: str) -> dict:
        """
        Read money data from json file and keep them on one money list
        @param sMoneyJsonFilePath: path to json file which contains serialized money class objects
        @type sMoneyJsonFilePath: String
        @return: Dictionary with money objects
        @rtype: Dictionary
        """
        with open(sMoneyJsonFilePath) as IOFile:
            dMoney = json.load(IOFile)
        return dMoney

    def ReadCoinsDataFromFile(self, sCoinsJsonFilePath: str) -> dict:
        """
        Read coins data from json file and keep them on one coins list
        @param sCoinsJsonFilePath: path to json file which contains coins and their quantity
        @type sCoinsJsonFilePath: String
        @return: Dictionary with coins
        @rtype: Dictionary
        """
        with open(sCoinsJsonFilePath) as IOFile:
            dCoins = json.load(IOFile)
        return dCoins

    def FilterData(self, Products: dict, sProductType: str) -> dict:
        """
        Read coins data from json file and keep them on one coins list
        @param Products: products dictionary
        @type Products: Dictionary
        @param sProductType: product's type to show to user (ALL, SWEET, DRINK)
        @type Products: String
        @return: Dictionary with filtered product
        @rtype: Dictionary
        """
        if sProductType == Consts.ALL:
            return Products
        filteredProducts = dict([])
        for pProduct in Products.values():
            if pProduct.sProductFamily == sProductType:
                filteredProducts[pProduct.iUid] = pProduct
        return filteredProducts
