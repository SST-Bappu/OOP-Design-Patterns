from patterns.strategy_pattern.interface.payment_strategy import PaymentStrategy


class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        """ in case we want to switch the strategy dynamically """
        self.strategy = strategy
    
    def process_payment(self, amount: float):
        """ execute the selected payment strategy """
        self.strategy.pay(amount)
