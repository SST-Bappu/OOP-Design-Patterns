# Observer Pattern Implementation on Top of Strategy Pattern

## 1️⃣ Observer Pattern Overview

The **Observer Pattern** is a **behavioral design pattern** where an object (called the **Subject**) maintains a list of dependents (**Observers**) and notifies them of any state changes. This pattern is useful in **event-driven systems**, such as **news broadcasting, stock price alerts, or push notifications**.

### 🔹 **How It Works**
1. The **Subject** (Observable) maintains a list of observers.
2. Observers subscribe to the subject to receive updates.
3. When the subject's state changes, all observers are **notified automatically**.

This pattern ensures a **loosely coupled system**, where the **Subject does not need to know how the Observers process the updates**.

---

## 2️⃣ Implemented Example: **News Notification System**

### **Objective**

I implemented an **Observer Pattern** for a **news notification system**, where multiple users receive notifications via **Email, SMS, or WhatsApp** whenever news is published.

### **How It Works in My Implementation**
1. The **News Agency (Subject)** publishes news and notifies observers.
2. **Notification Manager (Observer)** receives the update and sends notifications to users.
3. **Different Notification Strategies (Strategy Pattern)** handle Email, SMS, and WhatsApp notifications.
4. Users only receive notifications via the **channels they have provided (email, phone, WhatsApp)**.

### **Why We Used the Strategy Pattern?**

Instead of hardcoding **if-else conditions** to determine how users should be notified, I applied the **Strategy Pattern** to define a flexible way to handle different types of notifications.

- Each notification method (**Email, SMS, WhatsApp**) is a **separate strategy**.
- The **Notification Manager** dynamically selects the correct strategy **based on available user data**.
- This approach makes the system **highly scalable** and **easy to extend**.

---

## 3️⃣ Folder Structure

To keep the implementation modular, we organized the code into different directories:

```
observer_strategy_pattern/
│── main.py                      # Entry point to run the program
│
├── subjects/                     # NewsAgency (Subject)
│   ├── news_agency.py            # Subject (Observable)
│
├── observers/                     # Notification Manager (Previously Subscriber)
│   ├── notification_manager.py   # Manages notification strategies
│
├── strategies/                   # Concrete Notification Strategies
│   ├── email_notification.py     # Concrete Email Notification
│   ├── sms_notification.py       # Concrete SMS Notification
│   ├── whatsapp_notification.py  # Concrete WhatsApp Notification
│
├── interfaces/                   # Interfaces for Observer & Strategy
│   ├── observer.py               # Observer Interface
│   ├── notification_strategy.py  # Strategy Interface
│
└── README.md                     # Documentation
```

### **Breakdown of Each Directory**
- **subjects/** → Contains the **NewsAgency**, which is the subject (observable) that notifies observers.
- **observers/** → Contains the **NotificationManager**, which is the observer that handles notifications.
- **strategies/** → Implements the **Strategy Pattern**, defining **different types of notifications**.
- **interfaces/** → Contains **abstract interfaces** for Observer and Strategy patterns.

---

## 4️⃣ SOLID Principles Applied

This implementation follows all **5 SOLID principles**, ensuring a clean and scalable architecture.

| SOLID Principle  | How It Is Applied in Our Implementation                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **S** - Single Responsibility | Each class has a **clear, single responsibility**. The NewsAgency only publishes news, NotificationManager only processes notifications, and each strategy handles a **single type of notification** (Email, SMS, WhatsApp). |
| **O** - Open/Closed | The system is **open for extension, closed for modification**. We can add **new notification strategies** (e.g., Telegram, Push Notifications) **without modifying existing code**.                                          |
| **L** - Liskov Substitution | Each **notification strategy** (`EmailNotification`, `WhatsAppNotification`, etc.) can be replaced without modifying the core logic, thanks to **common interfaces**.                                                        |
| **I** - Interface Segregation | Each strategy **only implements what it needs**. Email strategy does not require `send_sms()`, and SMS strategy does not require `send_email()`.                                                                             |
| **D** - Dependency Inversion | High-level modules (**NotificationManager**) **depend on abstractions** (`NotificationStrategy`), not on specific implementations.                                                                                           |

---

## 5️⃣ **Why This Approach is Better?**
✅ **Decoupled Design** → The system is modular and **easy to extend**.  
✅ **Scalable** → We can **handle thousands of users** dynamically.  
✅ **No Hardcoded `if-else` Logic** → Notification strategies **define their required fields**, eliminating manual checks.  
✅ **Easy Maintenance** → **New notification types** can be added without modifying existing code.  

---

[//]: # (## 6️⃣ **Future Enhancements**)

[//]: # (1. **Database Integration** → Store user preferences in **MySQL/PostgreSQL**.  )

[//]: # (2. **Event-Driven Architecture** → Use **Celery, RabbitMQ, Kafka** for large-scale notifications.  )

[//]: # (3. **Logging & Error Handling** → Track failed notifications for reliability.  )

This Observer Pattern implementation **on top of Strategy Pattern** provides a **flexible, efficient, and maintainable** solution for real-world notification systems! 🚀
