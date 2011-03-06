import logging
import os.path
import sqlite3
import sys
import config
import game

PARSE_DB = 0
INSTALL_DB = 1

d = config.ABANDI_HOME_DIR

FILE_NAME = [d / 'parsedb.sqlite', d / 'installdb.sqlite']
VERSION = [1, 1]
fields = [game.fields_key + game.fields_parse, game.fields_key + game.fields_install]
data_fields = [game.fields_parse, game.fields_install]
fields_all = game.fields_key + game.fields_parse + game.fields_install
def get_version(n):
    conn = sqlite3.connect(FILE_NAME[n])
    cur = conn.cursor()
    version = None
    try:
        execute(cur, 'select * from version')
        row = cur.fetchone()
        version = row[0]
    except:
        logging.debug(sys.exc_info())
        version = -1
    cur.close()
    return version

def exists(n):
    return os.path.isfile(FILE_NAME[n])

def init():
    init_n(0)
    init_n(1)

def init_n(n):
    logging.debug('own version:' + str(VERSION))
    if exists(n):
        db_version = get_version(n)
        logging.debug('db version:' + str(db_version))
        if int(VERSION[n]) != int(db_version):
            logging.debug('version mismatch, removing ' + FILE_NAME[n])
            os.remove(FILE_NAME[n])

    if not exists(n):
        conn = sqlite3.connect(FILE_NAME[n])
        cur = conn.cursor()
        create_tables(cur, n)
        conn.commit()
        cur.close()

def create_tables(cur, n):
    execute(cur, 'create table games('
            + ' text,'.join(game.fields_key) + ' integer'
            + ','
            + ' text,'.join(data_fields[n]) + ' text'
            + ')')
    execute(cur, 'create table version(version text)')
    execute(cur, 'insert into version (version) values (?)', (VERSION[n],))

def execute(cur, sql, x=tuple()):
    logging.debug('sql:' + sql)
    logging.debug('par:' + str(x))
    cur.execute(sql, x)

def open():
    init()
    #conn = sqlite3.connect(FILE_NAME[n])
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    execute(cur, 'attach database "%s" as p' % (FILE_NAME[PARSE_DB],))
    execute(cur, 'attach database "%s" as i' % (FILE_NAME[INSTALL_DB],))
    return (conn, cur)

def save_game(game):
    game.source = game.source.lower()

    (conn, cur) = open()

    cur = conn.cursor()

    def doit(dbalias,n):
        execute(cur, 'select * from {dbalias}.games where id=? and source=?'.format(dbalias=dbalias)
                , (game.id, game.source))

        if not len(cur.fetchall()):
            execute(cur, 'insert into {dbalias}.games (id,source) values (?,?)'.format(dbalias=dbalias),
                    (game.id, game.source.lower()))

        for f in data_fields[n]:
            v=game.__dict__.get(f)
            #if v:
            execute(cur, 'UPDATE {dbalias}.games SET {f}=? WHERE id=? and source=?'.format(f=f,dbalias=dbalias)
                    , (v, game.id, game.source))
    doit('p',0)

    if game.zip or game.dir:
        doit('i',1)

    close(conn)

def close(conn):
    conn.commit()
    cur = conn.cursor()
    cur.close()


def load_games(where='', orderby='name'):
    if not exists(0):
        return []

    (conn, cur) = open()

    games = []

    if where:
        where = ' where ' + where

    execute(cur,
            ('select * from {0} ' + where + '' + ' order by ' + orderby).format(game_table())
            )
    rows = cur.fetchall()
    for row in rows:
        g = game.Game()
        g.__dict__ = dict(zip(fields_all, row))
        games.append(g)
    cur.close()
    games = filter(lambda g:g.name, games)
    return games

def game_table():
    join = 'p.games LEFT JOIN i.games ON p.games.source=i.games.source and p.games.id=i.games.id'
    f = ','.join(['p.games.source', 'p.games.id'] + game.fields_parse + game.fields_install)
    x = '(select {f} from {join})'.format(f=f, join=join)
    return x

def load_game_by_key(source, id, ignore_empty=True):

    if not exists(0):
        return

    source = source.lower()
    (conn, cur) = open()

    execute(cur,
            'select * from {0} where source=? and id=?'.format(game_table()),
            (source, id))

    row = cur.fetchone()

    g = None
    if row:
        g = game.Game()
        g.__dict__.update(dict(zip(fields_all, row)))

    cur.close()

    if g and ignore_empty and not g.name:
        g = None

    return g
