import sqlite3

con = None
cur = None

queries = {
    'source': {
        'create': 'insert into Source (nameSource) values (?)',
        'read': 'select nameSource from Source where nameSource like ?',
        'readall': 'select nameSource from Source'
    }
}


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


def read_source(source_name):
    if cur is not None:
        if source_name is not None:
            cur.execute(queries['source']['read'], (source_name,))
            return cur.fetchall()
        else:
            cur.execute(queries['source']['readall'])
            return cur.fetchall()

def create_source(source_name):
    if cur is not None:
        cur.execute(queries['source']['create'], (source_name,))
        cur.execute(queries['source']['read'], (source_name,))
        con.commit()
        return cur.fetchone()

def create_waifu(name, age, source):
    if cur is not None:
        pass
    pass