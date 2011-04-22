import pluginloader

def Runner(name):
    x=pluginloader.plugin(hook='runner', name=name)
    if x:
        return x.plugin_object

def runners():
    ls=pluginloader.plugins(hook='runner')
    return [x.plugin_object for x in ls]
