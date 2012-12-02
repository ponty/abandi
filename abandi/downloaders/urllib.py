from abandi import FileUtils
from path import path
from abandi.iplugin import IPlugin
import logging
import urllib2

log = logging.getLogger(__name__)


class Urllib (IPlugin):
    '''
    '''

    hook = 'downloader'
    name='urllib'

    
    def __init__(self):        
        pass


    def download(self, url, targetDir, fileName=None, useSessionCookie=False, referer=None):
        log.debug('downloading:' + str(url))
        cookie = None
        targetDir = path(targetDir)
        if not targetDir.isdir():
            targetDir.makedirs()
        if useSessionCookie:
            parent = urllib2.urlopen(referer)
            cookie = parent.info()['set-cookie']
            #print cookie
        
        req = urllib2.Request(url)
        if referer:
            logging.debug('referer:' + referer)
            req.add_header('Referer', referer)
        if cookie:
            logging.debug('cookie:' + cookie)
            req.add_header('Cookie', cookie)
        
        f = urllib2.urlopen(req)
        eff_url = f.geturl()
        logging.debug('EFFECTIVE_URL:' + eff_url)
        
        s = f.read()
        #print s
        
        if fileName:
            targ = targetDir / fileName
        else:
            targ = targetDir / FileUtils.convertToFileName(eff_url)
        
        open(targ,'wb').write(s)
        
        logging.debug('downloaded file name:' + targ)
        return targ


