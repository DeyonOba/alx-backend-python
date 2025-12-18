import sqlite3
from contextlib import contextmanager

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
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            age INTEGER NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL
        );
        """
        cursor.execute(query)

def populate_database(db_name: str=DB_NAME):
    users = [
        ("Alice", 30, "alice@gmail.com"),
        ("Bob", 25, "bob@yahoo.com"),
        ("Charlie", 35, "charlie@gmail.com")
    ]
    with get_db_connection(db_name) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("DELETE FROM users;")
        cursor.executemany("INSERT INTO users (name, age, email) VALUES (?, ?, ?);", users)
        conn.commit()

if __name__ == "__main__":
    setup_database()
    populate_database()  # Output: greet

    with get_db_connection(DB_NAME) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
