from .customer import Customer

class Employee:
    __role: str
    __wage: float
    __skill_level: float
    __time_worked: float = 0

    def __init__(self, role: str, wage: float, skill_level: float):
        self.__role = role
        self.__wage = wage
        self.__skill_level = skill_level

    def get_role(self) -> str:
        return self.__role
    
    def work(self, time: float):
        self.__time_worked += time
