from abandi.pluginloader import plugins_unsorted
import operator
from entrypoint2 import entrypoint

@entrypoint
def list_plugins():
    ''' list plugins found by yapsy
    '''
    all = plugins_unsorted()
    all.sort(key=operator.attrgetter('name'))
    for x in all:
        print x.name +'\t\t'+ x.plugin_object.hook



