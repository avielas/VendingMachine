

class Product:
    """
    Base class (for inheritance use) which define basic member variables for Vending Machine's Product
    """
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, x):
        self._id = x

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, x):
        self._name = x

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, x):
        self._price = x

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, x):
        self._quantity = x