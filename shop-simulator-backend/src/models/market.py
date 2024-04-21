from .item import Item

class Market:
    __items: list[Item]

    def __init__(self):
        self.__items = []
    
    def get_items(self):
        return self.__items

    def get_price(self, itemName : str) -> float:
        for item in self.__items:
            if item.get_name() == itemName:
                return item.get_price()
        return -1
    
    def add_item(self, itemName: str, price: float):
        self.__items.append(Item(itemName, price))

    def buy_item(self, itemName: str, quantity: float, amount : float) -> bool:
        for item in self.__items:
            if item.get_name() == itemName:
                if item.get_price() * quantity == amount:
                    self.__items.remove(item)
                    return True
        return False