from abandi import runner
import cli4func
import db
import game
import logging

def search_games(where='', orderby='name'):
    games = db.load_games(where, orderby)
    return games

def search(columns='[source id platform] name', where='', orderby='name', name='', platform='', source='', runner=''):
    ''' search in game database
    
    where   :  SQL where, e.g. "id>5 and name like falcon"
    name    :  game name like this
    source  :  check lsplugin for list
    platform :  check lsplatform for list
    '''
    #if columns != 'all':
    #    columns = columns.split(',')
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
    if runner:
        games = search_for_runner(runner, games)
    logging.debug(str(games))
    game.print_games(games, columns)
    return games

def search_for_runner(runner_name, games):
    r = runner.Runner(runner_name)
    games = filter(lambda x:x.platform in r.platforms, games) 
    if hasattr(r, 'can_run_game'):
        games = filter(lambda x:r.can_run_game(x), games) 
        
    return games
   
cli4func.main(search)
