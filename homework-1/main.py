"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="fegterpgoou044")
try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data/customers_data.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                cur.executemany("insert into customers values (%s, %s, %s)", reader)

            with open('north_data/employees_data.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                cur.executemany("insert into employees values (%s, %s, %s, %s, %s, %s)", reader)

            with open('north_data/orders_data.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                cur.executemany("insert into orders values (%s, %s, %s, %s, %s)", reader)
finally:
    conn.close()