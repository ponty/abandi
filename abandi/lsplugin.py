from abandi.pluginloader import plugins_unsorted
import operator
from entrypoint2 import entrypoint


@entrypoint
def list_plugins():
    ''' list plugins
    '''
    ls = plugins_unsorted()
    ls.sort(key=operator.attrgetter('name'))
    for x in ls:
        print '%-20s' % x.name, x.hook
