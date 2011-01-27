import cli4func
import game
import game_source

def parse_game(source, id):
    id=int(id)
    game = game_source.GameSource(source).parse_game(id)
    return game

def print_game(source, id):
    '''parse game on source and print all information
    :param source: ['gb64',..]
    :param id:     ['1',..]
    '''
    g = parse_game(source, id)
    game.print_game(g)

cli4func.main(print_game)
