from patterns.observer_pattern.interface.notification_strategy import NotificationStrategy


class WhatsAppNotification(NotificationStrategy):
    """ Concrete implementation of a notification strategy"""
    
    def __init__(self, key: str, url: str):
        """initiate all the required dependencies"""
        self.key = key
        self.url = url
    
    def notify(self, recipient: dict, news: str):
        phone = recipient.get('phone', None)
        if phone:
            print(f"{news} successfully notified to {phone} via whatsapp")
    
    @staticmethod
    def required_fields():
        return ["phone"]
