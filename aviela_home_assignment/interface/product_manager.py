import abc


class ProductManager(abc.ABC):
    """
    Abstract class (interface) which enforce users to implement the methods below when implementing Manager class (DrinkManager, FoodManager atc)
    """
    @abc.abstractmethod
    def get_available_products(self):
        """
        Get list of all products with quantity greater than 0
        """
        pass

    # @abc.abstractmethod
    # # Open the file for storing information of the number of available objects
    # def record_object_data(self, sJsonObjectData: str, sJsonFilePath: str):
    #     """
    #     Stored values which created by json.dumps() to the file json_file_path
    #     @param sJsonObjectData: object with values which created by json.dumps()
    #     @param sJsonFilePath: path to json file which you want to store in
    #     """
    #     pass
