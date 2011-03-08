import config
import pluginloader

def Unpacker(name=None):
    x=pluginloader.plugin(hook='unpacker', name=name, prio_list=config.unpackers)
    if x:
        return x.plugin_object

def unpackers():
    ls=pluginloader.plugins(hook='unpacker', prio_list=config.unpackers)
    return [x.plugin_object for x in ls]
