from abandi import config, info
from abandi.FileUtils import convertToFileName
from abandi.downloader import Downloader
from abandi.game_source import GameSource
from abandi.update import update_game
from entrypoint2 import entrypoint
import db
import logging
import os
import pyunpack
import sys

log = logging.getLogger(__name__)


def install_game(source='abandonia', id=129, downloadonly=False,
                  unpackonly=False,removezip=False,nocache=False):
    '''download and unpack game found in database
    :param source: ['gb64',..]
    :param id:     ['1',..]
    '''
    game = info.search_game(source, id)
    if not game:
        game = update_game(source, id)
    install(game, downloadonly, unpackonly,removezip,nocache)
    return game

def install(game, downloadonly=False, unpackonly=False,removezip=False,nocache=False):
    download = not unpackonly
    unpack = not downloadonly
    if download:
        download_game(game,nocache)
    if unpack:
        unpack_game(game,removezip)

def download_game(game,nocache=False):
    targetDir = config.GameArchives / game.source

    src_plugin  = GameSource(game.source)
    downloadOptions = {}
    if hasattr(src_plugin, 'download_options'):
        downloadOptions = src_plugin.download_options(game)

    if hasattr(src_plugin,'game_file_url'):
        log.debug('game_file_url is not static, calling plugin:%s' % src_plugin)
        gameUrl = src_plugin.game_file_url(game)
    else:
        gameUrl = game.game_file_url
    assert gameUrl
    
    downloader = Downloader(cached=not nocache)
    print 'downloading %s...' % game.name,
    sys.stdout.flush()
    
    game.zip = downloader.download(gameUrl, targetDir, **downloadOptions)
    print 'OK'
    #downloader = DownloaderFactory.createDownloader(not nocache)
    #def game_downloader(game, targetDir, downloader):
    #    gameUrl = game.game_file_url
    #    game.zip = downloader.downloadFile(gameUrl, targetDir,
    #                                       downloadOptions=downloadOptions)
    #if src_plugin.game_downloader:
    #    game_downloader = src_plugin.game_downloader
    #game_downloader(game, targetDir, downloader)

    db.save_game(game)

def unpack_game(game,removezip=False):
    targetDir = config.GAMES / game.source /convertToFileName(game.name)+'.'+str(game.id)
    
    print 'unpacking %s...' % game.name,
    sys.stdout.flush()
    
    pyunpack.Archive(game.zip).extractall(targetDir, auto_create_dir=True)
#    if msg:
#        return False
    print 'OK'
    if removezip:
        os.remove(game.zip)
    game.dir = targetDir
    db.save_game(game)
    return True

entrypoint(install_game)
