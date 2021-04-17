from aviela_home_assignment.base.product import Product
from aviela_home_assignment.consts import Consts


class Snack(Product):
    """
    Snack class which is a Product
    """
    def __init__(self, iUid, sName, iPrice, iQuantity, bSweet):
        """
        For variables documentation see Product class init description
        """
        super().__init__(iUid, sName, iPrice, iQuantity, Consts.SNACK)
        self._bSweet = bSweet

    @property
    def bSweet(self):
        return self._bSweet
