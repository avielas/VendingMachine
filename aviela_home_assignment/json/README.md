
Few words to explain json files use case:
* ProductData - contains initial drinks data of the vending machine (id, name, price, quantity, product_family)
  BE MINDED: DataReader use 'eval' for decide the class's name according to json definition of _sProductFamily
* ProductDataDump - contains mid product data of the vending machine (id, name, price, quantity, product_family). Actually it's the product data state of the machine
* CoinsData - contains initial change money data of the vending machine. it's represented by dictionary which store quantity of each coin (coin, quantity)
* CoinsDataDump - contains mid change money data of the vending machine. it's represented by dictionary which store quantity of each coin (coin, quantity)