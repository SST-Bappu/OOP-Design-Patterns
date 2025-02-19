from patterns.builder_pattern.objects.meal import Meal


class MealBuilder:
    """ Builder class to construct meal step-by-step"""
    
    def __init__(self, burger: str):
        self.burger = burger
        self.drink = None
        self.fries = False
        self.cheese = False
        self.sauce = False
    
    def add_drink(self, drink: str):
        self.drink = drink
        return self
    
    def add_fries(self, fries: bool):
        self.fries = fries
        return self
    
    def add_sauce(self, sauce: bool):
        self.sauce = sauce
        return self
    
    def build(self):
        meal = Meal(self.burger, self.drink, self.fries, self.cheese, self.sauce)
        return meal
