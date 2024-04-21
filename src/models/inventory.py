from .stock import Stock

class Inventory:
    __stock : dict

    def __init__(self):
        self.__stock = {}
    
    def add_item(self, itemName: str, quantity: float) -> bool:
        if itemName in self.__stock:
            return self.__stock[itemName].add_to_stock(itemName, quantity)
        self.__stock[itemName] = Stock(itemName)
        return self.__stock[itemName].add_to_stock(itemName, quantity)
    
    def use_item(self, itemName: str, quantity: float) -> bool:
        if itemName in self.__stock:
            return self.__stock[itemName].remove_from_stock(itemName, quantity)
        return False
    
    def list_stock(self) -> dict:
        return [{stock.get_item_name(): stock.get_quantity()} for stock in self.__stock.values()]