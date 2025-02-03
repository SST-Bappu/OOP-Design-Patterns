from patterns.observer_pattern.interface.notification_strategy import NotificationStrategy
from patterns.observer_pattern.interface.observer import Observer


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
    
    def update(self, recipient: str, news: str):
        """ Trigger each of the notification mediums one by one """
        for strategy in self.strategies:
            strategy.notify(recipient, news)
