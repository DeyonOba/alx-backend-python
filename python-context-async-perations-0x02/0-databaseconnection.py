import sqlite3

db_name = "users.db"


def setup_database(conn: sqlite3.Connection):
    setup_db_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        age INTEGER NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    );
    """
    populate_table_query = """
    INSERT OR IGNORE INTO users (name, age, email)
    VALUES (?, ?, ?);
    """

    dummy_users = [
        ("John", 20, "john@gmail.com"),
        ("Alice", 30, "alice@yahoo.com"),
        ("Bob", 40, "bob@gmail.com")
    ]

    with conn:
        cursor = conn.cursor()
        cursor.execute(setup_db_query)
        cursor.executemany(populate_table_query, dummy_users)


class DatabaseConnection:
    def __init__(self, database: str):
        self.database = database
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.database)
        return self.conn
    
    def __exit__(self, type, value, traceback):
        print('Closing database connection ...')
        self.conn.close()
        return False


if __name__ == "__main__":
    with DatabaseConnection(db_name) as conn:
        setup_database(conn)
        cursor = conn.cursor()
        users = cursor.execute("SELECT * FROM users;")
        for user in users:
            print(user)
