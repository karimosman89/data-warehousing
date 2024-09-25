import sqlite3

def create_tables():
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            amount REAL,
            date TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_tables()
