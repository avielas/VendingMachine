import json
from drink import Drink
from consts import Consts
from interface.product_manager import ProductManager


class DrinkManager(ProductManager):
    """
        DrinkManager class which implement ProductManager interface
    """
    def __init__(self, drink_json):
        self.drink_data = []
        # Read DrinkData.json. This will take the id, name, price and quantity data to create drink obj by storing it in the _drink_data dictionary
        with open(drink_json) as fd:
            drink_list = json.load(fd)
            for drink_dic in drink_list:
                drink = Drink(drink_dic["_id"], drink_dic["_name"], drink_dic["_price"], drink_dic["_quantity"])
                self.add_drink_data(drink)
            # convert list to dictionary with ID as a key
            self._drink_data = dict((x.uid, x) for x in self._drink_data)

    @property
    def drink_data(self):
        return self._drink_data

    @drink_data.setter
    def drink_data(self, x):
        self._drink_data = x

    # Create add_drink_data() to store drink in []
    def add_drink_data(self, drink):
        self._drink_data.append(drink)

    def get_available_data(self):
        available_drinks = []
        for drink in self._drink_data.values():
            if drink.quantity > 0:
                available_drink_with_price = "{} {} {} {} {} {}".format(drink.uid, ":", drink.name, "price", drink.price, Consts.CURRENCY_TYPE)
                available_drinks.append(available_drink_with_price)
        return available_drinks

    def record_object_data(self, json_drink_data, json_file_path):
        # Open the file for storing information of the number of cans when the drink is dispensed (we can override DrinkData.json, but keep it separately to make it clear)
        with open(json_file_path, "w") as write_file:
            write_file.write(json_drink_data)

    def print_drink_payment(self, drink_name):
        print(f"Payment for {drink_name} is done.")
