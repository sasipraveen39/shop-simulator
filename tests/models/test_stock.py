import unittest
from src.models.stock import Stock

class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = Stock('Apple')

    def test_add_to_stock(self):
        self.assertTrue(self.stock.add_to_stock('Apple', 10))
        self.assertEqual(self.stock.get_quantity(), 10)

    def test_add_to_stock_wrong_item(self):
        self.assertFalse(self.stock.add_to_stock('Orange', 10))
        self.assertEqual(self.stock.get_quantity(), 0)

    def test_remove_from_stock(self):
        self.stock.add_to_stock('Apple', 10)
        self.assertTrue(self.stock.remove_from_stock('Apple', 5))
        self.assertEqual(self.stock.get_quantity(), 5)

    def test_remove_from_stock_wrong_item(self):
        self.stock.add_to_stock('Apple', 10)
        self.assertFalse(self.stock.remove_from_stock('Orange', 5))
        self.assertEqual(self.stock.get_quantity(), 10)

    def test_remove_from_stock_insufficient_quantity(self):
        self.stock.add_to_stock('Apple', 10)
        self.assertFalse(self.stock.remove_from_stock('Apple', 15))
        self.assertEqual(self.stock.get_quantity(), 10)

    def test_get_item_name(self):
        self.assertEqual(self.stock.get_item_name(), 'Apple')

    def test_get_quantity(self):
        self.assertEqual(self.stock.get_quantity(), 0)

if __name__ == '__main__':
    unittest.main()