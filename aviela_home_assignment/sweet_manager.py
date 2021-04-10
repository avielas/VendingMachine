import json
from aviela_home_assignment.sweet import Sweet
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.interface.product_manager import ProductManager


class SweetManager(ProductManager):
    """
    SweetManager class which implement ProductManager interface
    """
    def __init__(self, sJsonFilePath):
        """
        @param sJsonFilePath: path to json file which contains available products and their quantity
        """
        self._dSweets = []
        # Read ProductData.json. This will take the id, name, price and quantity data to create sweet obj by storing it in the _sweet_data dictionary
        with open(sJsonFilePath) as fd:
            lSweets = json.load(fd)
            for sSweet in lSweets:
                if sSweet["_sProductFamily"] == Consts.SWEETS:
                    sweet = Sweet(sSweet["_iUid"], sSweet["_sName"], sSweet["_iPrice"], sSweet["_iQuantity"])
                    self.add_sweet_data(sweet)
            # convert list to dictionary with ID as a key
            self._dSweets = dict((x.iUid, x) for x in self._dSweets)

    @property
    def sSweets(self):
        return self._dSweets

    # Create add_sweet_data() to store sweet in []
    def add_sweet_data(self, sSweet):
        self._dSweets.append(sSweet)

    def get_available_products(self):
        lAvailableProducts = []
        for sSweet in self._dSweets.values():
            if sSweet.iQuantity > 0:
                sAvailableProductWithPrice = "{} {} {} {} {} {}".format(sSweet.iUid, ":", sSweet.sName, "price", sSweet.iPrice, Consts.CURRENCY_TYPE)
                lAvailableProducts.append(sAvailableProductWithPrice)
        return lAvailableProducts
