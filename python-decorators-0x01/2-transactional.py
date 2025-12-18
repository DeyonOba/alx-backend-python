import sqlite3 
import functools

DB_NAME = "users.db"


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect(DB_NAME)
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper


def transactional(func):
    @functools.wraps(func)
    def wrapper(conn: sqlite3.Connection, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            raise e
    return wrapper


@with_db_connection 
@transactional 
def update_user_email(conn: sqlite3.Connection, user_id: int, new_email: str): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 


#### Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')