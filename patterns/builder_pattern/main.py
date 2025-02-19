from patterns.builder_pattern.builders.meal_builder import MealBuilder

if __name__=="__main__":
    meal = (
        MealBuilder('Chicken Burger')
        .add_drink('Coca-cola')
        .add_fries(True)
        .add_sauce(True)
        .build()
    )
    
    print(meal)