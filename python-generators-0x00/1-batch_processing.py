import pymysql
from seed import connect_to_prodev


def stream_users_in_batches(batch_size):
    connection: pymysql.connections.Connection = connect_to_prodev()
    with connection:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM user_data;"
            cursor.execute(sql)
            while True:
                users = cursor.fetchmany(batch_size)
                if not users:
                    break
                yield users

def batch_processing(batch_size):
    connection: pymysql.connections.Connection = connect_to_prodev()
    with connection:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM user_data WHERE age > 25"
            cursor.execute(sql)
            while True:
                users = cursor.fetchmany(batch_size)
                if not users:
                    break
                yield users


if __name__ == "__main__":
    from pprint import PrettyPrinter

    pprint = PrettyPrinter(indent=2)

    for idx, users in enumerate(stream_users_in_batches(2)):
        print(f"Batch: <{idx+1}>")
        pprint.pprint(users)
        print(end="\n\n")
        if idx==4:
            break

    for idx, users in enumerate(batch_processing(2)):
        print(f"Batch: <{idx+1}>")
        pprint.pprint(users)
        print(end="\n\n")
        if idx==4:
            break
