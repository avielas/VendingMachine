from aviela_home_assignment.base.product import Product
from aviela_home_assignment.consts import Consts


class Sweet(Product):
    """
    Sweet class which use from base Product
    """
    def __init__(self, iUid, sName, iPrice, iQuantity):
        """
        For variables documentation see Product class init description
        """
        super().__init__(iUid, sName, iPrice, iQuantity, Consts.SWEETS)
