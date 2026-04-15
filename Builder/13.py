class Pizza:
    def __init__(self):
        self.size = ""
        self.dough = ""
        self.sauce = ""
        self.cheese = ""
        self.toppings = []

    def __str__(self):
        toppings_str = ', '.join(self.toppings) if self.toppings else 'без топпингов'
        return (
            f"Пицца {self.size} на {self.dough} тесте\n"
            f"Соус: {self.sauce}, Сыр: {self.cheese}\n"
            f"Топпинги: {toppings_str}"
        )

class PizzaBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._pizza = Pizza()
        return self

    def set_size(self, size: str):
        self._pizza.size = size
        return self

    def set_dough(self, dough: str):
        self._pizza.dough = dough
        return self

    def set_sauce(self, sauce: str):
        self._pizza.sauce = sauce
        return self

    def set_cheese(self, cheese: str):
        self._pizza.cheese = cheese
        return self

    def add_topping(self, topping: str):
        self._pizza.toppings.append(topping)
        return self

    def build(self):
        if not self._pizza.size:
            raise ValueError("Укажите размер пиццы")
        if not self._pizza.dough:
            raise ValueError("Укажите тип теста")
        built_pizza = self._pizza
        self.reset()
        return built_pizza

class Director:
    def __init__(self, builder: PizzaBuilder):
        self._builder = builder

    def build_margherita(self):
        return (
            self._builder
                .set_size("M")
                .set_dough("традиционное")
                .set_sauce("томатный")
                .set_cheese("моцарелла")
                .add_topping("базилик")
                .build()
        )

    def build_pepperoni(self):
        return (
            self._builder
                .set_size("L")
                .set_dough("тонкое")
                .set_sauce("томатный")
                .set_cheese("моцарелла")
                .add_topping("пепперони")
                .add_topping("помидоры")
                .build()
        )

    def build_vegetarian(self):
        return (
            self._builder
                .set_size("S")
                .set_dough("традиционное")
                .set_sauce("томатный")
                .set_cheese("моцарелла")
                .add_topping("перец")
                .add_topping("грибы")
                .add_topping("лук")
                .add_topping("маслины")
                .build()
        )

if __name__ == "__main__":
    builder = PizzaBuilder()
    director = Director(builder)

    print(director.build_margherita())
    print()
    print(director.build_pepperoni())
    print()
    print(director.build_vegetarian())

    custom_pizza = (
        PizzaBuilder()
        .set_size("XL")
        .set_dough("тонкое")
        .set_sauce("сырный")
        .set_cheese("чеддер")
        .add_topping("куперсу")
        .add_topping("каперсы")
        .build()
    )
    print()
    print(custom_pizza)