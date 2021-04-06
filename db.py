import sqlite3

con = None
cur = None

def open_db():
    global con
    global cur 
    con = sqlite3.connect('WaifuBattler.db')
    cur = con.cursor()

def init_db():
    if cur is not None:
        with open('schema.sql', 'r', encoding='utf-8') as schema_file:
            cur.executescript(schema_file.read())

def close_db():
    con.close()

def exec_sql(sql):
    if cur is not None:
        cur.execute(sql)
        return cur.fetchall()

def read_source(source_name):
    'select'

def create_source(source_name):


def create_waifu(name, age, source):
    pass