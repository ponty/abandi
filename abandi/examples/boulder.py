'''
1. list boulder games 
2. start selected game
'''

from abandi.search import search_games
from abandi.run import run_game
from psidialogs import choice
import unicodedata
from entrypoint2 import entrypoint
def norm(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')


@entrypoint
def main():
    games = search_games(where='name like "%boulder%"')
    dic = dict([ (norm(x.name), x) for x in games])
    name = choice(sorted(dic.keys()))
    if name:
        game = dic[name]
        run_game(game.source, game.id, auto_install=1)
