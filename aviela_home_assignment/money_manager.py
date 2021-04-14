from aviela_home_assignment.data_reader import DataReader
import json
from aviela_home_assignment.consts import Consts


class MoneyManager:
    """
    MoneyManager class for handle the money calculation and record
    """
    def __init__(self, sMoneyJsonPath):
        """
        @param sMoneyJsonPath: JSON path to initialize variables iChangeMoney, iCustomerMoney values
        @param iVmChangeMoney: current change money value of the vending machine
        @param iCustomerMoney: current costumer money value
        @param iCustomerChangeMoney: current costumer change money value
        """
        self.__dMoney = DataReader().ReadMoneyDataFromFile(sMoneyJsonPath)

        self._iVmChangeMoney = self.__dMoney[Consts.iVmChangeMoney]
        self._iCustomerMoney = self.__dMoney[Consts.iCustomerMoney]
        self._iCustomerChangeMoney = self.__dMoney[Consts.iCustomerChangeMoney]

    @property
    def iVmChangeMoney(self):
        return self._iVmChangeMoney

    @property
    def iCustomerMoney(self):
        return self._iCustomerMoney

    @property
    def iCustomerChangeMoney(self):
        return self._iCustomerChangeMoney

    def DumpMoney(self, sJsonFilePath):
        dMoney = dict([])
        dMoney[Consts.iVmChangeMoney] = self._iVmChangeMoney
        dMoney[Consts.iCustomerMoney] = self._iCustomerMoney
        dMoney[Consts.iCustomerChangeMoney] = self._iCustomerChangeMoney
        sMoneyJsonToDump = json.dumps([dMoney])
        # Open the file for storing money data when the drink has been paid (we can overwrite MoneyData.json, but keep it separately to make it clear)
        with open(sJsonFilePath, "w") as IOFile:
            IOFile.write(sMoneyJsonToDump)

    def AddToCustomerMoney(self, x):
        self._iCustomerMoney = self._iCustomerMoney + x

    def AddToVmChangeMoney(self, x):
        self._iVmChangeMoney = self._iVmChangeMoney + x

    def CustomerHaveEnoughMoney(self, Product):
        return self._iCustomerMoney >= Product.iPrice

    def AddToCustomerChangeMoney(self, iProductPrice):
        self._iCustomerChangeMoney = self._iCustomerMoney - iProductPrice

    def HaveEnoughChange(self):
        return self._iCustomerChangeMoney < self._iVmChangeMoney
