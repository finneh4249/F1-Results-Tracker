import sqlite3
import datetime
from time import sleep

db = "./structures/db/history.db"

# Create the table if it doesn't exist


def create_table():
    try:
        with sqlite3.connect(db) as conn:
            cur = conn.cursor()
            cur.execute(
                f"CREATE TABLE IF NOT EXISTS searches (search TEXT, date TIMESTAMP)")
            conn.commit()
    except sqlite3.Error as e:
        print(e)

# Add a search to the database


def add_search(search):
    try:
        with sqlite3.connect(db) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO searches VALUES (?,?)",
                        (search, datetime.datetime.now()))
            conn.commit()
    except sqlite3.Error as e:
        print(e)

# Get the search history from the database


def get_searches():
    try:
        with sqlite3.connect(db) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM searches")
            return cur.fetchall()
    except sqlite3.Error as e:
        print(e)


create_table()
