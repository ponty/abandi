from abandi import runner
from entrypoint2 import entrypoint
import db
import game
import logging

def search_games(where='', orderby='name'):
    '''
    '''
    games = db.load_games(where, orderby)
    return games

def search_for_runner(runner_name, games):
    '''
    '''
    r = runner.Runner(runner_name)
    #print runner_name
    games = filter(lambda x:x.platform in r.platforms, games)
    if hasattr(r, 'can_run_game'):
        games = filter(lambda x:r.can_run_game(x), games)

    return games

@entrypoint
def search(col_format='[source id platform] name', where='', orderby='name', name='', platform='', source='', runner=''):
    ''' search in game database

    :param where:     SQL where, e.g. "id>5 and name like falcon"
    :param name:      game name like this
    :param source:    check lsplugin for list
    :param platform:  check lsplatform for list

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
    game.print_games(games, col_format)
    return games


