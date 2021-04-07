import sqlite3

con = None
cur = None

queries = {
    'source': {
        'create': 'insert into Source (nameSource) values (?)',
        'read': 'select * from Source where nameSource like ?',
        'readall': 'select nameSource from Source'
    },

    'waifu': {
        'create': 'insert into Waifu (nameWaifu, tierWaifu, Source_idSource) values (?, ?, ?)',
        'read': 'select * from Waifu inner join Source S on S.idSource = Waifu.Source_idSource where nameWaifu like ? or nickWaifu like ?',
        'readall': 'select * from Waifu',
        'update_nick': 'update Waifu set nickWaifu=? where nameWaifu=? or nickWaifu=?',
        'update_url_image': 'update Waifu set imageURLWaifu=? where nameWaifu=? or nickWaifu=?'
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
    if cur is not None and source_name is not None:
        print(source_name)
        cur.execute(queries['source']['create'], (source_name,))
        con.commit()
        cur.execute(queries['source']['read'], (source_name,))
        return cur.fetchone()

def create_waifu(name, tier, source_name):
    if cur is not None:
        #print(f'{name} {tier} {source_name}')
        cur.execute(queries['source']['read'], (source_name,))
        source = cur.fetchone()

        print(source)
        if source is None:
            source = create_source(source_name)
            print(source)

        cur.execute(queries['waifu']['create'], (name, tier, source['idSource']))
        con.commit()
        cur.execute(queries['waifu']['read'], (name, name))
        return cur.fetchone()


def read_waifu(name_or_nick):
    if cur is not None:
        if name_or_nick is not None:
            cur.execute(queries['waifu']['read'], (name_or_nick, name_or_nick))
        else:
            cur.execute(queries['waifu']['readall'])
        
        return cur.fetchone()

def add_waifu_alias(name, nick):
    if cur is not None:
        if name is not None and nick is not None:
            waifu = read_waifu(name)
            cur.execute(queries['waifu']['update_nick'], (nick, name, name))
            con.commit()

def add_waifu_image(name, url):
    if cur is not None:
        if name is not None and url is not None:
            waifu = read_waifu(name)
            cur.execute(queries['waifu']['update_url_image'], (url, name, name))
            con.commit()