from abandi.game_source import game_sources
import operator
from entrypoint2 import entrypoint

@entrypoint
def list_sources():
    ''' list runners found by yapsy
    '''
    all = game_sources()
    all.sort(key=operator.attrgetter('name'))
    s = ''
    for x in all:
        ls = []
        ls += ['"' + x.name + '"']
        ls += ['"' + x.long_name + '"']
        ls += ['"[' + ', '.join(x.platforms) + ']"']
        ls += ['"' + x.homepage + '"']
        ls += ['"' + str(x.max_game_id) + '"']

        line = ', '.join(ls)
        s += line+'\n'    
    print s
    return s



