from entrypoint2 import entrypoint
import config
import pluginloader


def HtmlParser(name=None):
    return pluginloader.plugin(hook='html_parser', name=name, prio_list=config.htmlparsers)


@entrypoint
def test():
    print HtmlParser()

