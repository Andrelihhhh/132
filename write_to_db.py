# danilov
# danilov
# Домашнее задание №6

import sqlite3
import pandas as pd

# Загрузка датасета (если ещё не загружен)
FILE_ID = "1j7ZAFLYStESJoCrkH0-bLctoxV75djUf"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"
df = pd.read_csv(file_url)

# Подключение к SQLite-файлу creds.db
conn = sqlite3.connect('creds.db')
cursor = conn.cursor()

# Получение учётных данных (предположим, что они в таблице creds)
cursor.execute("SELECT host, database, user, password FROM creds WHERE id = 1")
creds = cursor.fetchone()
db_host = creds[0]
db_name = creds[1]
db_user = creds[2]
db_password = creds[3]

conn.close()

import psycopg2

# Подключение к PostgreSQL
try:
    conn_pg = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=5432  # если порт другой — уточни в чате
    )
    print(" Подключение к PostgreSQL успешно")
except Exception as e:
    print(f" Ошибка подключения: {e}")
    exit(1)

table_name = "danilov"

# Создание таблицы (если её нет)
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    Customer_ID TEXT,
    Product_ID TEXT,
    Transaction_ID TEXT,
    Purchase_Frequency INTEGER,
    Average_Order_Value REAL,
    Most_Frequent_Category TEXT,
    Time_Between_Purchases INTEGER,
    Region TEXT,
    Churn_Probability REAL,
    Lifetime_Value REAL,
    Launch_Date DATE,
    Peak_Sales_Date DATE,
    Season TEXT,
    Preferred_Purchase_Times TEXT,
    Retention_Strategy TEXT
);
"""

cursor_pg = conn_pg.cursor()
cursor_pg.execute(create_table_query)
conn_pg.commit()

print(f" Таблица '{table_name}' создана или уже существует")

# Запись данных (максимум 100 строк)
df_to_write = df.head(100)  # берем первые 100 строк

for _, row in df_to_write.iterrows():
    insert_query = f"""
    INSERT INTO {table_name} VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
    """
    cursor_pg.execute(insert_query, tuple(row))

conn_pg.commit()
print(f" Записано {len(df_to_write)} строк в таблицу '{table_name}'")