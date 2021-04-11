from aviela_home_assignment.sweet_manager import SweetManager
from aviela_home_assignment.drink_manager import DrinkManager
from aviela_home_assignment.money_manager import MoneyManager
from aviela_home_assignment.vending_machine import VendingMachine
from aviela_home_assignment.consts import Consts


def main():
    sm = SweetManager(Consts.JSON_DIR_PATH_PROGRAM + Consts.PRODUCT_DATA_JSON_FILE)
    dm = DrinkManager(Consts.JSON_DIR_PATH_PROGRAM + Consts.PRODUCT_DATA_JSON_FILE)
    mm = MoneyManager(Consts.JSON_DIR_PATH_PROGRAM + Consts.MONEY_DATA_JSON_FILE)
    vm = VendingMachine(sm, dm, mm)
    vm.start_vending_machine()


if __name__ == "__main__":
    main()
