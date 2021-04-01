import abc


class ProductManager(abc.ABC):
    """
    Abstract class (interface) which enforce users to implement the methods below when implementing Manager class (DrinkManager, FoodManager atc)
    """
    @abc.abstractmethod
    def get_available_data(self):
        """
        Get all objects with quantity greater than 0
        """
        pass

    @abc.abstractmethod
    # Open the file for storing information of the number of available objects
    def record_object_data(self, json_object_data: str, json_file_path: str):
        """
        Stored values which created by json.dumps() to the file json_file_path
        @param json_object_data: object with values which created by json.dumps()
        @param json_file_path: path to json file which you want to store in
        """
        pass
