class Recipe:
    __name: str
    __ingreditents: dict[str, int]
    __price: float
    __preparation_time: float
    __skill_level: float

    def __init__(self, name: str, ingredients: dict[str, int], price: float, preparation_time: float, skill_level: float):
        self.__name = name
        self.__ingreditents = ingredients
        self.__price = price
        self.__preparation_time = preparation_time
        self.__skill_level = skill_level

    def get_price(self) -> float:
        return self.__price
    
    def get_name(self) -> str:
        return self.__name
    
    def get_ingredients(self) -> dict[str, int]:
        return self.__ingreditents
    
    def get_preparation_time(self) -> float:
        return self.__preparation_time
    
    def get_skill_level(self) -> float:
        return self.__skill_level