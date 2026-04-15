from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def query(self, sql: str) -> list:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

class MySQLConnection(DatabaseConnection):
    def connect(self) -> None:
        print("Подключение к MySQL установленo.")
    def query(self, sql: str) -> list:
        print(f"Запрос к MySQL: {sql}")
        return [{"id": 1, "status": "new"}]
    def disconnect(self) -> None:
        print("Отключение от MySQL.")

class PostgreSQLConnection(DatabaseConnection):
    def connect(self) -> None:
        print("Подключение к PostgreSQL установлено.")
    def query(self, sql: str) -> list:
        print(f"Запрос к PostgreSQL: {sql}")
        return [{"id": 2, "status": "new"}]
    def disconnect(self) -> None:
        print("Отключение от PostgreSQL.")

class SQLiteConnection(DatabaseConnection):
    def connect(self) -> None:
        print("Подключение к SQLite установлено.")
    def query(self, sql: str) -> list:
        print(f"Запрос к SQLite: {sql}")
        return [{"id": 3, "status": "new"}]
    def disconnect(self) -> None:
        print("Отключение от SQLite.")

class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        pass

class MySQLFactory(DatabaseFactory):
    def create_connection(self) -> DatabaseConnection:
        return MySQLConnection()

class PostgreSQLFactory(DatabaseFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()

class SQLiteFactory(DatabaseFactory):
    def create_connection(self) -> DatabaseConnection:
        return SQLiteConnection()

def run_report(factory: DatabaseFactory):
    conn = factory.create_connection()
    conn.connect()
    results = conn.query("SELECT * FROM orders WHERE status = 'new'")
    conn.disconnect()
    return results

if __name__ == "__main__":
    for factory in [MySQLFactory(), PostgreSQLFactory(), SQLiteFactory()]:
        results = run_report(factory)
        print(f"Результаты: {results}\n")