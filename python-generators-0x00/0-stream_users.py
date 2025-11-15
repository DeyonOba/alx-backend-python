import pymysql
from seed import connect_to_prodev


def stream_users():
    """
    A generator that yields users one by one from the user_data table.8

    WARNING: This implementation is not memory efficient for large datasets.
    Because it fetches all users at once and stores them in memory.

    CHECK: Use stream_users() instead for better memory efficiency.
    REFERENCE: https://github.com/PyMySQL/PyMySQL/blob/main/pymysql/cursors.py#L43
    pymysql Cursor documentation: self._rows holds all fetched rows in memory.
    """
    connection: pymysql.connections.Connection = connect_to_prodev()
    with connection:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM user_data;"
            cursor.execute(sql)

            while True:
                user = cursor.fetchone()
                if not user:
                    break
                yield user


if __name__ == "__main__":
    for _ in range(6):
        print(next(stream_users()))