from abandi.downloaders.cache import Cache
from abandi.downloaders.urllib import Urllib


def Downloader(cached=True, name=None):
    if cached:
        return Cache()
    else:
        return Urllib()
