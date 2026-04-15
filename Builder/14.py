class SelectQueryBuilder:
    def __init__(self):
        self._select_fields = []
        self._table = ""
        self._joins = []
        self._where_conditions = []
        self._order_by = ""
        self._limit = None
        self._offset = None

    def select(self, *fields):
        if fields:
            self._select_fields.extend(fields)
        return self

    def from_table(self, table_name: str):
        self._table = table_name
        return self

    def join(self, table: str, on_condition: str):
        self._joins.append(f"JOIN {table} ON {on_condition}")
        return self

    def where(self, condition: str):
        self._where_conditions.append(condition)
        return self

    def order_by(self, column: str, direction: str = "ASC"):
        self._order_by = f"{column} {direction}"
        return self

    def limit(self, count: int):
        self._limit = count
        return self

    def offset(self, count: int):
        self._offset = count
        return self

    def build(self) -> str:
        query_parts = []

        select_clause = (
            "SELECT " + (", ".join(self._select_fields) if self._select_fields else "*")
        )
        query_parts.append(select_clause)

        if not self._table:
            raise ValueError("Таблица не указана. Используйте from_table().")
        query_parts.append(f"FROM {self._table}")

        if self._joins:
            query_parts.extend(self._joins)

        if self._where_conditions:
            query_parts.append("WHERE " + " AND ".join(self._where_conditions))

        if self._order_by:
            query_parts.append(f"ORDER BY {self._order_by}")

        if self._limit is not None:
            query_parts.append(f"LIMIT {self._limit}")

        if self._offset is not None:
            query_parts.append(f"OFFSET {self._offset}")

        return "\n".join(query_parts)

if __name__ == "__main__":
    sql = (
        SelectQueryBuilder()
        .from_table("orders")
        .select("id", "total", "status")
        .join("users", "orders.user_id = users.id")
        .where("status = 'new'")
        .where("total > 1000")
        .order_by("created_at", "DESC")
        .limit(10)
        .offset(20)
        .build()
    )

    print(sql)

    sql_min = SelectQueryBuilder().from_table("products").build()
    print("\n" + sql_min)