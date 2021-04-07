from aviela_home_assignment.drink_manager import DrinkManager
from aviela_home_assignment.money_manager import MoneyManager
from aviela_home_assignment.vending_machine import VendingMachine
from aviela_home_assignment.consts import Consts

def main():
    drink_manager = DrinkManager(Consts.JSON_DIR_PATH_PROGRAM + Consts.DRINK_DATA_JSON_FILE_NAME)
    money_manager = MoneyManager(Consts.JSON_DIR_PATH_PROGRAM + Consts.MONEY_DATA_JSON_FILE_NAME)
    vending_machine = VendingMachine(drink_manager, money_manager)
    vending_machine.start_vending_machine()


if __name__ == "__main__":
    main()
