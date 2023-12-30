import sqlite3

def get_db_connection(app):
    connection = sqlite3.connect("students.db", check_same_thread=False)
    create_tables(connection, app)
    connection.row_factory = sqlite3.Row
    return connection

def create_tables(connection, app):
    with connection:
        with app.open_resource('schema.sql', mode='r') as f:
            connection.executescript(f.read())
