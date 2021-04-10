import json
from aviela_home_assignment.drink import Drink
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.interface.product_manager import ProductManager


class DrinkManager(ProductManager):
    """
    DrinkManager class which implement ProductManager interface
    """
    def __init__(self, sDrinksJsonFilePath):
        """
        @param sDrinksJsonFilePath: path to json file which contains available products and their quantity
        """
        self._dDrinks = []
        # Read ProductData.json. This will take the id, name, price and quantity data to create drink obj by storing it in the _drink_data dictionary
        with open(sDrinksJsonFilePath) as fd:
            lDrinks = json.load(fd)
            for dDrink in lDrinks:
                if dDrink["_sProductFamily"] == Consts.DRINKS:
                    drink = Drink(dDrink["_iUid"], dDrink["_sName"], dDrink["_iPrice"], dDrink["_iQuantity"])
                    self.add_drink_data(drink)
            # convert list to dictionary with ID as a key
            self._dDrinks = dict((x.iUid, x) for x in self._dDrinks)

    @property
    def dDrinks(self):
        return self._dDrinks

    # Create add_drink_data() to store drink in []
    def add_drink_data(self, dDrink):
        self._dDrinks.append(dDrink)

    def get_available_products(self):
        lAvailableProducts = []
        for dDrink in self._dDrinks.values():
            if dDrink.iQuantity > 0:
                sAvailableProductWithPrice = "{} {} {} {} {} {}".format(dDrink.iUid, ":", dDrink.sName, "price", dDrink.iPrice, Consts.CURRENCY_TYPE)
                lAvailableProducts.append(sAvailableProductWithPrice)
        return lAvailableProducts
