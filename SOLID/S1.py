import re

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

class EmailValidator:
    def validate(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

class EmailSender:
    def send_welcome_email(self, user: User):
        print(f"Отправка письма на {user.email}: Добро пожаловать, {user.name}!")
def main():
    user = User("Алексей", "alex@example.com")
    
    validator = EmailValidator()
    if validator.validate(user.email):
        sender = EmailSender()
        sender.send_welcome_email(user)
    else:
        print("Некорректный адрес электронной почты!")

if __name__ == "__main__":
    main()