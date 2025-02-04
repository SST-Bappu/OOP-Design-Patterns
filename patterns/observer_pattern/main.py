from patterns.observer_pattern.observers.notification_manager import NotificationManager
from patterns.observer_pattern.strategies.email_notification import EmailNotification
from patterns.observer_pattern.strategies.whatsapp_notification import WhatsAppNotification
from patterns.observer_pattern.subjects.news_agency import NewsAgency

if __name__ == "__main__":
    # recipient list, these should be retrieved from DB. Hardcoded here just to understand the pattern
    recipients = [
        {"name": "Alice", "email": "alice@example.com", "phone": "1234567890"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Charlie", "phone": "9876543210"},
        {"name": "David", "phone": "5678901234"},
        {"name": "Eve"}  # No contact info (will be ignored)
    ]
    
    # initiate the notification strategies
    email_notification = EmailNotification('test_key', 'https://test/url')
    whatsapp_notification = WhatsAppNotification('test_key', 'https://test/url')
    
    # initiate the observer (Notification Manager), it requires the list of notification strategies that we have declared above
    observer = NotificationManager([email_notification, whatsapp_notification])
    
    # initiate the subject (News Agency) to publish news.
    news_agency = NewsAgency([observer])
    
    # let's publish a news
    news_agency.publish_news(recipients, "Python 4.0 released")
    
    # let's publish another news. We only notify over email this time, not whatsapp
    observer.remove_strategy(whatsapp_notification)
    news_agency.publish_news(recipients, "We are only notifying via email")
    
    
    # Let's publish another news. We don't want to notify the users this time
    news_agency.remove_observer(observer)
    news_agency.publish_news(recipients, "We are not notifying the clients")
