from abandi.runner import runners
import operator

from entrypoint2 import entrypoint


@entrypoint
def list_runners():
    ''' list runners
    '''
    all = runners()
    all.sort(key=operator.attrgetter('name'))
    s = ''
    for x in all:
        ls = []
        ls += ['"' + x.name + '"']
        ls += ['"' + x.long_name + '"']
        ls += ['"[' + ', '.join(x.platforms) + ']"']
        ls += ['"' + x.home_url + '"']

        line = ', '.join(ls)
        s += line+'\n'    
    print s
    return s


