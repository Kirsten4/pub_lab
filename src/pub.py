class Pub:
    
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = {}
        
    def add_drink(self,drink):
        if drink in self.drinks:
            self.drinks[drink] += 1
        else:
            self.drinks[drink] = 1

    def increase_till(self, amount):
        self.till += amount

    def age_check(self,customer):
        return customer.age >= 18

    def drunkenness_check(self,customer):
        return customer.drunkenness < 12

    def serve(self, customer, drink):
        if self.age_check(customer) and self.drunkenness_check(customer):
            self.increase_till(drink.price)
            self.drinks[drink] -= 1
            customer.buy_drink(drink)
        else: 
            return "no sale"

    def stock_value(self):
        total = 0
        for drink in self.drinks:
            total += (drink.price * self.drinks[drink])
        return total