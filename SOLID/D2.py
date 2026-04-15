from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class FileLogger(Logger):
    def log(self, message: str):
        print(f"[FILE] {message}")

class UserService:
    def __init__(self, logger: Logger):
        self.logger = logger

    def register(self, username: str):
        print(f"Пользователь {username} зарегистрирован")
        self.logger.log(f"Регистрация: {username}")

    def delete(self, username: str):
        print(f"Пользователь {username} удалён")
        self.logger.log(f"Удаление: {username}")

logger = FileLogger()
service = UserService(logger)
service.register("Алексей")
service.delete("Алексей")