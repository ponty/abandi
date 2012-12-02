from abandi import config
from abandi.downloader import Downloader
from entrypoint2 import entrypoint
from path import path
import pyunpack
import sys
import tempfile


@entrypoint
def dbdownload(url=config.DB_GAME_URL):
    '''downloads and unpacks game database
    :param url: packed sqlite file
    '''
    temp = tempfile.mkdtemp()
    print 'downloading %s...' % url,
    sys.stdout.flush()
    f = Downloader().download(url, temp)
    print 'OK'

    f1 = config.DB_GAME_PATH
    f2 = config.DB_GAME_PATH + '.backup'
    print 'creating backup of existing file: %s -> %s' % (f1, f2)
    path(f1).move(f2)

    print 'unpacking %s...' % f,
    sys.stdout.flush()
    error_text = pyunpack.Archive(f).extractall(config.ABANDI_HOME_DIR, auto_create_dir=1)
    if error_text:
        print 'ERROR!'
        print error_text
    else:
        print 'OK'

