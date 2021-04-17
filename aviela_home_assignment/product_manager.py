from aviela_home_assignment.data_reader import DataReader
import json


class ProductManager:
    """
    ProductManager manage the inventory of the products
    """
    def __init__(self, sProductsJsonFilePath: str):
        """
        @param sProductsJsonFilePath: path to json file which contains available products and their id, quantity, price and family
        @type sProductsJsonFilePath: String
        """
        self._dProducts = dict([])
        self.__dataReader = DataReader()
        self._dProducts = self.__dataReader.ReadProductsDataFromFile(sProductsJsonFilePath)

    @property
    def dProducts(self) -> dict:
        """
        Dictionary of VM products which loaded from JSON file
        @return: All product on dict
        @rtype: Dictionary
        """
        return self._dProducts

    def GetAvailableProducts(self) -> dict:
        """
        Get dict of all products with quantity greater than 0
        @return: Dictionary of all products with quantity greater than 0
        @rtype: Dictionary
        """
        dAvailableProducts = dict([])
        for Product in self.dProducts.values():
            if Product.iQuantity > 0:
                dAvailableProducts[Product.iUid] = Product
        return dAvailableProducts

    def RemoveProduct(self, ProductUid: int):
        """
        Remove product from dProducts dict
        @param ProductUid: Product iUid
        @type ProductUid: Integer
        """
        pProduct = self._dProducts[ProductUid]
        if pProduct in self._dProducts.values():
            del self._dProducts[pProduct.iUid]
        else:
            raise KeyError("dictionary doesn't contain key")

    def DumpProducts(self, sJsonFilePath: str):
        """
        Stored values which created by json.dumps() to the file sJsonFilePath. This critical for persistently purposes.
        @param sJsonFilePath: json file path for dumping
        @type sJsonFilePath: String
        """
        # create a document (after update product quantity) in json format
        values = self.dProducts.values()
        pProductJsonToDump = json.dumps([productObj.__dict__ for productObj in values])
        # save the up-to-date product quantity to file
        with open(sJsonFilePath, "w") as IOFile:
            IOFile.write(pProductJsonToDump)

    def UpdateQuantity(self, iProductId: int):
        """
        remove 1 from product quantity after purchase
        @param iProductId: product id
        @type iProductId: Integer
        """
        self._dProducts[iProductId].Reduce1FromQuantity()
