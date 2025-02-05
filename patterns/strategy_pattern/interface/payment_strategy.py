from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    """ Abstract strategy class to define the interfaces for payment methods """
    
    @abstractmethod
    def pay(self, amount: float):
        pass
