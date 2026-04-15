from abc import ABC, abstractmethod

class Toast(ABC):
    @abstractmethod
    def show(self, message: str) -> None:
        pass

class Dialog(ABC):
    @abstractmethod
    def show(self, title: str, body: str, buttons: list[str]) -> None:
        pass

class ProgressBar(ABC):
    @abstractmethod
    def show(self, label: str, value: int) -> None:
        pass

class IOSToast(Toast):
    def show(self, message: str) -> None:
        print(f"[iOS Toast]: {message}")

class IOSDialog(Dialog):
    def show(self, title: str, body: str, buttons: list[str]) -> None:
        print(f"[iOS Dialog]: {title}\n{body}\nButtons: {', '.join(buttons)}")

class IOSProgressBar(ProgressBar):
    def show(self, label: str, value: int) -> None:
        print(f"[iOS ProgressBar]: {label} - {value}%")

class AndroidToast(Toast):
    def show(self, message: str) -> None:
        print(f"[Android Toast]: {message}")

class AndroidDialog(Dialog):
    def show(self, title: str, body: str, buttons: list[str]) -> None:
        print(f"[Android Dialog]: {title}\n{body}\nButtons: {', '.join(buttons)}")

class AndroidProgressBar(ProgressBar):
    def show(self, label: str, value: int) -> None:
        print(f"[Android ProgressBar]: {label} - {value}%")

class NotificationFactory(ABC):
    @abstractmethod
    def create_toast(self) -> Toast:
        pass

    @abstractmethod
    def create_dialog(self) -> Dialog:
        pass

    @abstractmethod
    def create_progress_bar(self) -> ProgressBar:
        pass

class IOSFactory(NotificationFactory):
    def create_toast(self) -> Toast:
        return IOSToast()

    def create_dialog(self) -> Dialog:
        return IOSDialog()

    def create_progress_bar(self) -> ProgressBar:
        return IOSProgressBar()

class AndroidFactory(NotificationFactory):
    def create_toast(self) -> Toast:
        return AndroidToast()

    def create_dialog(self) -> Dialog:
        return AndroidDialog()

    def create_progress_bar(self) -> ProgressBar:
        return AndroidProgressBar()

def show_upload_progress(factory: NotificationFactory, filename: str, progress: int):
    toast = factory.create_toast()
    bar = factory.create_progress_bar()

    toast.show(f"Загрузка {filename} начата")
    bar.show("Прогресс загрузки", progress)

    if progress == 100:
        dialog = factory.create_dialog()
        dialog.show("Готово", f"{filename} успешно загружен", ["OK"])

if __name__ == "__main__":
    platform = "iOS"  # Или "Android"

    if platform == "iOS":
        factory = IOSFactory()
    else:
        factory = AndroidFactory()

    for progress in [0, 50, 100]:
        show_upload_progress(factory, "файл.zip", progress)