import sqlite3 
import functools

DB_NAME = "users.db"
query_cache = {}


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


def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn: sqlite3.Connection, query: str):
        if query in query_cache:
            print("Fetching data from cache ...")
            return query_cache[query]
        else:
            result = func(conn, query)
            query_cache[query] = result
            print("Cached query output ...")
            return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")

print(query_cache)
