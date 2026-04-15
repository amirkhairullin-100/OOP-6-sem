from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Input(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class LightButton(Button):
    def render(self) -> str:
        return "[Light Button]"

class LightCheckbox(Checkbox):
    def render(self) -> str:
        return "[Light Checkbox]"

class LightInput(Input):
    def render(self) -> str:
        return "[Light Input]"

class DarkButton(Button):
    def render(self) -> str:
        return "[Dark Button]"

class DarkCheckbox(Checkbox):
    def render(self) -> str:
        return "[Dark Checkbox]"

class DarkInput(Input):
    def render(self) -> str:
        return "[Dark Input]"

class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

    @abstractmethod
    def create_input(self) -> Input:
        pass

class LightThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()

    def create_input(self) -> Input:
        return LightInput()

class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()

    def create_input(self) -> Input:
        return DarkInput()

class Application:
    def __init__(self, factory: UIFactory):
        self.factory = factory

    def render_ui(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()
        input_field = self.factory.create_input()
        print(button.render(), checkbox.render(), input_field.render())

light_factory = LightThemeFactory()
dark_factory = DarkThemeFactory()

print("Светлая тема:")
app_light = Application(light_factory)
app_light.render_ui()

print("\nТёмная тема:")
app_dark = Application(dark_factory)
app_dark.render_ui()