from aviela_home_assignment.data_reader import DataReader
import json
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.calculator import Calculator


class MoneyManager:
    """
    MoneyManager class for handle coins, money and dumping
    """
    def __init__(self, sCoinsJsonPath: str):
        """
        @param sCoinsJsonPath: JSON path to initialize variable dVmCoins
        @type sCoinsJsonPath: String
        """
        self.__Calculator = Calculator()
        self.__DataReader = DataReader()
        self.__dVmCoins = self.__DataReader.ReadCoinsDataFromFile(sCoinsJsonPath)
        self.__initDCostumerCoins()
        self._dCostumerChangeCoins = dict([])

    @property
    def dVmCoins(self) -> dict:
        """
        Dictionary of VM's coins which loaded from JSON and update each time user buy product
        @return: Dictionary of coins
        @rtype: Dictionary
        """
        return self.__dVmCoins

    @property
    def dCostumerChangeCoins(self) -> dict:
        """
        Dictionary of customer's coins which update each time user buy product and reset after VM finished to run
        @return: Dictionary of coins
        @rtype: Dictionary
        """
        return self._dCostumerChangeCoins

    @property
    def iVmChangeMoney(self) -> int:
        """
        Current change money value of the vending machine
        @return: current VM change money value
        @rtype: Integer
        """
        return self.__sumCoinsDict(self.__dVmCoins)

    @property
    def iCustomerMoney(self) -> int:
        """
        Current costumer money value
        @return: costumer money value
        @rtype: Integer
        """
        return self.__sumCoinsDict(self._dCostumerCoins)

    @property
    def iCustomerChangeMoney(self) -> int:
        """
        Current costumer change money value
        @return: costumer money value
        @rtype: Integer
        """
        return self.__sumCoinsDict(self._dCostumerChangeCoins)

    def DumpMoney(self, sJsonCoinsFilePath: str):
        """
        Stored values which created by json.dumps() to the files sJsonCoinsFilePath. This critical for persistently purposes.
        @param sJsonCoinsFilePath: Coins json file path for dumping
        @type sJsonCoinsFilePath: String
        """
        sCoinsJsonToDump = json.dumps(self.dVmCoins)
        # Open the file for storing coins data when the product has been paid (we can overwrite CoinsData.json, but keep it separately to make it clear)
        with open(sJsonCoinsFilePath, "w") as IOFile:
            IOFile.write(sCoinsJsonToDump)

    def AddToCustomerCoins(self, coin: str):
        """
        Add coin to customer coins dictionary
        @param coin: Valid coin (for valid coins see CoinsData.json)
        @type coin: String
        """
        if coin in self._dCostumerCoins:
            self._dCostumerCoins[coin] = self._dCostumerCoins[coin] + 1
        else:
            raise KeyError("Can't add the coin because Vending Machine doesn't support it")
            pass

    def CustomerHaveEnoughMoney(self, ProductPrice: int) -> bool:
        """
        Validate if customer have enough money to buy product
        @param ProductPrice: the price of the product
        @type ProductPrice: Integer
        @return: True if yes, else False
        @rtype: Boolean
        """
        return self.iCustomerMoney >= ProductPrice

    def VmHaveEnoughChange(self, ProductPrice: int) -> bool:
        """
        This function use CalculateMinimum to check if VM have enough change to return to user.
        Read CalculateMinimum and __CalculateFinite documentation for more details
        @param ProductPrice: the price of the product
        @type ProductPrice: Integer
        @return: True if yes, else False
        @rtype: Boolean
        """

        # merge 2 dictionaries
        dTotalCoins = self._dCostumerCoins.copy()
        for k, v in self.__dVmCoins.items():
            dTotalCoins[k] += v

        iChange = self.iCustomerMoney - ProductPrice
        ChangeCoins = dict([]) if iChange == 0 else self.__Calculator.CalculateMinimum(dTotalCoins.copy(), iChange)
        if iChange != 0 and ChangeCoins is None:
            return False
        else:
            self._dCostumerChangeCoins = ChangeCoins
            self.__dVmCoins = dTotalCoins
            self._dCostumerCoins = dict([])

            # update dVmCoins
            for k, v in ChangeCoins.items():
                self.__dVmCoins[k] -= v

            return True

    def __sumCoinsDict(self, dDict: dict) -> int:
        """
        Sum all values*keys on Dictionary (v1*k1 + v2*k2 + ... + vn*kn)
        @param dDict: Dictionary of coins
        @type dDict: Dictionary
        @return: sum of keys
        @rtype: Integer
        """
        sm = 0
        for k, v in dDict.items():
            sm += int(k)*int(v)
        return sm

    def __initDCostumerCoins(self):
        """
        Init _dCostumerCoins variable from dVmCoins but insert 0 to all keys
        """
        self._dCostumerCoins = dict([])
        for k, v in self.dVmCoins.items():
            self._dCostumerCoins[k] = 0
