from patterns.factory_design_pattern.interfaces.factory_strategy import FactoryStrategy
from patterns.factory_design_pattern.interfaces.notification_strategy import NotificationStrategy
from patterns.factory_design_pattern.strategies.email_notification import EmailNotification
from patterns.factory_design_pattern.strategies.whatsapp_notification import WhatsAppNotification


class NotificationFactory(FactoryStrategy):
    def __init__(self):
        self.strategies = {
            'email': EmailNotification,
            'whatsapp': WhatsAppNotification
        }
    def create_strategy(self, strategy_type: str, dependencies: dict) -> NotificationStrategy | None:
        
        strategy = self.strategies.get(strategy_type, None)
        if strategy:
            required_fields = strategy.required_fields()
            if all(field in dependencies for field in required_fields):
                return strategy(dependencies)
        return None
    
    
