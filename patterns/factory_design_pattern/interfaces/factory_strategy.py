from abc import ABC, abstractmethod

from patterns.factory_design_pattern.interfaces.notification_strategy import NotificationStrategy


class FactoryStrategy(ABC):
    @abstractmethod
    def create_strategy(self, strategy_type: str, dependencies: dict) -> NotificationStrategy | None:
        pass
    
