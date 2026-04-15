from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        ...

class EmailNotifier(Notifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"Email → {recipient}: {message}")

class SMSNotifier(Notifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"SMS → {recipient}: {message}")

class PushNotifier(Notifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"Push → {recipient}: {message}")

class NotificationService:
    def __init__(self, notifier_factory):
        """
        notifier_factory: функция без параметров, создающая экземпляр Notifier
        """
        self.notifier_factory = notifier_factory

    def send(self, recipient: str, message: str) -> None:
        notifier = self.notifier_factory()
        notifier.send(recipient, message)

service_email = NotificationService(lambda: EmailNotifier())
service_email.send('user@example.com', 'Ваш заказ подтверждён')

service_sms = NotificationService(lambda: SMSNotifier())
service_sms.send('+79001234567', 'Код подтверждения: 1234')

service_push = NotificationService(lambda: PushNotifier())
service_push.send('user_device_id', 'Новое уведомление')