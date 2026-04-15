class UserAccount:
    def __init__(self, name: str):
        self.name = name

    def get_discount(self) -> float:
        return 0.10

class PremiumAccount(UserAccount):
    def get_discount(self) -> float:
        return 0.25

class GuestAccount(UserAccount):
    def get_discount(self) -> float:
        return 0.0  # гостям скидка равна 0

def print_discounts(accounts: list[UserAccount]):
    for acc in accounts:
        print(f"{acc.name}: скидка {acc.get_discount() * 100}%")

# Вызов
accounts = [
    UserAccount("Анна"),
    PremiumAccount("Иван"),
    GuestAccount("Гость")
]
print_discounts(accounts)