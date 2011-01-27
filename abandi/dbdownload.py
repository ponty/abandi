from abandi import config
from abandi.downloader import Downloader
from abandi.unpacker import Unpacker
import cli4func
import tempfile

default_url='http://ponty.github.com/abandi/parsedb.sqlite.7z'

def dbdownload(url=default_url):
    '''downloads and unpacks game database
    :param url: packed sqlite file
    '''
    temp=tempfile.mkdtemp()
    f=Downloader().download(url, temp)
    Unpacker().unpack(f,config.ABANDI_HOME_DIR)
    
cli4func.main(dbdownload)
