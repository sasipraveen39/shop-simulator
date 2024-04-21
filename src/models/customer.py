class Customer:
    __items: dict[str, int]
    __recieved_items: dict[str, int] = {}
    __ordering_time: float = 0
    
    __waiting_start_time: float = 0
    __waiting_end_time: float = 0

    def __init__(self, items: dict[str, int], ordering_time_for_one_item: float):
        self.__items = items
        self.__ordering_time = ordering_time_for_one_item * len(items)

    def wait_in_queue(self, start_time: float):
        self.__waiting_start_time = start_time

    def leave_queue(self, end_time: float):
        self.__waiting_end_time = end_time

    def order_items(self) -> dict[str, int]:
        return self.__items

    def get_ordering_time(self) -> float:
        return self.__ordering_time
    
    def get_waiting_time(self) -> float:
        return self.__waiting_end_time - self.__waiting_start_time
    
    def make_payment(self, total_price: float) -> bool:
        return True
    
    def recieve_items(self, items: dict[str, int]):
        self.__recieved_items = items

    def provide_feedback(self) -> float:
        return 0.0