class Stock:
    __itemName : str
    __quantity : float = 0.0

    def __init__(self, itemName: str):
        self.__itemName = itemName

    def add_to_stock(self, itemName: str, quantity: float) -> bool:
        if itemName == self.__itemName:
            self.__quantity += quantity
            return True
        return False
    
    def remove_from_stock(self, itemName: str, quantity: float) -> bool:
        if itemName == self.__itemName and self.__quantity >= quantity:
            self.__quantity -= quantity
            return True
        return False
    
    def get_item_name(self) -> str:
        return self.__itemName
    
    def get_quantity(self) -> float:
        return self.__quantity