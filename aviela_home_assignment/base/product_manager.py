from aviela_home_assignment.consts import Consts
import json
from abc import abstractmethod


class ProductManager:
    """
    ProductManager manage the inventory of the products
    """
    def __init__(self, sProductsJsonFilePath):
        self._dProducts = dict([])
        self._AddProducts(sProductsJsonFilePath)

    def GetAvailableProducts(self):
        """
        Get print list of all products with quantity greater than 0
        """
        lAvailableProducts = []
        for pProduct in self.dProducts.values():
            if pProduct.iQuantity > 0:
                sAvailableProductWithPrice = "{} {} {} {} {} {}".format(pProduct.iUid, ":", pProduct.sName, "price", pProduct.iPrice, Consts.CURRENCY_TYPE)
                lAvailableProducts.append(sAvailableProductWithPrice)
        return lAvailableProducts

    @property
    def dProducts(self):
        return self._dProducts

    def _AddProduct(self, iUid, Product):
        self._dProducts[iUid] = Product

    def _RemoveProduct(self, iUid):
        del self._dProducts[iUid]

    def DumpProducts(self, sJsonFilePath):
        """
        Stored values which created by json.dumps() to the file sJsonFilePath. This critical for persistently purposes.
        @param sJsonFilePath: json file path for dumping
        """
        # create a document (after update product quantity) in json format
        values = self.dProducts.values()
        pProductJsonToDump = json.dumps([productObj.__dict__ for productObj in values])
        # save the up-to-date product quantity to file
        with open(sJsonFilePath, "w") as IOFile:
            IOFile.write(pProductJsonToDump)

    @abstractmethod
    def _AddProducts(self, sProductsJsonFilePath):
        """
        This function take the id, name, price and quantity data to create product obj by storing it in the pProducts dictionary
        @param sProductsJsonFilePath: path to json file which contains available products and their id, quantity, price and family
        """
        raise NotImplementedError("add_products is abstract function and you should implement it")

    def UpdateQuantity(self, iProductId):
        """
        remove 1 from product quantity after purchase
        @param iProductId: product id
        """
        self._dProducts[iProductId].reduce_1_from_quantity()
