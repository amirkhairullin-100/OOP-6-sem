from abc import ABC, abstractmethod

class Finder(ABC):
    @abstractmethod
    def find(self, id: int):
        pass

class Saver(ABC):
    @abstractmethod
    def save(self, entity: dict):
        pass

class Deleter(ABC):
    @abstractmethod
    def delete(self, id: int):
        pass

class Exporter(ABC):
    @abstractmethod
    def export_csv(self) -> str:
        pass

class FullRepository(Finder, Saver, Deleter, Exporter):
    def find(self, id: int):
        return {'id': id, 'name': 'Анна'}

    def save(self, entity: dict):
        print(f"Сохранение: {entity}")

    def delete(self, id: int):
        print(f"Удаление id={id}")

    def export_csv(self) -> str:
        return "id,name\n1,Анна"

class ReadOnlyRepository(Finder, Exporter):
    def find(self, id: int):
        return {'id': id, 'name': 'Иван'}

    def export_csv(self) -> str:
        return "id,name\n1,Иван"

repo_full = FullRepository()
print(repo_full.find(1))
repo_full.save({'id': 2, 'name': 'Петя'})
print(repo_full.export_csv())

print("---")

repo_read_only = ReadOnlyRepository()
print(repo_read_only.find(1))
print(repo_read_only.export_csv())
