import json
from aviela_home_assignment.consts import Consts


class MoneyManager:
    """
    MoneyManager class for handle the money calculation and record
    """
    def __init__(self, sMoneyJsonPath):
        """
        @param sMoneyJsonPath: JSON path to initialize variables iChangeMoney, iCustomerMoney values
        @param iChangeMoney: current change money value of the vending machine
        @param iCustomerMoney: current costumer money value
        """
        # Read MoneyData.json
        with open(sMoneyJsonPath) as IOFile:
            lMoney = json.load(IOFile)
        # change
        self.iChangeMoney = lMoney[0]["_iChangeMoney"]
        # customer money
        self.iCustomerMoney = lMoney[0]["_iCustomerMoney"]

    @property
    def iChangeMoney(self):
        return self._iChangeMoney

    @iChangeMoney.setter
    def iChangeMoney(self, x):
        self._iChangeMoney = x

    @property
    def iCustomerMoney(self):
        return self._iCustomerMoney

    @iCustomerMoney.setter
    def iCustomerMoney(self, x):
        self._iCustomerMoney = x

    def dump_money(self, sJsonFilePath):
        mMoneyJsonToDump = json.dumps([self.__dict__])
        # Open the file for storing money data when the drink has been paid (we can overwrite MoneyData.json, but keep it separately to make it clear)
        with open(sJsonFilePath, "w") as IOFile:
            IOFile.write(mMoneyJsonToDump)
