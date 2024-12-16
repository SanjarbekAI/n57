from database import execute_query


def create_tables() -> bool | None:
    try:
        contacts = """
        CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        user_id BIGINT NOT NULL,
        full_name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(13) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """

        users = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        email VARCHAR(128) NOT NULL,
        password VARCHAR(128) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        is_login SMALLINT NOT NULL DEFAULT 0
        )
        """
        verification_codes = """
          CREATE TABLE IF NOT EXISTS verification_codes (
          id SERIAL PRIMARY KEY,
          email VARCHAR(128) NOT NULL,
          code SMALLINT NOT NULL,
          created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
          )
          """
        execute_query(query=users)
        execute_query(query=contacts)
        execute_query(query=verification_codes)
        return True
    except Exception as e:
        print(e)


def add_contact_query(params: tuple) -> bool | None:
    try:
        query = """
        INSERT INTO contacts (user_id, full_name, phone_number)
        VALUES (%s, %s, %s)
        """

        execute_query(query=query, params=params)
        return True
    except Exception as e:
        print(e)


def get_all_contacts(user_id: int) -> list[tuple] | None:
    try:
        query = "SELECT * FROM contacts WHERE user_id=%s"
        return execute_query(query=query, params=(user_id,), fetch="all")
    except Exception as e:
        print(e)


def get_contact(contact_id: int) -> tuple:
    try:
        query = "SELECT * FROM contacts WHERE id = %s"
        return execute_query(query=query, params=(contact_id,), fetch="one")
    except Exception as e:
        print(e)


def delete_contact_query(contact_id: int) -> bool | None:
    try:
        query = "DELETE FROM contacts WHERE id=%s"
        execute_query(query=query, params=(contact_id,))
        return True
    except Exception as e:
        print(e)


def update_contact_query(contact_id: int, new_name: str):
    try:
        query = """UPDATE contacts SET full_name=%s WHERE id=%s"""
        execute_query(query=query, params=(new_name, contact_id,))
        return True
    except Exception as e:
        print(e)
        return False


def get_user_by_email(email: str):
    try:
        query = "SELECT * FROM users WHERE email = %s"
        return execute_query(query=query, params=(email,), fetch="one")
    except Exception as e:
        print(e)


def add_user_query(params: tuple) -> bool | None:
    try:
        query = """
        INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)
        """

        execute_query(query=query, params=params)
        return True
    except Exception as e:
        print(e)


def get_user_code(email: str, code: int):
    try:
        query = "SELECT * FROM verification_codes WHERE email = %s and code = %s"
        return execute_query(query=query, params=(email, code,), fetch="one")
    except Exception as e:
        print(e)


def add_verification_code(email: str, code: int) -> bool | None:
    try:
        query = """
        INSERT INTO verification_codes (email, code) VALUES (%s, %s)
        """

        execute_query(query=query, params=(email, code,))
        return True
    except Exception as e:
        print(e)


def update_user_status(email: str, status: int):
    try:
        query = """UPDATE users SET status = %s WHERE email = %s"""
        execute_query(query=query, params=(status, email,))
        return True
    except Exception as e:
        print(e)
        return False


def update_user_is_login(email: str, is_login: int):
    try:
        query = """UPDATE users SET is_login = %s WHERE email = %s"""
        execute_query(query=query, params=(is_login, email,))
        return True
    except Exception as e:
        print(e)
        return False


def get_active_user():
    try:
        query = """SELECT * FROM users WHERE is_login=1"""
        return execute_query(query=query, fetch="one")
    except Exception as e:
        print(e)
        return False


def logout_all():
    try:
        query = """UPDATE users SET is_login=0 WHERE is_login=1"""
        execute_query(query=query)
        return True
    except Exception as e:
        print(e)
        return False
