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
        @param iCustomerMoney: current customer money value
        """
        # Read CoinsData.json
        with open(sMoneyJsonPath) as IOFile:
            lCoins = json.load(IOFile)

        self._dVmCoins = lCoins[0]
        self._iChangeMoney = 0
        self._dCustomerCoins = dict()
        # change all values on customer coins dictionary to 0
        self._dCustomerCoins.update(self._dVmCoins)
        for k, v in self._dCustomerCoins.items():
            self._dCustomerCoins[k] = 0

    @property
    def dVmCoins(self):
        return self._dVmCoins

    @property
    def iChangeMoney(self):
        return self._iChangeMoney

    @iChangeMoney.setter
    def iChangeMoney(self, x):
        self._iChangeMoney = x

    @property
    def dCustomerCoins(self):
        return self._dCustomerCoins

    @property
    def iCustomerMoney(self):
        return self.sum_coins()

    def dump_money(self, sJsonFilePath):
        mMoneyJsonToDump = json.dumps([self.__dict__])
        # Open the file for storing money data when the drink has been paid (we can overwrite CoinsData.json, but keep it separately to make it clear)
        with open(sJsonFilePath, "w") as IOFile:
            IOFile.write(mMoneyJsonToDump)

    def update_customer_money(self, coin):
        self.dCustomerCoins[coin] += 1

    def update_customer_coins(self, iProductPrice):
        iSumCustomerCoins = self.sum_coins()
        iChange = iSumCustomerCoins - iProductPrice
        lCoins = self.get_available_coins()
        iMinCoinChangeQuantity = self.min_coins_for_change(lCoins, iChange)
        dCoins = dict()
        self.calc_change_coins_quantity(lCoins, iMinCoinChangeQuantity, iChange, dCoins)
        self.add_customer_coins_to_vm_coins()
        # self.dCustomerCoins[coin] += 1
        pass

    def customer_have_enough_money(self, iProductPrice):
        return self.sum_coins() >= iProductPrice

    def sum_coins(self):
        iSum = 0
        for k, v in self._dCustomerCoins.items():
            iSum += (int(k)*self._dCustomerCoins[k])
        return iSum

    def min_coins_for_change(self, lCoins, iChange):
        if iChange < 1: return 0
        self.dp = [0] * (iChange + 1)
        lCoins.sort(reverse=True)
        return self.get_min_coins(lCoins, iChange)

    def get_min_coins(self, lCoins, iChange):
        if iChange < 0:
            return -1
        if iChange == 0:
            return 0
        if self.dp[iChange]:
            return self.dp[iChange]

        fMin = float("inf")

        for i in range(len(lCoins)):
            k = self.get_min_coins(lCoins, iChange - lCoins[i])
            if 0 <= k < fMin:
                fMin = k + 1

        self.dp[iChange] = -1 if fMin == float("inf") else fMin

        return self.dp[iChange]

    def get_available_coins(self):
        lCoins = []
        for k, v in self._dVmCoins.items():
            if v > 0:
                lCoins.append(int(k))
        return lCoins

    def calc_change_coins_quantity(self, lCoins, iMinCoinChangeQuantity, iChange, dCoins):
        if iChange < 0:
            return -1
        if iChange == 0:
            return 0

        x = 1
        inside = False
        for coin in lCoins:
            while 0 <= iChange - x*coin:
                x += 1
                inside = True
                if coin in dCoins:
                    dCoins[coin] = dCoins[coin] + 1
                else:
                    dCoins[coin] = 1
            x = x if not inside else x-1
            res = self.calc_change_coins_quantity(lCoins, iMinCoinChangeQuantity - x, iChange - x*coin, dCoins)
            if res == 0:
                break

        return res

    def add_customer_coins_to_vm_coins(self):
        for k, v in self._dCustomerCoins.items():
            if v > 0:
                if k in self._dVmCoins:
                    self._dVmCoins[k] = self._dVmCoins[k] + v
                else:
                    self._dVmCoins[k] = v
