

class Product:
    """
    Vending Machine's Product
    """
    def __init__(self, iUid: int, sName: str, iPrice: int, iQuantity: int, sProductFamily: str):
        """
        @param iUid: Uniq id for describe each product. Firstly initialize by JSON file and never change manually by program
        @param sName: Product's name which visible to user. Firstly initialize by JSON file and never change manually by program
        @param iPrice: Product's price which visible to user. Firstly initialize by JSON file and never change manually by program
        @param iQuantity: Product's quantity which visible to user. The VM update this value in any change
        @param sProductFamily: Product's family which describe the Product's group. useful for filtering purposes
        """
        self._iUid = iUid
        self._sName = sName
        self._iPrice = iPrice
        self._iQuantity = iQuantity
        self._sProductFamily = sProductFamily

    @property
    def iUid(self):
        return self._iUid

    @property
    def sName(self):
        return self._sName

    @property
    def iPrice(self):
        return self._iPrice

    @property
    def iQuantity(self):
        return self._iQuantity

    @property
    def sProductFamily(self):
        return self._sProductFamily

    def reduce_1_from_quantity(self):
        self._iQuantity -= 1
