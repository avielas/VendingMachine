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
        # Read MoneyData.json
        with open(sMoneyJsonPath) as IOFile:
            lMoney = json.load(IOFile)
        self._iVmChangeMoney = lMoney[0]["_iVmChangeMoney"]
        self._iCustomerMoney = lMoney[0]["_iCustomerMoney"]
        self._iCustomerChangeMoney = lMoney[0]["_iCustomerChangeMoney"]

    @property
    def iVmChangeMoney(self):
        return self._iVmChangeMoney

    @property
    def iCustomerMoney(self):
        return self._iCustomerMoney

    @property
    def iCustomerChangeMoney(self):
        return self._iCustomerChangeMoney

    def dump_money(self, sJsonFilePath):
        mMoneyJsonToDump = json.dumps([self.__dict__])
        # Open the file for storing money data when the drink has been paid (we can overwrite MoneyData.json, but keep it separately to make it clear)
        with open(sJsonFilePath, "w") as IOFile:
            IOFile.write(mMoneyJsonToDump)

    def add_to_customer_money(self, x):
        self._iCustomerMoney = self._iCustomerMoney + x

    def add_to_vm_change_money(self, x):
        self._iVmChangeMoney = self._iVmChangeMoney + x

    def customer_have_enough_money(self, pProduct):
        return self._iCustomerMoney >= pProduct.iPrice

    def add_to_customer_change_money(self, iProductPrice):
        self._iCustomerChangeMoney = self._iCustomerMoney - iProductPrice

    def have_enough_change(self):
        return self._iCustomerChangeMoney < self._iVmChangeMoney
