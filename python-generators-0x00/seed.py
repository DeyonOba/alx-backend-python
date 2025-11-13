import pymysql
import pymysql.cursors
import uuid
import os

DB_PASSWORD = os.environ.get("DB_PASSWORD", None)
DB_PORT = int(os.environ.get("DB_PORT", 3306))
DB_USER = os.environ.get("DB_USER", "root")
DB_NAME: str = "ALX_prodev"


def connect_db() -> pymysql.connections.Connection:
    return pymysql.connect(password=DB_PASSWORD, user=DB_USER, port=DB_PORT)

def create_database(connection: pymysql.connections.Connection) -> None:
    with connection.cursor() as cursor:
        sql = f"CREATE DATABASE IF NOT EXISTS {DB_NAME};"
        cursor.execute(sql)

def connect_to_prodev() -> None:
    return pymysql.connect(password=DB_PASSWORD, user=DB_USER, port=DB_PORT, database=DB_NAME)

def create_table(connection: pymysql.connections.Connection) -> None:
    with connection.cursor() as cursor:
        sql = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            age INT NOT NULL
        );
        """
        cursor.execute(sql)

def insert_data(connection: pymysql.connections.Connection, data: str) -> None:
    with connection.cursor() as cursor:
        with open(data, "r") as fp:
            for idx, line in enumerate(fp):
                if idx == 0:
                    continue
                user_id = str(uuid.uuid4())
                name, email, age = line.strip().split(",")
                age = int(age.strip("\""))
                sql = """
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s);
                """
                cursor.execute(sql, (user_id, name, email, age))
        connection.commit()


    
if __name__ == "__main__":
    connection = connect_db()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()
            print(f"MySQL Dastabase version: {version[0]}")
            cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            print("Databases:")
            for idx, database in enumerate(databases):
                print(f"{idx+1}--{database[0]}")
            create_database(connection)
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            print("Databases:")
            for idx, database in enumerate(databases):
                print(f"{idx+1}--{database[0]}")
            with connect_to_prodev() as prodev_conn:
                with prodev_conn.cursor() as prodev_cursor:
                    prodev_cursor.execute(f"DROP TABLE IF EXISTS {DB_NAME}.user_data;")
                    create_table(prodev_conn)
                    prodev_cursor.execute(f"USE {DB_NAME};")
                    prodev_cursor.execute("SHOW TABLES;")
                    tables = prodev_cursor.fetchall()
                    print("Tables in ALX_prodev database:")
                    for idx, table in enumerate(tables):
                        print(f"{idx+1}--{table[0]}")
                    prodev_cursor.execute("DESCRIBE user_data;")
                    description = prodev_cursor.fetchall()
                    print("Description of user_data table:")
                    print("Field | Type | Null | Key | Default | Extra")
                    for row in description:
                        print(row)
                    insert_data(prodev_conn, "user_data.csv")
                    prodev_cursor.execute("SELECT * FROM user_data LIMIT 5;")
                    records = prodev_cursor.fetchall()
                    print("First 5 records in user_data table:")
                    for record in records:
                        print(record)
    print(connection)
    print(connection.open)
    # create_database(connection)


    
