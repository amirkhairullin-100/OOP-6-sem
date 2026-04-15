from abc import ABC, abstractmethod

class ReadableStorage(ABC):
    @abstractmethod
    def read(self, key: str) -> str:
        pass

class WritableStorage(ReadableStorage):
    @abstractmethod
    def write(self, key: str, value: str):
        pass

class Storage(WritableStorage):
    def __init__(self):
        self.data = {}

    def read(self, key: str) -> str:
        return self.data.get(key, "")

    def write(self, key: str, value: str):
        self.data[key] = value
        print(f"Запись: {key} = {value}")

class ReadOnlyStorage(ReadableStorage):
    def __init__(self, initial_data: dict):
        self.data = initial_data

    def read(self, key: str) -> str:
        return self.data.get(key, "")

def save_data(storage: WritableStorage, key: str, value: str):
    storage.write(key, value)
    print(f"Ключ '{key}' после записи: {storage.read(key)}")

storage = Storage()
save_data(storage, "user", "Алексей")  # успешно

print()

readonly_storage = ReadOnlyStorage({"user": "Борис"})