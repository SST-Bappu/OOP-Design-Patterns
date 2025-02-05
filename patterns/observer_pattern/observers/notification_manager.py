from patterns.observer_pattern.interfaces.notification_strategy import NotificationStrategy
from patterns.observer_pattern.interfaces.observer import Observer


class NotificationManager(Observer):
    """ Concrete observer that take control of each of notification mediums dynamically """
    
    def __init__(self, strategies: list[NotificationStrategy] = None):
        self.strategies = strategies if strategies else []
    
    def add_strategy(self, strategy: NotificationStrategy):
        """ Dynamically add a strategy """
        self.strategies.append(strategy)
    
    def remove_strategy(self, strategy: NotificationStrategy):
        """ Dynamically remove a strategy"""
        self.strategies.remove(strategy)
    
    def update(self, recipient: dict, news: str):
        """ Trigger each of the notification mediums one by one """
        for strategy in self.strategies:
            required_fields = strategy.required_fields()
            if all(field in recipient for field in required_fields):
                strategy.notify(recipient, news)
