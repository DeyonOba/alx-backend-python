import datetime as dt
import sqlite3
from functools import wraps


#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""
LOG_FILE = 'query_log.txt'

def log_queries(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query', '') or (args[0] if args else '')
        dt_now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, 'a') as f:
            f.write(f"[{dt_now}] Executing query: {query}\n")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print(list(users))