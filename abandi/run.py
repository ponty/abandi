from abandi import info
from abandi.install import install_game
from abandi.runner import runners, Runner
import cli4func
import logging
import platform

message = '''Install the game first:
    install {source} {id}
or run with auto-install:
    run -a {source} {id}'''
def run_game(source, id, runner='auto', auto_install=False):
    game = info.search_game(source, id)
    if not game or not game.dir:
        if auto_install:
            game = install_game(source, id)
        else:
            print message.format(source=source, id=str(id))
            return
    run(game, runner)

def check_emulator(p):
    logging.debug('checking version:'+ p.name)
    v = p.version()
    if not v:
        print 'emulator %s not installed!' % p.name
        if platform.dist()[0].lower() == 'ubuntu':
            print 'you can install by:'
            print 'sudo apt-get install %s' % p.ubuntu_package
    return v

def find_runner_plugin(game):
    logging.debug(game.name + ' platform:' + game.platform)
    for p in runners():
        logging.debug(p.name + ' platforms:' + str(p.platforms))
        if game.platform in p.platforms:
            if check_emulator(p):
                if hasattr(p, 'test_game'):
                    logging.debug('test_game()' )
                    ok=p.test_game(game)
                else:
                    ok=1
                if ok:
                    logging.debug(p.name + ' was accepted for ' + game.name)
                    return p

def run(game, runner='auto'):
    if not game or not game.dir:
        print 'game is missing!'
        return
    if runner == 'auto':
        p = find_runner_plugin(game)
    else:
        p = Runner(runner)
        if not p:
            print runner +' runner not found!'
            return 0
        if not check_emulator(p):
            return 0
    if not p:
        print 'no runner found! (game="{0}",platform={1})'.format(game.name, game.platform)
        return 0
    print 'running %s..\n' % game.name
    p.run_game(game)
    return 1

cli4func.main(run_game)
