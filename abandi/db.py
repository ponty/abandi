from abandi import config
from abandi.game import Game, fields
import logging
import os.path
import sqlite3
import sys

FILE_NAME = config.ABANDI_HOME_DIR / 'gamesdb.sqlite'
VERSION = 9


def get_version():
    conn = sqlite3.connect(FILE_NAME)
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

def exists():
    return os.path.isfile(FILE_NAME)

def init():
    logging.debug('own version:' + str(VERSION))
    if exists():
        db_version = get_version()
        logging.debug('db version:' + str(db_version))
        if int(VERSION) != int(db_version):
            logging.debug('version mismatch, removing ' + FILE_NAME)
            os.remove(FILE_NAME)

    if not exists():
        conn = sqlite3.connect(FILE_NAME)
        cur = conn.cursor()
        create_tables(cur)
        conn.commit()
        cur.close()

def create_tables(cur):
    execute(cur, 'create table games('
#    + ' text,'.join(sorted(fields, key=lambda x: 100 if x=='id' else 1 )) +
    + ' text,'.join(fields) +
    ' integer)')
    execute(cur, 'create table version(version text)')
    execute(cur, 'insert into version (version) values (?)', (VERSION,))

def execute(cur, sql, x=tuple()):
    logging.debug('sql:' + sql)
    logging.debug('par:' + str(x))
    cur.execute(sql, x)

def open():
    conn = sqlite3.connect(FILE_NAME)
    return conn

def save_game(game, conn=None):
    game.source = game.source.lower()

    mustClose = False
    if not conn:
        init()
        conn = open()
        mustClose = True

    cur = conn.cursor()

    execute(cur, 'select * from games where id=? and source=?'
            , (game.id, game.source))
    if not len(cur.fetchall()):
        execute(cur, 'insert into games (id,source) values (?,?)', (game.id, game.source.lower()))

    for f in fields:
        execute(cur, 'UPDATE games SET %s=? WHERE id=? and source=?'
                % f, (game.__dict__.get(f), game.id, game.source))

    if mustClose:
        close(conn)

def close(conn):
    conn.commit()
    cur = conn.cursor()
    cur.close()

def load_games(where='', orderby='name'):
    if not exists():
        return
    conn = open()
    cur = conn.cursor()
    games = []

    if where:
        where = ' where ' + where
    execute(cur, 'select * from games ' + where + '' + ' order by ' + orderby)
    rows = cur.fetchall()
    for row in rows:
        game = Game()
        game.__dict__ = dict(zip(fields, row))
        games.append(game)
    cur.close()
    games=filter(lambda g:g.name, games)
    return games

def load_game_by_key(source, id, ignore_empty=True):
    if not exists():
        return
    source = source.lower()
    conn = open()
    cur = conn.cursor()

    execute(cur, 'select * from games where source=? and id=?', (source, id))
    row = cur.fetchone()
    game = None
    if row:
        game = Game()
        game.__dict__ = dict(zip(fields, row))


    cur.close()
    if ignore_empty and not game.name:
        game = None
    return game
