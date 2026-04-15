from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def create_notification(self, target: str):
        pass

    def notify(self, target: str, message: str):
        notification = self.create_notification(target)
        notification.send(message)

class EmailNotifier(Notifier):
    def create_notification(self, target: str):
        return EmailNotification(target)

class SmsNotifier(Notifier):
    def create_notification(self, target: str):
        return SmsNotification(target)

class PushNotifier(Notifier):
    def create_notification(self, target: str):
        return PushNotification(target)

class EmailNotification:
    def __init__(self, address: str):
        self.address = address

    def send(self, message: str):
        print(f"Email → {self.address}: {message}")

class SmsNotification:
    def __init__(self, phone: str):
        self.phone = phone

    def send(self, message: str):
        print(f"SMS → {self.phone}: {message}")

class PushNotification:
    def __init__(self, device_token: str):
        self.device_token = device_token

    def send(self, message: str):
        print(f"Push → {self.device_token}: {message}")

notifier = EmailNotifier()
notifier.notify("user@example.com", "Ваш заказ подтверждён")

notifier = SmsNotifier()
notifier.notify("+79001234567", "Код подтверждения: 1234")

notifier = PushNotifier()
notifier.notify("device_token_123", "Новое сообщение")