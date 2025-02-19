class Meal:
    """ The final meal object to be constructed using the builder"""
    
    def __init__(self, burger: str, drink: str, fries: bool, cheese: bool, sauce: bool):
        self.burger = burger
        self.drink = drink
        self.fries = fries
        self.cheese = cheese
        self.sauce = sauce
    
    def __str__(self):
        return f"Meal[Burger={self.burger}, Drink={self.drink}, Fries={self.fries}, Cheese={self.cheese}, Sauce={self.sauce}]"
