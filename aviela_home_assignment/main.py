from aviela_home_assignment.product_manager import ProductManager
from aviela_home_assignment.money_manager import MoneyManager
from aviela_home_assignment.vending_machine import VendingMachine
from aviela_home_assignment.vending_machine_printer import VendingMachinePrinter
from aviela_home_assignment.consts import Consts


def main():
    PM = ProductManager(Consts.JSON_DIR_PATH_PROGRAM + Consts.PRODUCT_DATA_JSON_FILE)
    MM = MoneyManager(Consts.JSON_DIR_PATH_PROGRAM + Consts.MONEY_DATA_JSON_FILE)
    VMP = VendingMachinePrinter()
    VM = VendingMachine(PM, MM, VMP)
    VM.StartVendingMachine()


if __name__ == "__main__":
    main()
