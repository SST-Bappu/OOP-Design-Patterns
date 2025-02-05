from patterns.factory_design_pattern.factories.notification_factory import NotificationFactory

if __name__ == "__main__":
    def main():
        dependencies = {
            "key": "test_key",
            "url": "https://test/url"
        }
        
        # initiate the notification factory
        notification_factory = NotificationFactory()
        
        # create strategies
        strategies = {}
        for strategy_type in ('email', 'whatsapp'):
            strategies[strategy_type] = notification_factory.create_strategy(strategy_type, dependencies)
        recipients = [
            {"name": "Alice", "contact_type": "email", "contact": "alice@example.com"},
            {"name": "Bob", "contact_type": "email", "contact": "bob@example.com"},
            {"name": "Charlie", "contact_type": "whatsapp", "contact": "9876543210"},
            {"name": "David", "contact_type": "email", "contact": "david@example.com"},
            {"name": "Eve", "contact_type": "whatsapp", "contact": "1122334455"},
            {"name": "Frank", "contact_type": "whatsapp", "contact": "9998887777"}
        ]
        
        for recipient in recipients:
            strategy = strategies[recipient['contact_type']]
            if strategy:
                strategy.notify(recipient['contact'], "Here are some exciting news")
    
    main()