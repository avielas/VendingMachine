from aviela_home_assignment.base.product import Product


class Drink(Product):
    """
    Drink class which use from base Product
    """
    def __init__(self, iUid, sName, iPrice, iQuantity):
        """
        For variables documentation see Product class init description
        """
        super().__init__(iUid, sName, iPrice, iQuantity)
