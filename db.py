import sqlite3

con = None
cur = None

def open_db():
    con = sqlite3.connect('WaifuBattler.db')
    cur = con.cursor()

def init_db():
    if cur is not None:
        with open('schema.sql', 'r', encoding='utf-8') as schema_file:
            cur.executescript(schema_file.read())

def close_db():
    con.close()