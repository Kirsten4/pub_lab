import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food("burger",6.25,2)

    def test_food_has_name(self):
        self.assertEqual("burger", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(6.25,self.food.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(2,self.food.rejuvenation_level)