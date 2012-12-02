from abandi import game
from abandi.parse import parse_game
from nose.tools import eq_


def test_abandonia():
    g = parse_game('abandonia', '1')
    game.print_game(g)
    eq_(g.source, 'abandonia')
    eq_(g.id, 1)
    eq_(g.name, 'Budokan - The Martial Spirit')
    eq_(g.platform, 'dos')


def test_abandoneer():
    g = parse_game('abandoneer', '1')
    game.print_game(g)
    eq_(g.source, 'abandoneer')
    eq_(g.id, 1)
    eq_(g.name, 'Wasteland')
    eq_(g.platform, 'dos')


def test_gb64():
    g = parse_game('gb64', '1')
    game.print_game(g)
    eq_(g.source, 'gb64')
    eq_(g.id, 1)
    eq_(g.name, '$100,000 Pyramid, The')
    eq_(g.platform, 'c64')


def test_oscomp():
    g = parse_game('oscomp', '1')
    game.print_game(g)
    eq_(g.source, 'oscomp')
    eq_(g.id, 1)
    eq_(g.name, 'Bomber Man')
    eq_(g.platform, 'nes')


def test_osd():
    g = parse_game('osd', '1')
    game.print_game(g)
    eq_(g.source, 'osd')
    eq_(g.id, 1)
    eq_(g.name, '10th Frame Bowling')
    eq_(g.platform, 'dos')



