from aviela_home_assignment.sweet_manager import SweetManager
from aviela_home_assignment.drink_manager import DrinkManager
from aviela_home_assignment.money_manager import MoneyManager
from aviela_home_assignment.vending_machine import VendingMachine
from aviela_home_assignment.consts import Consts


def main():
    SM = SweetManager(Consts.JSON_DIR_PATH_PROGRAM + Consts.PRODUCT_DATA_JSON_FILE)
    DM = DrinkManager(Consts.JSON_DIR_PATH_PROGRAM + Consts.PRODUCT_DATA_JSON_FILE)
    MM = MoneyManager(Consts.JSON_DIR_PATH_PROGRAM + Consts.MONEY_DATA_JSON_FILE)
    VM = VendingMachine(SM, DM, MM)
    VM.StartVendingMachine()


if __name__ == "__main__":
    main()
