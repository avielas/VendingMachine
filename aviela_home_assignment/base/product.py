

class Product:
    """
    Vending Machine's Product
    """
    def __init__(self, uid, name, price, quantity):
        """
        @param uid: Uniq id for describe each product. Firstly initialize by JSON file and never change manually by program
        @param name: Product's name which visible to user. Firstly initialize by JSON file and never change manually by program
        @param price: Product's price which visible to user. Firstly initialize by JSON file and never change manually by program
        @param quantity: Product's quantity which visible to user. The VM update this value in any change
        """
        self.uid = uid
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, x):
        self._uid = x

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