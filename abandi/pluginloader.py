from abandi import config
from abandi.iplugin import IPlugin
from path import path
import logging
import plugins

log = logging.getLogger(__name__)


def  plugin(name=None, **kw):
    all = plugins(**kw)
    d = dict([(x.name, x) for x in all])
    pl = None
    if name:
        pl = d.get(name)
    else:
        if len(all):
            pl = all[0]

    if pl:
        log.debug('plugin selected:' + pl.name)
    else:
        log.debug('plugin not found')
    return pl


def default_places():
    x = [path(__file__).dirname() / 'plugins']
    x += [config.ABANDI_HOME_DIR / 'plugins']
    return x


def plugins(prio_list=None, **kw):
    all = plugins_unsorted(**kw)
    if prio_list:
        ls = [(prio_list.index(
            x.name) if x.name in prio_list else 1000, x) for x in all]
        ls.sort(key=lambda x: x[0])
        all = [x[1] for x in ls]
    return all


def plugins_unsorted(hook=None, places=None, ext='ini'):
    if not places:
        places = default_places()

    all = IPlugin.__subclasses__()

    def create_obj(cl):
        try:
            obj = cl()
        except Exception, e:
            log.debug('plugin error:')
            log.debug(e)
            obj = None
        return obj

    all = [create_obj(x) for x in all]

    # filter None
    all = [x for x in all if (x)]

    def pfilter(p):
        jo = 1
        if hook:
            if not hasattr(p, 'hook'):
                log.debug('missing hook in "' + p.name + '" ')
            else:
                jo = p.hook == hook
                if jo:
                    log.debug('plugin "' + p.name +
                              '" was accepted for hook "' + hook + '"')
                    if hasattr(p, 'available'):
                        jo = p.available()
                    else:
                        log.debug('missing "available" in "' + p.name + '" ')
        return jo

    all = [x for x in all if pfilter(x)]
    return all
