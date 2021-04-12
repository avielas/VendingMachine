import json
from aviela_home_assignment.sweet import Sweet
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.base.product_manager import ProductManager


class SweetManager(ProductManager):
    """
    SweetManager class which implement ProductManager interface
    """
    def __init__(self, sProductsJsonFilePath):
        super().__init__(sProductsJsonFilePath)

    def _AddProducts(self, sProductsJsonFilePath):
        with open(sProductsJsonFilePath) as fd:
            lProducts = json.load(fd)
            for Product in lProducts:
                if Product["_sProductFamily"] == Consts.SWEETS:
                    sweet = Sweet(Product["_iUid"], Product["_sName"], Product["_iPrice"], Product["_iQuantity"])
                    self._AddProduct(Product["_iUid"], sweet)
