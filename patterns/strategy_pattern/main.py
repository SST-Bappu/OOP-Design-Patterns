from patterns.strategy_pattern.context.payment_context import PaymentContext
from patterns.strategy_pattern.strategies.credit_card import CreditCardPayment
from patterns.strategy_pattern.strategies.paypal_payment import PaypalPayment

if __name__ == '__main__':
    amount = 120.50
    
    # using credit card
    credit_card = CreditCardPayment('1234-5678-9012-3456')
    context = PaymentContext(credit_card)
    context.process_payment(amount)
    
    # using PayPal
    paypal = PaypalPayment('abc@test.com')
    context.set_strategy(paypal)
    context.process_payment(amount)
