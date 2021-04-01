from drink_manager import DrinkManager
from money_manager import MoneyManager
from vending_machine import VendingMachine


def main():
    drink_manager = DrinkManager("json/DrinkData.json")
    money_manager = MoneyManager("json/MoneyData.json")
    vending_machine = VendingMachine(drink_manager, money_manager)
    vending_machine.start_vending_machine()


if __name__ == "__main__":
    main()
