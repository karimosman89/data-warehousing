import sqlite3
import pandas as pd

def load_data(file_path):
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()

    data = pd.read_csv(file_path)
    data.to_sql('sales', conn, if_exists='append', index=False)

    conn.commit()
    conn.close()
