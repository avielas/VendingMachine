from base.product import Product


class Drink(Product):
    """
    Drink class which inherit from base Product
    """
    def __init__(self, id, name, price, quantity):
        super().__init__(id, name, price, quantity)
