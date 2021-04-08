import json
from aviela_home_assignment.consts import Consts


class VendingMachine:
    """
    VendingMachine class which run the main flow
    """
    def __init__(self, dm, mm):
        self._dmDrinkManager = dm
        self._mmMoneyManager = mm

    def start_vending_machine(self):
        # Open infinity loop which can stop by ctrl+c
        while True:
            print("\n --- Vending machine --- ")
            self.print_initial_message()
            # Get input from customer
            sCoins = ', '.join(Consts.COINS_LIST)
            sUserInput = str(input("Please insert coin " + sCoins + " " + str(Consts.CURRENCY_TYPE) + ". To place order, press 0: "))
            # If you drop valid coin, add the money that has been added continuously with customer_money
            if sUserInput in Consts.COINS_LIST:
                self._mmMoneyManager.iCustomerMoney = self._mmMoneyManager.iCustomerMoney + int(sUserInput)
            # If you click to select the product
            elif sUserInput == '0':
                while True:
                    self.print_initial_message()
                    # Keep what the customer choose to drink
                    try:
                        iDrinkId = int(input("Please give the id of the drink you want: "))
                    except ValueError:
                        self.print_invalid_drink_id_error_mesaage()
                        continue
                    dDrinks = self._dmDrinkManager.dDrinks
                    if iDrinkId in dDrinks:
                        dDrink = dDrinks[iDrinkId]
                        break
                    else:
                        self.print_invalid_drink_id_error_mesaage()
                        continue
                if self._mmMoneyManager.iCustomerMoney < dDrink.iPrice:
                    self.print_not_enough_money_to_buy_drink_error_message(dDrink)
                    continue
                else:
                    iChange = self._mmMoneyManager.iCustomerMoney - dDrink.iPrice
                    # update machine change
                    self._mmMoneyManager.iChangeMoney = self._mmMoneyManager.iChangeMoney + dDrink.iPrice
                    dDrink.iQuantity = dDrink.iQuantity - 1
                    self._mmMoneyManager.iCustomerMoney = 0
                    # create a document (after update drink quantity) in format json from _drink_manager.get_drink_data()
                    sDrinkJsonToDump = json.dumps([drinkobj.__dict__ for drinkobj in self._dmDrinkManager.dDrinks.values()])
                    # save the up-to-date drink quantity to file
                    self._dmDrinkManager.record_object_data(sDrinkJsonToDump, Consts.JSON_DIR_PATH_PROGRAM + Consts.DRINK_DATA_AFTER_BUY_JSON_FILE_NAME)
                    # create a format json document from money_manager.
                    sMoneyJsonToDump = json.dumps([self._mmMoneyManager.__dict__])
                    # save the new amount into file
                    self._mmMoneyManager.record_money(sMoneyJsonToDump, Consts.JSON_DIR_PATH_PROGRAM + Consts.MONEY_DATA_AFTER_BUY_JSON_FILE_NAME)
                    self.print_change_money(iChange)
                    self.print_drink_payment(dDrink.sName)
                break
            else:
                self.print_invalid_coin_error_message()

    def print_invalid_coin_error_message(self):
        print("\n*********************************************************************")
        print("********* You inserted invalid coin. please insert again ! **********")
        print("*********************************************************************")

    def print_not_enough_money_to_buy_drink_error_message(self, dDrink):
        print("\n************************************************************************************************************")
        print("***** The money that drops(" + str(self._mmMoneyManager.iCustomerMoney) + ") is less than the price(" + str(
            dDrink.iPrice) + ") of the product, please insert more money !!! *****")
        print("************************************************************************************************************\n")

    def print_invalid_drink_id_error_mesaage(self):
        print("\n**************************************************************************************************************")
        print("************************************** invalid drink id. please try again! ***********************************")
        print("**************************************************************************************************************\n")

    def print_initial_message(self):
        print("\nYou can choose one of the following drinks:")
        print(self._dmDrinkManager.get_available_products())
        print(f"For now, your deposit money is {self._mmMoneyManager.iCustomerMoney} " + str(Consts.CURRENCY_TYPE) + ".")

    def print_drink_payment(self, sDrinkName):
        print(f"Payment for {sDrinkName} is done.")

    def print_change_money(self, iChangeMoney):
        print(f"Change money is {iChangeMoney} " + Consts.CURRENCY_TYPE + ".")
