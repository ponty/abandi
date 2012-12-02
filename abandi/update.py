from abandi.game import Game
from abandi.game_source import GameSource, game_sources
from entrypoint2 import entrypoint
from parse import parse_game
import db
import extract_id
import time
import sys

def update(source, id, force=False):
    '''parse and update game in database
    :param source: ['all','gb64',..]
    :param id:     ['all','1','1-5','1,5-8,10',..]
    '''
    if source=='all':
        for x in game_sources():
            update_source_games(x.name, id, force)
    else:
        update_source_games(source, id, force)

def update_source_games(source, id, force=False):
    gs = GameSource(source)
    id_set = extract_id.extract_id(id, gs.max_game_id)

    first=1
    for x in id_set:
        sleep_between_downloads = 0
        if not first:
            sleep_between_downloads = 0
        first=0
        update_game(source, x, force, sleep_between_downloads=sleep_between_downloads)

def update_game(source, id, force=False, sleep_between_downloads=0):
    if not force:
        game = db.load_game_by_key(source, id, ignore_empty=False)
        if game:
            print 'up-to-date %s/%d...' % (source, int(id))
            return game
    else:
        print 'force',
    print 'updating %s/%d...' % (source, int(id)),
    sys.stdout.flush()

    if sleep_between_downloads:
        print  'sleeping %s sec...' % sleep_between_downloads,
        sys.stdout.flush()
        time.sleep(sleep_between_downloads)

    game = parse_game(source, id)
    if game:
        print 'found:"' + game.name + '"...',
        db.save_game(game)
    else:
        print 'no game found...',
        g=Game()
        g.source=source
        g.id=id
        db.save_game(g)

    print 'OK'
    return game

entrypoint(update)