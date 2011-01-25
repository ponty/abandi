import cli4func
import pluginloader

def GameSource(name):
    x=pluginloader.plugin(hook='game_source', name=name)
    if x:
        return x.plugin_object

def game_sources():
    ls=pluginloader.plugins(hook='game_source')
    return [x.plugin_object for x in ls]

def test():
    print GameSource('abandoneer')
    print game_sources()

cli4func.main(test)
