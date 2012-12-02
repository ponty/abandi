from entrypoint2 import entrypoint
import db
import game


def search_game(source, id):
    #x=sources.manager.find_plugin(source)
    #game=db.load_game_by_key(x.info.get('short_name'), id)
    game=db.load_game_by_key(source, id)
    return game


@entrypoint
def print_game(source, id):
    '''print all information for game in database
    :param source: ['gb64',..]
    :param id:     ['1',..]
    '''
    g = search_game(source, id)
    game.print_game(g)

