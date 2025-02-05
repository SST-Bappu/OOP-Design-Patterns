from abc import ABC, abstractmethod


class NotificationStrategy(ABC):
    """ Abstract strategy for each of the notification type (email, phone, whatsapp)"""
    
    @abstractmethod
    def notify(self, recipient: dict, news: str):
        pass
    
    @staticmethod
    @abstractmethod
    def required_fields():
        """ Each of the notification strategy requires different parameter to process (email for email notification, number for whatsapp).
            As a consequence, it is important to check if the observer has required parameter to call the strategy
        """
        pass
