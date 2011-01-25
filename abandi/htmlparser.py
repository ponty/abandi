import cli4func
import config
import pluginloader

def HtmlParser(name=None):
    x=pluginloader.plugin(hook='html_parser', name=name, prio_list=config.htmlparsers)
    if x:
        return x.plugin_object

def test():
    print HtmlParser()

cli4func.main(test)
