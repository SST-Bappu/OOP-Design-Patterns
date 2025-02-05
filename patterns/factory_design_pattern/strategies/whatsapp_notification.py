from patterns.factory_design_pattern.interfaces.notification_strategy import NotificationStrategy


class WhatsAppNotification(NotificationStrategy):
    """ Concrete implementation of a notification strategy"""
    
    def __init__(self, dependencies: dict):
        """initiate all the required dependencies"""
        self.key = dependencies['key']
        self.url = dependencies['url']
    
    def notify(self, recipient: str, news: str):
        print(f"{news} successfully notified to {recipient} via whatsapp")
    
    
    @staticmethod
    def required_fields() -> list[str]:
        return ['key', 'url']

