from .inventory import Inventory
from .employee import Employee
from .recipe import Recipe
from .customer import Customer

class Shop:
    __inventory : Inventory
    __employees : list[Employee]
    __recipes : list[Recipe]
    __customers_waiting_to_order : list[Customer]
    __customers_waiting_for_items : list[Customer]
    __served_customers : list[Customer]
    __cash : float = 0
    __clock : float = 0
    __shop_running_time : float = 0

    def __init__(self, inventory: Inventory, employees: list[Employee], recipes: list[Recipe]):
        self.__inventory = inventory
        self.__employees = employees
        self.__recipes = recipes
        self.__customers_waiting_to_order = []
        self.__customers_waiting_for_items = []

    def get_clock(self) -> float:
        return self.__clock

    def add_employee(self, employee: Employee):
        self.__employees.append(employee)

    def remove_employee(self, employee: Employee):
        self.__employees.remove(employee)

    def enter(self, customer: Customer):
        customer.wait_in_queue(self.get_clock())
        self.__customers_waiting_to_order.append(customer)

    def take_order(self, customer: Customer, employee: Employee):
        pass
    
    def recieve_payment(self, total_price: float):
        self.__cash += total_price

    def server_order(self, customer: Customer, employee: Employee):
        pass

    def is_open(self) -> bool:
        return self.__clock < self.__shop_running_time