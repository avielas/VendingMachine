
Few words to explain json files use case:
* ProductData - contains initial drinks data of the vending machine (id, name, price, quantity, product_family)  
* ProductDataDump - contains mid product data of the vending machine (id, name, price, quantity, product_family). Actually it's the product data state of the machine
* DrinkDataDump - contains mid drinks data of the vending machine (id, name, price, quantity, product_family). Actually it's the drink data state of the machine
* SweetDataDump - contains mid sweet data of the vending machine (id, name, price, quantity, product_family). Actually it's the sweet data state of the machine
* CoinsData - contains initial change money data of the vending machine. it's represent by dictionary which store quantity of each coin
* CoinsDataDump - contains mid change money data of the vending machine. it's represent by dictionary which store quantity of each coin