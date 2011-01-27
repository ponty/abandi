from abandi import config
from abandi.downloader import Downloader
from abandi.unpacker import Unpacker
import cli4func
import sys
import tempfile

default_url='https://github.com/downloads/ponty/abandi/parsedb.sqlite.7z'

def dbdownload(url=default_url):
    '''downloads and unpacks game database
    :param url: packed sqlite file
    '''
    temp=tempfile.mkdtemp()
    print 'downloading %s...' % url,
    sys.stdout.flush()
    f=Downloader().download(url, temp)
    print 'OK'

    print 'unpacking %s...' % f,
    sys.stdout.flush()
    Unpacker().unpack(f,config.ABANDI_HOME_DIR)
    print 'OK'
    
cli4func.main(dbdownload)
