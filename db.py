import sqlite3

con = None
cur = None

queries = {
    'source': {
        'create': 'insert into Source (nameSource, aliasSource) values (?)',
        'read': 'select nameSource from Source where nameSource like ?',
        'readall': 'select nameSource from Source'
    },
    'waifu': {
        'create': 'insert into Waifu (nameWaifu, nickWaifu, tierWaifu, imageURLWaifu) values (?, ?, ?, ?)',
        'read': 'select * from Waifu inner join Source S on S.idSource = Waifu.Source_idSource where nameWaifu like ? or nickWaifu like ?',
        'readall': 'select * from Waifu'
    }
}


def open_db():
    global con
    global cur 
    con = sqlite3.connect('WaifuBattler.db')
    con.row_factory = sqlite3.Row
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
        else:
            cur.execute(queries['source']['readall'])

        return cur.fetchone()

def create_source(source_name):
    if cur is not None:
        cur.execute(queries['source']['create'], (source_name,))
        cur.execute(queries['source']['read'], (source_name,))
        con.commit()
        return cur.fetchone()

def create_waifu(name, alias, tier, image_url, source):
    if cur is not None:
        pass
    pass


def read_waifu(name_or_nick):
    if cur is not None:
        if name_or_nick is not None:
            cur.execute(queries['waifu']['read'], (name_or_nick, name_or_nick))
        else:
            cur.execute(queries['waifu']['readall'])
        
        return cur.fetchone()
