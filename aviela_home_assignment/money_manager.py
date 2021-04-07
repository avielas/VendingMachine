import json
from aviela_home_assignment.consts import Consts


class MoneyManager:
    """
    MoneyManager class for handle the money calculation and record
    """
    def __init__(self, money_json):
        # Read MoneyData.json
        with open(money_json) as fd:
            money_list = json.load(fd)
        # change
        self.change_money = money_list[0]["_change_money"]
        # customer money
        self.customer_money = money_list[0]["_customer_money"]

    @property
    def change_money(self):
        return self._change_money

    @change_money.setter
    def change_money(self, x):
        self._change_money = x

    @property
    def customer_money(self):
        return self._customer_money

    @customer_money.setter
    def customer_money(self, x):
        self._customer_money = x

    def record_money(self, json_moeny_data, json_file_path):
        # Open the file for storing money data when the drink has been paid (we can overwrite MoneyData.json, but keep it separately to make it clear)
        with open(json_file_path, "w") as write_file:
            write_file.write(json_moeny_data)

    def print_change_money(self, change_money):
        print(f"Change money is {change_money} " + Consts.CURRENCY_TYPE + ".")
