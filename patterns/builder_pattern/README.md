# 🏗️ Builder Design Pattern

## 📌 Introduction
The **Builder Pattern** is a **creational design pattern** that provides a way to construct complex objects **step-by-step** rather than using a large constructor with multiple parameters.  
It improves **readability, flexibility, and maintainability** by **separating object creation logic** from the final object itself.

---

## 🚀 Why Use the Builder Pattern?
✔ When an object **has multiple optional attributes**.  
✔ When object **creation is complex and should be done step-by-step**.  
✔ When an object **needs to be created in different configurations**.  
✔ When you want a **clean, readable, and maintainable object construction** process.  

---

## 🍔 Meal Builder Example (Burger Meal Customization)
Imagine an **online meal ordering system** where users can customize their meal **step-by-step**:  
- Choose a **burger type** (Chicken, Veggie).
- Add **a drink** (optional).
- Add **fries, cheese, or sauce** (optional).  

Instead of using a **long constructor with multiple parameters**, we use the **Builder Pattern** to structure object creation.

---

## 📂 Project Structure
```
meal_builder/
│── builders/
│   ├── meal_builder.py        # The Builder class
├── objects/
│   ├── meal.py                # The Meal (final product class)
├── main.py                     # Entry point to test MealBuilder
│── README.md                        # Documentation
│── requirements.txt                  # Dependencies (if needed)
```

---

## 🏗️ Implementation

### **1️⃣ The Final Product (`entities/meal.py`)**

```python
class Meal:
    """The final Meal object that gets constructed using the builder."""
    
    def __init__(self, burger, drink, fries, cheese, sauce):
        self.burger = burger
        self.drink = drink
        self.fries = fries
        self.cheese = cheese
        self.sauce = sauce

    def __str__(self):
        return f"Meal[Burger={self.burger}, Drink={self.drink}, Fries={self.fries}, Cheese={self.cheese}, Sauce={self.sauce}]"
```

---

### **2️⃣ The Builder Class (`builders/meal_builder.py`)**

```python
class MealBuilder:
    """Builder class to construct a meal step-by-step."""
    
    def __init__(self, burger):
        self.burger = burger
        self.drink = None
        self.fries = False
        self.cheese = False
        self.sauce = False

    def add_drink(self, drink):
        self.drink = drink
        return self

    def add_fries(self):
        self.fries = True
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_sauce(self):
        self.sauce = True
        return self

    def build(self):
        """Returns the final Meal object."""
        return Meal(self.burger, self.drink, self.fries, self.cheese, self.sauce)
```

---

### **3️⃣ Using the Builder (`main.py`)**

```python

# ✅ Creating Meal Using Builder (Step-by-Step)
meal = (
    MealBuilder("Chicken Burger")
    .add_drink("Coca-cola")
    .add_fries()
    .add_cheese()
    .build()
)

print(meal)
```

### **🔹 Output**
```
Meal[Burger=Chicken Burger, Drink=Coca-cola, Fries=True, Cheese=True, Sauce=False]
```

---

[//]: # (## ✅ Advantages of the Builder Pattern)

[//]: # (| **Aspect**          | **Without Builder ❌** | **With Builder ✅** |)

[//]: # (|-------------------|----------------|----------------|)

[//]: # (| **Readability** | `.filter&#40;&#41;.filter&#40;&#41;.filter&#40;&#41;` everywhere | `.where&#40;&#41;.or_where&#40;&#41;.build&#40;&#41;` &#40;clean chaining&#41; |)

[//]: # (| **Dynamic Queries** | Manual if-else logic | Automatically constructs filter conditions |)

[//]: # (| **Reusability** | Query logic repeated | **Reusable query builder** |)

[//]: # (| **Complex Queries** | Hard to manage AND/OR | **Handles AND/OR properly** |)








## 📌 Conclusion
✔ The **Builder Pattern** is useful when creating complex objects step-by-step.  
✔ It follows the **Single Responsibility Principle (SRP)** by **separating object creation logic**.  
✔ It improves **readability, flexibility, and testability**.  


