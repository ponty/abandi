from abandi import config
from path import path
from yapsy.PluginManager import PluginManager
import logging

def  plugin(name=None, **kw):
    all = plugins(**kw)
    d = dict([(x.name , x) for x in all])
    pl = None
    if name:
        pl = d.get(name)
    else:
        if len(all):
            pl = all[0]

    if pl:
        logging.debug('plugin selected:' + pl.name)
    else:
        logging.debug('plugin not found')
    return pl

def default_places():
    x = [path(__file__).dirname() / 'plugins']
    x += [config.ABANDI_HOME_DIR / 'plugins']
    return x

def plugins(prio_list=None, **kw):
    all = plugins_unsorted(**kw)
    if prio_list:
        ls = [(prio_list.index(x.name) if x.name in prio_list else 1000, x) for x in all]
        ls.sort(key=lambda x: x[0])
        all = [x[1] for x in ls]
    return all

def plugins_unsorted(hook=None, places=None, ext='ini'):
    if not places:
        places = default_places()

    pm = PluginManager()
#    pm.setPluginInfoClass(PluginInfo)
    pm.setPluginInfoExtension(ext)
    pm.setPluginPlaces(places)
    pm.collectPlugins()
    all = pm.getAllPlugins()

    def pfilter(p):
        jo = 1
        if hook:
            if not hasattr(p.plugin_object, 'hook'):
                logging.debug('missing hook in "' + p.name + '" ')
            else:
                jo = p.plugin_object.hook == hook
                if jo:
                    logging.debug('plugin "' + p.name + '" was accepted for hook "' + hook + '"')
                    if hasattr(p.plugin_object, 'available'):
                        jo = p.plugin_object.available()
                    else:
                        logging.debug('missing "available" in "' + p.name + '" ')
        return jo

    all = [x for x in all if pfilter(x)]
    for x in all:
        x.plugin_object.name = x.name
    return all

