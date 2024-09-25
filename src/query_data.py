import sqlite3

def query_data():
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM sales WHERE amount > 100')
    results = cursor.fetchall()

    for row in results:
        print(row)

    conn.close()
