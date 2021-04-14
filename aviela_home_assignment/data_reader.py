import json
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.sweet import Sweet
from aviela_home_assignment.consts import Consts

class DataReader:
    """
    DataReader class which responsible to read data from VM's ProductData.json
    """
    def ReadDataFromFile(self, sProductsJsonFilePath):
        """
        Read products from json file and keep them on one Products list
        @param sProductsJsonFilePath: path to json file which contains available products and their id, quantity, price and family
        """
        dProducts = dict([])
        with open(sProductsJsonFilePath) as fd:
            lProducts = json.load(fd)
            for pProduct in lProducts:
                product = eval(pProduct["_sProductFamily"])(pProduct["_iUid"], pProduct["_sName"], pProduct["_iPrice"], pProduct["_iQuantity"], pProduct["_sProductFamily"])
                dProducts[product.iUid] = product
        return dProducts

    def FilterData(self, Products, sProductType):
        if sProductType == Consts.ALL:
            return Products
        filtered = dict([])
        for pProduct in Products.values():
            if pProduct.sProductFamily == sProductType:
                filtered[pProduct.iUid] = pProduct
        return filtered

