from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def query(self, sql: str) -> list:
        pass

class MySQLConnection(DatabaseConnection):
    def query(self, sql: str) -> list:
        print(f"[MySQL] Выполнение: {sql}")
        return [{'id': 1, 'name': 'Товар A'}]

class PostgreSQLConnection(DatabaseConnection):
    def query(self, sql: str) -> list:
        print(f"[PostgreSQL] Выполнение: {sql}")
        return [{'id': 2, 'name': 'Товар B'}]

class ProductRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def find_all(self) -> list:
        return self.db.query("SELECT * FROM products")

    def find_by_id(self, id: int) -> dict:
        results = self.db.query(f"SELECT * FROM products WHERE id = {id}")
        return results[0] if results else {}

mysql_conn = MySQLConnection()
repo_mysql = ProductRepository(mysql_conn)
print(repo_mysql.find_all())
print(repo_mysql.find_by_id(1))

postgres_conn = PostgreSQLConnection()
repo_postgres = ProductRepository(postgres_conn)
print(repo_postgres.find_all())
print(repo_postgres.find_by_id(2))