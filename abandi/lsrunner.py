from path import path
from abandi.pluginloader import plugins_unsorted
from abandi.runner import runners
import cli4func
import logging
import operator

def list_runners():
    ''' list runners found by yapsy
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



cli4func.main(list_runners)
