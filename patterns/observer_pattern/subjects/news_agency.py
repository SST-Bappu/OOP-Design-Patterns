from patterns.observer_pattern.interface.observer import Observer


class NewsAgency:
    """ This will publish news to observer (Notification Manager) """
    
    def __init__(self, observers: list[Observer] = None):
        self._observers = observers if observers else []
    
    def add_observer(self, observer: Observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify_users(self, recipients: list[dict], news: str):
        """ Let's assume we have thousands of users (recipients) and we will notify them using via email, whatsapp, message and so on.
            In our case here, we have only one observer (notification manager). In this dynamic approach, We can add more observers dynamically
            without breaking or touching the core logic.
        """
        for observer in self._observers:
            for recipient in recipients:
                observer.update(recipient, news)
    
    def publish_news(self, recipients: list[dict], news: str):
        """ Let's perform all the tasks related to publishing news first. Once news is published, we will call notify_users method to send the notifications  """
        print("News published successfully")
        self.notify_users(recipients, news)
