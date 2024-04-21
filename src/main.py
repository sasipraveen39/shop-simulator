# Import necessary modules
from models.item import Item
from models.inventory import Inventory

# Define main function
def main():
    item1 = Item("apple", 1.0)
    item2 = Item("banana", 0.5)
    item3 = Item("orange", 1.5)

    inventory = Inventory()
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)

    item4 = Item("apple", 1.0)

    inventory.remove_item(item4)

    print(inventory.get_items())

# Check if the script is being run directly
if __name__ == "__main__":
    main()
