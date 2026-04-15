from abc import ABC, abstractmethod
from typing import Protocol

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        ...

class CardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Оплата картой: {amount} руб.")

class CryptoPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Оплата криптовалютой: {amount} руб.")

class SBPPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Оплата через СБП: {amount} руб.")

class PaymentProcessor:
    def __init__(self, payment_factory):
        """
        payment_factory: функция без параметров, возвращающая экземпляр PaymentMethod
        """
        self.payment_factory = payment_factory

    def pay(self, amount: float) -> None:
        method = self.payment_factory()
        method.pay(amount)

processor_card = PaymentProcessor(lambda: CardPayment())
processor_card.pay(1500.0)

processor_crypto = PaymentProcessor(lambda: CryptoPayment())
processor_crypto.pay(3200.0)

processor_sbP = PaymentProcessor(lambda: SBPPayment())
processor_sbP.pay(2100.0)