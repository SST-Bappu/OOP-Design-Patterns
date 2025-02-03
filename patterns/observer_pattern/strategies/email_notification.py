from patterns.observer_pattern.interface.notification_strategy import NotificationStrategy


class EmailNotification(NotificationStrategy):
    """ Concrete implementation of a notification strategy"""
    
    def __init__(self, key: str, url: str):
        """initiate all the required dependencies"""
        self.key = key
        self.url = url
    
    def notify(self, recipient: str, news: str):
        print(f"{news} successfully notified to {recipient} via email")
