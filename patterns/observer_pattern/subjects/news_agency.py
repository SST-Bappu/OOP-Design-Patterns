from patterns.observer_pattern.interface.observer import Observer

class NewsAgency:
    """ This will publish news to observer (Notification Manager) """
    def __init__(self, observers: list[Observer]=None):
        self._observers = observers if observers else []
    
    def add_observer(self, observer: Observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify_observer(self):
        pass