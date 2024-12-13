import psycopg2


class DatabaseManager:
    def __init__(self, db_config: dict):
        self.conn = None
        self.cursor = None
        self.db_config = db_config

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            return self
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()

        if self.conn:
            self.conn.close()

        if self.cursor:
            self.cursor.close()

    def execute(self, query: str, params: tuple | None = None) -> None:
        self.cursor.execute(query, params)


database_config = {
    "host": "localhost",
    "database": "n57",
    "user": "sanjarbek",
    "password": "sanjarbek2002",
    "port": 5432
}


def execute_query(query: str, params: tuple | None = None, fetch: str | None = None) -> list | tuple | None:
    with DatabaseManager(db_config=database_config) as db:
        db.execute(query=query, params=params)
        if fetch == "one":
            return db.cursor.fetchone()
        elif fetch == "all":
            return db.cursor.fetchall()


try:
    query_str = """
    CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(50)
    )
    """
    execute_query(query=query_str)
    print("Table created successfully")
except Exception as e:
    print(e)
