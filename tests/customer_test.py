import unittest
from src.drink import Drink
from src.customer import Customer
from src.food import Food


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jack", 7.50, 75, 5)
        self.drink_1 = Drink("vodka", 1.50, 1)
        self.drink_2 = Drink("cocktail", 15.00, 6)
        self.food_1 = Food("pizza",7.40,4)

    def test_customer_has_name(self):
        self.assertEqual("Jack", self.customer.name)

    def test_customer_wallet_value(self):
        self.assertEqual(7.50,self.customer.wallet)

    def test_customer_age(self):
        self.assertEqual(75, self.customer.age)

    def test_custumer_drunkenness(self):
        self.assertEqual(5, self.customer.drunkenness)

    def test_can_afford_drink__yes(self):
        self.assertEqual(True, self.customer.can_afford_drink(self.drink_1))

    def test_can_afford_drink__no(self):
        self.assertEqual(False, self.customer.can_afford_drink(self.drink_2))

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink_1)
        self.assertEqual(6.00, self.customer.wallet)
        self.assertEqual(6, self.customer.drunkenness)

    def test_buy_food(self):
        self.customer.buy_food(self.food_1)
        self.assertEqual(1, self.customer.drunkenness)
        self.assertAlmostEqual(0.10, self.customer.wallet,2)


