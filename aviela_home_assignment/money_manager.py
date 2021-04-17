from aviela_home_assignment.data_reader import DataReader
import json
from aviela_home_assignment.consts import Consts
from aviela_home_assignment.calculator import Calculator


class MoneyManager:
    """
    MoneyManager class for handle the money calculation and record
    """
    def __init__(self, sMoneyJsonPath, sCoinsJsonPath):
        """
        @param sCoinsJsonPath: JSON path to initialize variable dVmCoins
        @param sMoneyJsonPath: JSON path to initialize variables iChangeMoney, iCustomerMoney values
        @param iVmChangeMoney: current change money value of the vending machine
        @param iCustomerMoney: current costumer money value
        @param iCustomerChangeMoney: current costumer change money value
        """
        self.__calculator = Calculator()
        self.__dataReader = DataReader()
        self.__dMoney = self.__dataReader.ReadMoneyDataFromFile(sMoneyJsonPath)
        self._dVmCoins = self.__dataReader.ReadCoinsDataFromFile(sCoinsJsonPath)
        self.__initDCostumerCoins()
        self._dCostumerChangeCoins = dict([])

        self._iVmChangeMoney = self.__dMoney[Consts.iVmChangeMoney]
        self._iCustomerMoney = self.__dMoney[Consts.iCustomerMoney]
        # self._iCustomerChangeMoney = self.__dMoney[Consts.iCustomerChangeMoney]

    @property
    def dVmCoins(self):
        return self._dVmCoins

    @property
    def dCostumerCoins(self):
        return self._dCostumerCoins

    @property
    def dCostumerChangeCoins(self):
        return self._dCostumerChangeCoins

    @property
    def iVmChangeMoney(self):
        return self.__sumCoinsDict(self._dVmCoins)
        # return self._iVmChangeMoney

    @property
    def iCustomerMoney(self):
        return self.__sumCoinsDict(self._dCostumerCoins)

    @property
    def iCustomerChangeMoney(self):
        return self.__sumCoinsDict(self._dCostumerChangeCoins)

    def DumpMoney(self, sJsonMoneyFilePath, sJsonCoinsFilePath):
        dMoney = dict([])
        dMoney[Consts.iVmChangeMoney] = self.iVmChangeMoney
        dMoney[Consts.iCustomerMoney] = self.iCustomerMoney
        # dMoney[Consts.iCustomerChangeMoney] = self.iCustomerChangeMoney
        sMoneyJsonToDump = json.dumps(dMoney)
        # Open the file for storing money data when the product has been paid (we can overwrite MoneyData.json, but keep it separately to make it clear)
        with open(sJsonMoneyFilePath, "w") as IOFile:
            IOFile.write(sMoneyJsonToDump)
        sCoinsJsonToDump = json.dumps(self.dVmCoins)
        # Open the file for storing coins data when the product has been paid (we can overwrite CoinsData.json, but keep it separately to make it clear)
        with open(sJsonCoinsFilePath, "w") as IOFile:
            IOFile.write(sCoinsJsonToDump)

    def AddToCustomerCoins(self, coin: str):
        if coin in self._dCostumerCoins:
            self._dCostumerCoins[coin] = self._dCostumerCoins[coin] + 1
        else:
            raise KeyError("Can't add the coin because Vending Machine doesn't support it")
            pass

    def CustomerHaveEnoughMoney(self, ProductPrice: int):
        return self.iCustomerMoney >= ProductPrice

    # def AddToCustomerChangeMoney(self, iProductPrice):
    #     self._iCustomerChangeMoney = self.iCustomerMoney - iProductPrice

    def VmHaveEnoughChange(self, ProductPrice):
        # return self.iCustomerChangeMoney < self._iVmChangeMoney

        # merge 2 dictionaries
        dTotalCoins = self._dCostumerCoins.copy()
        for k, v in self._dVmCoins.items():
            dTotalCoins[k] += v

        iChange = self.iCustomerMoney - ProductPrice
        ChangeCoins = self.__calculator.CalculateMinimum(dTotalCoins.copy(), iChange)
        if ChangeCoins is None:
            return False
        else:
            self._dCostumerChangeCoins = ChangeCoins
            self._dVmCoins = dTotalCoins
            self._dCostumerCoins = dict([])

            # update dVmCoins
            for k, v in ChangeCoins.items():
                self._dVmCoins[k] -= v

            return True

    def __sumCoinsDict(self, dDict):
        sm = 0
        for k, v in dDict.items():
            sm += int(k)*int(v)
        return sm

    def __initDCostumerCoins(self):
        self._dCostumerCoins = dict([])
        for k, v in self.dVmCoins.items():
            self._dCostumerCoins[k] = 0
