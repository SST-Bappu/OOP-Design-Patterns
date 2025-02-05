from patterns.observer_pattern.interfaces.notification_strategy import NotificationStrategy


class EmailNotification(NotificationStrategy):
    """ Concrete implementation of a notification strategy"""
    
    def __init__(self, key: str, url: str):
        """initiate all the required dependencies"""
        self.key = key
        self.url = url
    
    def notify(self, recipient: dict, news: str):
        email = recipient.get('email', None)
        if email:
            print(f"{news} successfully notified to {email} via email")
    
    @staticmethod
    def required_fields():
        return ['email']
    