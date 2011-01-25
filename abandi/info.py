import cli4func
import db
import game

def search_game(source, id):
    #x=sources.manager.find_plugin(source)
    #game=db.load_game_by_key(x.info.get('short_name'), id)
    game=db.load_game_by_key(source, id)
    return game

def print_game(source, id):
    g = search_game(source, id)
    game.print_game(g)

cli4func.main(print_game)
