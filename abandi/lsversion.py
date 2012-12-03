from abandi.pluginloader import plugins_unsorted
import operator
import platform
import abandi
from entrypoint2 import entrypoint


@entrypoint
def list_versions():
    ''' list plugin backend versions
    '''

    print 'python \t\t' + platform.python_version()
    print 'abandi \t\t' + abandi.__version__

    all = plugins_unsorted()
    all.sort(key=operator.attrgetter('name'))

    for x in all:
        if hasattr(x, 'version'):
            v = x.version()
            print x.name + '\t\t' + (v if v else 'not installed')
    return all
