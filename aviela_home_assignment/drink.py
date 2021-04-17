from aviela_home_assignment.base.product import Product
from aviela_home_assignment.consts import Consts


class Drink(Product):
    """
    Drink class which is a Product
    """
    def __init__(self, iUid, sName, iPrice, iQuantity, bSparkling):
        """
        For variables documentation see Product class init description
        """
        super().__init__(iUid, sName, iPrice, iQuantity, Consts.DRINK)
        self._bSparkling = bSparkling

    @property
    def bSparkling(self):
        return self._bSparkling
