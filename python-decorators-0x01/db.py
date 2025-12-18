import sqlite3
from contextlib import contextmanager
import uuid

DB_NAME = "users.db"


@contextmanager
def get_db_connection(db_name: str):
    conn = sqlite3.connect(db_name)
    try:
        yield conn
    finally:
        conn.close()


def setup_database(db_name: str=DB_NAME):
    with get_db_connection(db_name) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS users (
            user_id VARCHAR(20) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL
        );
        """
        cursor.execute(query)

def populate_database(db_name: str=DB_NAME):
    users = [
        (str(uuid.uuid4()), "Alice", 30),
        (str(uuid.uuid4()), "Bob", 25),
        (str(uuid.uuid4()), "Charlie", 35)
    ]
    with get_db_connection(db_name) as conn:
        cursor: sqlite3.Cursor = conn.cursor()

        cursor.executemany("INSERT INTO users (user_id, name, age) VALUES (?, ?, ?);", users)
        conn.commit()

if __name__ == "__main__":
    setup_database()
    populate_database() 

    with get_db_connection(DB_NAME) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
