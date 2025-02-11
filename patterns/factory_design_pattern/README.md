# Factory Design Pattern

## 1️⃣ Factory Pattern Overview

The **Factory Design Pattern** is a **creational design pattern** that provides an interface for creating objects **without specifying their exact class**. It helps in **encapsulating object creation logic**, making the system more flexible, scalable, and maintainable.

### 🔹 **Why Use Factory Pattern?**
- **Decouples object creation** from the main business logic.
- **Eliminates hardcoded instantiation** using `if-else` or `switch` statements.
- **Provides flexibility** in selecting different object types at runtime.
- **Makes the system open for extension** (new types can be added without modifying existing logic).

---

## 2️⃣ Implemented Example: **Notification System Using Factory Pattern**

### **Objective**

We implemented a **Factory Pattern** to dynamically create different types of notification objects (**Email, SMS, WhatsApp**) **without if-else conditions**.

### **How It Works in Our Implementation**
1. **Factory Class** is responsible for **creating notification objects dynamically**.
2. **Each Notification Strategy (Email, SMS, WhatsApp)** is a separate class implementing a common interface.
3. **Notification Manager** uses the Factory to get the required strategy based on user input.
4. **Recipients list follows a structured format**, where each user has:
   - A `contact_type` (email, phone, WhatsApp).
   - A `contact` field with the relevant email or phone number.
5. The Factory **eliminates the need for if-else conditions** by using a **mapping approach**.

---

## 3️⃣ Folder Structure

To maintain a clean and scalable architecture, the files are structured as follows:

```
factory_pattern_example/
│── main.py                      # Entry point to run the program
│
├── factories/                    # Factory Class for object creation
│   ├── notification_factory.py   # Dynamically creates notification strategies
│
├── strategies/                   # Concrete Notification Strategies
│   ├── email_notification.py     # Concrete Email Notification
│   ├── sms_notification.py       # Concrete SMS Notification
│   ├── whatsapp_notification.py  # Concrete WhatsApp Notification
│
├── interfaces/                   # Interfaces for Strategy Pattern
│   ├── notification_strategy.py  # Strategy Interface
│
└── README.md                     # Documentation
```

### **Breakdown of Each Directory**
- **factories/** → Contains the **Factory Class** that creates notification objects dynamically.
- **strategies/** → Implements the **Strategy Pattern**, defining different notification types.
- **interfaces/** → Contains **abstract interfaces** for defining notification strategies.

---

## 4️⃣ SOLID Principles Applied

This implementation follows multiple **SOLID principles**, making the architecture robust and scalable.

| SOLID Principle  | How It Is Applied in Our Implementation |
|------------------|----------------------------------------|
| **S** - Single Responsibility | The Factory is **only responsible for object creation**, while the Notification Strategies handle notifications independently. |
| **O** - Open/Closed | The Factory Pattern allows adding **new notification types** (e.g., Telegram, Push Notifications) **without modifying existing logic**. |
| **L** - Liskov Substitution | Each **notification strategy** (`EmailNotification`, `SMSNotification`, etc.) can be used interchangeably without breaking the system. |
| **I** - Interface Segregation | The Notification Strategies **only implement the necessary methods**, avoiding unnecessary dependencies. |
| **D** - Dependency Inversion | The Notification Manager **depends on the Factory interface**, not on concrete implementations. |

---

## 5️⃣ **Why This Approach is Better?**
✅ **No Hardcoded `if-else` Logic** → The Factory dynamically selects the correct strategy.  
✅ **More Scalable & Maintainable** → Easily add new notification types.  
✅ **Decouples Object Creation from Business Logic** → Notification Manager does not need to know how strategies are instantiated.  
✅ **Efficient Runtime Selection** → Objects are **only created when needed**, improving performance.  

---

[//]: # (## 6️⃣ **Future Enhancements**)

[//]: # (1. **Database Integration** → Store user preferences in **MySQL/PostgreSQL**.  )

[//]: # (2. **Event-Driven Architecture** → Use **Celery, RabbitMQ, Kafka** for large-scale notifications.  )

[//]: # (3. **Logging & Error Handling** → Track failed notifications and retry mechanisms.  )

[//]: # ()
[//]: # (This Factory Pattern implementation ensures a **flexible, dynamic, and maintainable notification system**! 🚀)
