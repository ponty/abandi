import config
import pluginloader

def Downloader(cached=True, name=None):
    if cached:
        ls=config.downloaders_cache
    else:
        ls=config.downloaders_nocache

    x=pluginloader.plugin(hook='downloader', name=name, prio_list=ls)
    if x:
        return x.plugin_object
