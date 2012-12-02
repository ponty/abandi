from abandi.info import print_game, search_game
from abandi.search import search_games
from nose.tools import eq_


def test_game():
    print_game('gb64', '5665')

    g = search_game('gb64', '5665')
    eq_(g.source, 'gb64')
    eq_(g.id, 5665)
    eq_(g.name, "Pharaoh's Curse")
    eq_(g.platform, 'c64')

    
def test_boulder():
    games = search_games(where='name like "%boulder%"')
    print games
    assert games
