from entrypoint2 import entrypoint
import pluginloader

def GameSource(name):
    x=pluginloader.plugin(hook='game_source', name=name)
    if x:
        return x.plugin_object

def game_sources():
    ls=pluginloader.plugins(hook='game_source')
    return [x.plugin_object for x in ls]


@entrypoint
def test():
    print GameSource('abandoneer')
    print game_sources()

