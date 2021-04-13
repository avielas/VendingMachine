from aviela_home_assignment.consts import Consts
import json
from abc import abstractmethod


class ProductManager:
    """
    ProductManager manage the inventory of the products
    """
    def __init__(self, sProductsJsonFilePath):
        """
        @param sProductsJsonFilePath: path to json file which contains available products and their id, quantity, price and family
        """
        self._dProducts = dict([])
        self._sProductsJsonFilePath = sProductsJsonFilePath
        self._AddProducts()

    def GetAvailableProducts(self):
        """
        Get dict of all products with quantity greater than 0
        """
        dAvailableProducts = dict([])
        for Product in self.dProducts.values():
            if Product.iQuantity > 0:
                dAvailableProducts[Product.iUid] = Product
                # sAvailableProductWithPrice = "{} {} {} {} {} {}".format(pProduct.iUid, ":", pProduct.sName, "price", pProduct.iPrice, Consts.CURRENCY_TYPE)
                # lAvailableProducts.append(sAvailableProductWithPrice)
        return dAvailableProducts

    @property
    def dProducts(self):
        return self._dProducts

    def _AddProduct(self, iUid, Product):
        self._dProducts[iUid] = Product

    def RemoveProduct(self, iUid):
        if iUid in self._dProducts:
            del self._dProducts[iUid]
        else:
            raise KeyError("dictionary doesn't contain key")

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
    def _AddProducts(self):
        """
        This function take the id, name, price and quantity data to create product obj by storing it in the pProducts dictionary
        """
        raise NotImplementedError("_AddProducts is abstract function and you should implement it")

    def UpdateQuantity(self, iProductId):
        """
        remove 1 from product quantity after purchase
        @param iProductId: product id
        """
        self._dProducts[iProductId].Reduce1FromQuantity()
