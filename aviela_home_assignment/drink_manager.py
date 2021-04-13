import json
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.base.product_manager import ProductManager


class DrinkManager(ProductManager):
    """
    DrinkManager class which implement ProductManager interface
    """
    def __init__(self, sProductsJsonFilePath):
        super().__init__(sProductsJsonFilePath)

    def _AddProducts(self):
        with open(self._sProductsJsonFilePath) as fd:
            lProducts = json.load(fd)
            for Product in lProducts:
                if Product["_sProductFamily"] == Consts.DRINKS:
                    drink = Drink(Product["_iUid"], Product["_sName"], Product["_iPrice"], Product["_iQuantity"])
                    self._AddProduct(Product["_iUid"], drink)
