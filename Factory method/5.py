from abc import ABC, abstractmethod

class Gateway(ABC):
    @abstractmethod
    def pay(self, amount: float, currency: str) -> str:
        pass

    @abstractmethod
    def refund(self, transaction_id: str) -> str:
        pass

class StripeGateway(Gateway):
    def pay(self, amount: float, currency: str) -> str:
        return f"Stripe: списано {amount} {currency}"

    def refund(self, transaction_id: str) -> str:
        return f"Stripe: возврат по транзакции {transaction_id}"

class PayPalGateway(Gateway):
    def pay(self, amount: float, currency: str) -> str:
        return f"PayPal: списано {amount} {currency}"

    def refund(self, transaction_id: str) -> str:
        return f"PayPal: возврат по транзакции {transaction_id}"

class YookassaGateway(Gateway):
    def pay(self, amount: float, currency: str) -> str:
        return f"ЮKassa: списано {amount} {currency}"

    def refund(self, transaction_id: str) -> str:
        return f"ЮKassa: возврат по транзакции {transaction_id}"

class PaymentProcessor(ABC):
    @abstractmethod
    def create_gateway(self) -> Gateway:
        pass

    def checkout(self, amount: float, currency: str = "RUB") -> str:
        gateway = self.create_gateway()
        return gateway.pay(amount, currency)

class StripeProcessor(PaymentProcessor):
    def create_gateway(self) -> Gateway:
        return StripeGateway()

class PayPalProcessor(PaymentProcessor):
    def create_gateway(self) -> Gateway:
        return PayPalGateway()

class YookassaProcessor(PaymentProcessor):
    def create_gateway(self) -> Gateway:
        return YookassaGateway()

class Shop:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount: float, currency: str = "RUB") -> str:
        return self.payment_processor.checkout(amount, currency)

shop_stripe = Shop(StripeProcessor())
print(shop_stripe.checkout(4990.0))

shop_paypal = Shop(PayPalProcessor())
print(shop_paypal.checkout(4990.0))

shop_yookassa = Shop(YookassaProcessor())
print(shop_yookassa.checkout(4990.0))