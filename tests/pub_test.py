import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink_1 = Drink("coke", 2.50, 1)
        self.drink_2 = Drink("rum",4.30,4)
        self.customer_1 = Customer("Mary", 5.60, 30, 3)
        self.customer_2 = Customer("Tammy", 10.50, 15, 0)
        self.customer_3 = Customer("Frank", 10.50, 35, 20)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till_value(self):
        self.assertEqual(100.00,self.pub.till)
    
    def test_pub_has_drinks(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_2)
        self.assertEqual({self.drink_1:1,self.drink_2:1},self.pub.drinks)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_age_check__old_enough(self):
        self.assertEqual(True, self.pub.age_check(self.customer_1))

    def test_age_check__too_young(self):
        self.assertEqual(False, self.pub.age_check(self.customer_2))

    def test_drunkenness_check__sober_enough(self):
        self.assertEqual(True, self.pub.drunkenness_check(self.customer_1))

    def test_drunkenness_check__too_drunk(self):
        self.assertEqual(False, self.pub.drunkenness_check(self.customer_3))

    def test_serve__yes(self):
        self.pub.add_drink(self.drink_1)
        self.pub.serve(self.customer_1, self.drink_1)
        self.assertEqual(102.50, self.pub.till)
        self.assertEqual(0,self.pub.drinks[self.drink_1])
        self.assertEqual(3.1, round(self.customer_1.wallet,2))

    def test_serve__no(self):
        self.pub.add_drink(self.drink_1)
        self.assertEqual("no sale", self.pub.serve(self.customer_2,self.drink_1))

    def test_stock_value(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_2)
        self.pub.stock_value()
        self.assertEqual(6.80, self.pub.stock_value())       



 

    