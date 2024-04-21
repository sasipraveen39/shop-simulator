import unittest
from src.models.recipe import Recipe

class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.ingredients = {"flour": 500, "sugar": 200, "eggs": 3}
        self.recipe = Recipe("Test Recipe", self.ingredients, price=15.0, preparation_time=30.0, skill_level=2.0)

    def tearDown(self):
        del self.recipe

    def test_get_price(self):
        self.assertEqual(self.recipe.get_price(), 15.0, "The price of the recipe is not returned correctly")

if __name__ == '__main__':
    unittest.main()