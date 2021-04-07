from base.product import Product


class Drink(Product):
    """
    Drink class which inherit from base Product
    """
    def __init__(self, uid, name, price, quantity):
        super().__init__(uid, name, price, quantity)
