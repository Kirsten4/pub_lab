class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def can_afford_drink(self,drink):
        return self.wallet >= drink.price
        
    def buy_drink(self, drink):
        if self.can_afford_drink(drink):
            self.wallet -= drink.price 
            self.drunkenness += drink.alcohol_level

    def buy_food(self,food):
        self.drunkenness -= food.rejuvenation_level
        self.wallet -= food.price

    
    