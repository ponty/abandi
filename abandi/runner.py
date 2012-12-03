import pluginloader


def Runner(name):
    x = pluginloader.plugin(hook='runner', name=name)
    return x


def runners():
    return pluginloader.plugins(hook='runner')
