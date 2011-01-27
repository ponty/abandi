from abandi import FileUtils
from path import path
from yapsy.IPlugin import IPlugin
import logging
#import tempfile
import urllib2



#last_call = dict()


class urllib (IPlugin):
    '''
    '''

    hook = 'downloader'

    
    def __init__(self):        
        pass


    def download(self, url, targetDir, fileName=None, useSessionCookie=False, referer=None):
        cookie = None
        targetDir = path(targetDir)
        if useSessionCookie:
            parent = urllib2.urlopen(referer)
            cookie = parent.info()['set-cookie']
            print cookie
        
        req = urllib2.Request(url)
        if referer:
            req.add_header('Referer', referer)
        if cookie:
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


