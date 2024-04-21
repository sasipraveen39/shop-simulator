import unittest
from src.models.inventory import Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()

    def test_add_item(self):
        self.assertTrue(self.inventory.add_item('Apple', 10))
        self.assertEqual(self.inventory.list_stock(), [{'Apple': 10}])

    def test_add_item_existing(self):
        self.inventory.add_item('Apple', 10)
        self.assertTrue(self.inventory.add_item('Apple', 5))
        self.assertEqual(self.inventory.list_stock(), [{'Apple': 15}])

    def test_use_item(self):
        self.inventory.add_item('Apple', 10)
        self.assertTrue(self.inventory.use_item('Apple', 5))
        self.assertEqual(self.inventory.list_stock(), [{'Apple': 5}])

    def test_use_item_non_existing(self):
        self.assertFalse(self.inventory.use_item('Orange', 5))
        self.assertEqual(self.inventory.list_stock(), [])

    def test_use_item_insufficient_quantity(self):
        self.inventory.add_item('Apple', 10)
        self.assertFalse(self.inventory.use_item('Apple', 15))
        self.assertEqual(self.inventory.list_stock(), [{'Apple': 10}])

    def test_list_stock(self):
        self.inventory.add_item('Apple', 10)
        self.inventory.add_item('Orange', 20)
        self.assertEqual(self.inventory.list_stock(), [{'Apple': 10}, {'Orange': 20}])

if __name__ == '__main__':
    unittest.main()