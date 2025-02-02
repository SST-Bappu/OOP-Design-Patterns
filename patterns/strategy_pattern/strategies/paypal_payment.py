from patterns.strategy_pattern.interface.payment_strategy import PaymentStrategy


class PaypalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float):
        print(f"Paid {amount} using email {self.email}")
