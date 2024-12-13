import psycopg2


class DatabaseManager:
    def __init__(self, db_config: dict):
        self.db_config = db_config
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_config)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.roolback()

        if self.conn:
            self.conn.close()

        if self.cursor:
            self.cursor.close()

    def execute(self, query: str, params: tuple | None):
        self.cursor.execute(query, params)


database_config = {
    'host': 'localhost',
    'port': 5432,
    'user': 'sanjarbek',
    'password': 'sanjarbek2002',
    'database': 'n57_test'
}


def execute_query(query: str, params: tuple | None = None, fetch: str | None = None) -> list | tuple:
    try:
        with DatabaseManager(database_config) as db:
            db.execute(query=query, params=params)
            if fetch == "one":
                return db.cursor.fetchone()
            elif fetch == "all":
                return db.cursor.fetchall()
    except Exception as e:
        print(e)


try:
    query_test = """
    CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(50)
    )
    """
    execute_query(query=query_test)

except Exception as e:
    print(e)
