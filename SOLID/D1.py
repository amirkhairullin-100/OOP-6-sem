from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass

class EmailSender(Notifier):
    def send(self, recipient: str, message: str):
        print(f"Email → {recipient}: {message}")

class OrderService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def place_order(self, order_id: int, email: str):
        print(f"Заказ #{order_id} оформлен")
        self.notifier.send(email, f"Ваш заказ #{order_id} принят")

notifier = EmailSender()
service = OrderService(notifier)
service.place_order(101, "user@example.com")
