from abc import ABC, abstractmethod


class Observer(ABC):
    """ Abstract observer interfaces for news agency """
    
    @abstractmethod
    def update(self, recipient: dict, news: str):
        pass
