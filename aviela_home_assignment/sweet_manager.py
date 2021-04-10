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

    def add_products(self, sProductsJsonFilePath):
        with open(sProductsJsonFilePath) as fd:
            lProducts = json.load(fd)
            for pProduct in lProducts:
                if pProduct["_sProductFamily"] == Consts.SWEETS:
                    sweet = Sweet(pProduct["_iUid"], pProduct["_sName"], pProduct["_iPrice"], pProduct["_iQuantity"])
                    self.add_product(pProduct["_iUid"], sweet)
