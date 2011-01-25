from abandi.path import path
from abandi.pluginloader import plugins_unsorted
import cli4func
import logging
import operator
import platform

def list_versions():
    ''' list plugin backend versions
    '''
    print 'python \t\t'+platform.python_version()
    all = plugins_unsorted()
    all.sort(key=operator.attrgetter('name'))

    for x in all:
        if hasattr(x.plugin_object, 'version'):
            v=x.plugin_object.version()
            print x.name +'\t\t'+ (v if v else 'not installed' )
    return all



cli4func.main(list_versions)
