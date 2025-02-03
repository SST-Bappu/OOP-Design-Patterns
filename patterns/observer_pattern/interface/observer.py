from abc import ABC, abstractmethod


class Observer(ABC):
    """ Abstract observer interface for news agency """
    
    @abstractmethod
    def update(self, recipient: str, news: str):
        pass
