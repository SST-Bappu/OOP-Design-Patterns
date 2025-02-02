from patterns.strategy_pattern.interface.payment_strategy import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number
    
    def pay(self, amount: float):
        print(f"Paid {amount} using credit card ending in {self.card_number[-4:]}")
