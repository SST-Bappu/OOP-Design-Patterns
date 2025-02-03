from abc import ABC, abstractmethod


class NotificationStrategy(ABC):
    """ Abstract strategy for each of the notification type (email, phone, whatsapp)"""
    
    @abstractmethod
    def notify(self, recipient: str, news: str):
        pass
