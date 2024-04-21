class Item:
    __name : str
    __price : float

    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price
    
    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price