from abandi.run import run_game
import cli4func
import db
import game
import logging

def search_games(where='', orderby='name'):
    games = db.load_games(where, orderby)
    return games

def print_games(columns='all', where='', orderby='name', name='', platform='', source=''):
    '''columns   all or id,name
    '''
    if columns != 'all':
        columns = columns.split(',')
    if not where:
        ls = []
        if name:
            ls.append("name like '%%%s%%'" % name)
        if platform:
            ls.append("platform = '%s'" % platform)
        if source:
            ls.append("source like '%%%s%%'" % source)
        where = ' and '.join(ls)
    games = search_games(where, orderby)
    logging.debug(str(games))
    game.print_games(games, columns)
    return games

def main(columns='all', where='', orderby='name', name='', platform='', source='', run=-1):
    run=int(run)
    games=print_games(columns, where, orderby, name, platform, source)
    if len(games)>run and run>=0:
        g=games[run]
        run_game(g.source, g.id,  auto_install=1)
cli4func.main(main)
