from entrypoint2 import entrypoint
import pluginloader


def GameSource(name):
    return pluginloader.plugin(hook='game_source', name=name)


def game_sources():
    return pluginloader.plugins(hook='game_source')


@entrypoint
def test():
    print GameSource('abandoneer')
    print game_sources()

