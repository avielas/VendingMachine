import json
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.snack import Snack
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
                if pProduct[Consts.sProductFamily] == Consts.DRINK:
                    product = eval(pProduct[Consts.sProductFamily])(pProduct[Consts.iUid], pProduct[Consts.sName],
                                                                    pProduct[Consts.iPrice], pProduct[Consts.iQuantity], pProduct[Consts.bSparkling])
                elif pProduct[Consts.sProductFamily] == Consts.SNACK:
                    product = eval(pProduct[Consts.sProductFamily])(pProduct[Consts.iUid], pProduct[Consts.sName],
                                                                    pProduct[Consts.iPrice], pProduct[Consts.iQuantity], pProduct[Consts.bSweet])
                dProducts[product.iUid] = product
        return dProducts

    def ReadCoinsDataFromFile(self, sCoinsJsonFilePath: str) -> dict:
        """
        Read coins data from json file and keep them on one coins list
        @param sCoinsJsonFilePath: path to json file which contains coins and their quantity
        @type sCoinsJsonFilePath: String
        @type sCoinsJsonFilePath: String
        @return: Dictionary with coins
        @rtype: Dictionary
        """
        with open(sCoinsJsonFilePath) as IOFile:
            dCoins = json.load(IOFile)
        return dCoins

    def FilterData(self, Products: dict, sProductType: str, specificProductsType: bool) -> dict:
        """
        Read coins data from json file and keep them on one coins list
        @param Products: products dictionary
        @type Products: Dictionary
        @param sProductType: product's type to show to user (ALL, SNACK, DRINK)
        @type Products: String
        @param specificProductsType: product's specific type to show to user (sweet Snacks only, sparkling Drink only)
        @type specificProductsType: Boolean
        @return: Dictionary with filtered product
        @rtype: Dictionary
        """
        if sProductType == Consts.ALL:
            return Products
        filteredProducts = dict([])
        for pProduct in Products.values():
            if specificProductsType and pProduct.sProductFamily == sProductType and sProductType == Consts.DRINK and pProduct.bSparkling:
                filteredProducts[pProduct.iUid] = pProduct
            elif specificProductsType and pProduct.sProductFamily == sProductType and sProductType == Consts.SNACK and pProduct.bSweet:
                filteredProducts[pProduct.iUid] = pProduct
            elif not specificProductsType and pProduct.sProductFamily == sProductType:
                filteredProducts[pProduct.iUid] = pProduct
        return filteredProducts
