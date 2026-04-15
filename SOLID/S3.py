class Logger:
    def log(self, message: str):
        print(f"[LOG] {message}")

class Order:
    def __init__(self, logger: Logger):
        self.items = []
        self.logger = logger

    def add_item(self, name: str, price: float, qty: int):
        self.items.append({'name': name, 'price': price, 'qty': qty})
        self.logger.log(f"Добавлен товар: {name}, кол-во: {qty}")

    def get_total(self) -> float:
        total = sum(i['price'] * i['qty'] for i in self.items)
        self.logger.log(f"Подсчёт итога: {total}")
        return total
        
logger = Logger()
order = Order(logger)
order.add_item("Книга", 350.0, 2)
order.add_item("Ручка", 50.0, 5)
print(f"Итого: {order.get_total()}")