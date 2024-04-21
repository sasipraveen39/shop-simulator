import unittest
from src.models.item import Item

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item("Test Item", 10.0)

    def tearDown(self):
        del self.item

    def test_get_name(self):
        self.assertEqual(self.item.get_name(), "Test Item", "The name of the item is not returned correctly")

    def test_get_price(self):
        self.assertEqual(self.item.get_price(), 10.0, "The price of the item is not returned correctly")

if __name__ == '__main__':
    unittest.main()