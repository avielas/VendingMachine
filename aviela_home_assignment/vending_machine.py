import json
from consts import Consts


class VendingMachine:
    """
        VendingMachine class which run the main flow
    """
    def __init__(self, drink_manager, money_manager):
        self._drink_manager = drink_manager
        self._money_manager = money_manager

    def start_vending_machine(self):
        # Open infinity loop which can stop by ctrl+c
        while True:
            print("\n --- Vending machine --- ")
            self.print_initial_message()
            # Get input from customer
            coins_list_str = ', '.join(Consts.COINS_LIST)
            customer_coin = str(input("Please insert coin " + coins_list_str + " " + str(Consts.CURRENCY_TYPE) + ". To place order, press 0: "))
            # If you drop valid coin, add the money that has been added continuously with customer_money
            if customer_coin in Consts.COINS_LIST:
                self._money_manager.customer_money = self._money_manager.customer_money + int(customer_coin)
            # If you click to select the product
            elif customer_coin == '0':
                while True:
                    self.print_initial_message()
                    # Keep what the customer choose to drink
                    try:
                        drink_id = int(input("Please give the id of the drink you want: "))
                    except ValueError:
                        self.print_invalid_drink_id_error_mesaage()
                        continue
                    drink_data_dict = self._drink_manager.drink_data
                    if drink_id in drink_data_dict:
                        drink = drink_data_dict[drink_id]
                        break
                    else:
                        self.print_invalid_drink_id_error_mesaage()
                        continue
                if self._money_manager.customer_money < drink.price:
                    self.print_not_enough_money_to_buy_drink_error_message(drink)
                    continue
                else:
                    change = self._money_manager.customer_money - drink.price
                    # update machine change
                    self._money_manager.change_money = self._money_manager.change_money + drink.price
                    drink.quantity = drink.quantity - 1
                    self._money_manager.customer_money = 0
                    # create a document (after update drink quantity) in format json from _drink_manager.get_drink_data()
                    updated_drink_json = json.dumps([drinkobj.__dict__ for drinkobj in self._drink_manager.drink_data.values()])
                    # save the up-to-date drink quantity to file
                    self._drink_manager.record_object_data(updated_drink_json)
                    # create a format json document from money_manager.
                    updated_money_json = json.dumps([self._money_manager.__dict__])
                    # save the new amount into file
                    self._money_manager.record_money(updated_money_json)
                    self._money_manager.print_change_money(change)
                    self._drink_manager.print_drink_payment(drink.name)
                break
            else:
                self.print_invalid_coin_error_message()

    def print_invalid_coin_error_message(self):
        print("\n*********************************************************************")
        print("********* You inserted invalid coin. please insert again ! **********")
        print("*********************************************************************")

    def print_not_enough_money_to_buy_drink_error_message(self, drink):
        print("\n************************************************************************************************************")
        print("***** The money that drops(" + str(self._money_manager.customer_money) + ") is less than the price(" + str(
            drink.price) + ") of the product, please insert more money !!! *****")
        print("************************************************************************************************************\n")

    def print_invalid_drink_id_error_mesaage(self):
        print("\n**************************************************************************************************************")
        print("************************************** invalid drink id. please try again! ***********************************")
        print("**************************************************************************************************************\n")

    def print_initial_message(self):
        print("\nYou can choose one of the following drinks:")
        print(self._drink_manager.get_available_data())
        print(f"For now, your deposit money is {self._money_manager.customer_money} " + str(Consts.CURRENCY_TYPE) + ".")
