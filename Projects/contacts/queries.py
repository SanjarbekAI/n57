from database import execute_query


def create_tables() -> bool | None:
    try:
        contacts = """
        CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(13) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
        execute_query(query=contacts)
        return True
    except Exception as e:
        print(e)


def add_contact_query(params: tuple) -> bool | None:
    try:
        query = """
        INSERT INTO contacts (full_name, phone_number)
        VALUES (%s, %s)
        """

        execute_query(query=query, params=params)
        return True
    except Exception as e:
        print(e)
