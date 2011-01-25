from abandi.path import path
from abandi.pluginloader import plugins_unsorted
import cli4func
import logging
import operator

def list_plugins():
    ''' list plugins found by yapsy
    '''
    all = plugins_unsorted()
    all.sort(key=operator.attrgetter('name'))
    for x in all:
        print x.name +'\t\t'+ x.plugin_object.hook



cli4func.main(list_plugins)
