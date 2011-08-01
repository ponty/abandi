from abandi import config
from abandi.downloader import Downloader
from entrypoint2 import entrypoint
import pyunpack
import sys
import tempfile

default_url='https://github.com/downloads/ponty/abandi/parsedb.sqlite.7z'


@entrypoint
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
    error_text = pyunpack.Archive(f).extractall(config.ABANDI_HOME_DIR, auto_create_dir=1)
    if error_text:
        print 'ERROR!'
        print error_text
    else:
        print 'OK'
    
