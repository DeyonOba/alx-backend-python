# TASKS

## 0. Logging database Queries

**Objective**: create a decorator that logs database queries executed by any function

**Instructions**:

- Complete the code below by writing a decorator log_queries that logs the SQL query before executing it.

- **Prototype**: `def log_queries()`

## 1. Handle Database Connections with a Decorator

**Objective**: create a decorator that automatically handles opening and closing database connections

**Instructions**:

- Complete the script below by Implementing a decorator with_db_connection that opens a database connection, passes it to the function and closes it afterword

**Objective**: create a decorator that manages database transactions by automatically committing or rolling back changes


## 2. Transaction Management Decorator

**Instructions**:

- Complete the script below by writing a decorator transactional(func) that ensures a function running a database operation is wrapped inside a transaction.If the function raises an error, rollback; otherwise commit the transaction.

- Copy the `with_db_connection` created in the previous task into the script
