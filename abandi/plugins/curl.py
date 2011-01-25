from abandi import FileUtils
from abandi.path import path
from yapsy.IPlugin import IPlugin
import logging
import pycurl
import tempfile
import time



#last_call = dict()


class Curl (IPlugin):
    '''
    pycurl should be installed

    http://curl.haxx.se/libcurl/c/curl_easy_setopt.html
    http://curl.haxx.se/libcurl/c/curl_easy_getinfo.html
    '''

    hook = 'downloader'

    # sec
#    wait_between_downloads = 2
    
    def __init__(self):        
        pass

#    def sleep(self, url):
#        global last_call
#        site = url.split('/')[2]
#        t = time.time()
#        last = last_call.get(site)
#        print site, t,last,last_call
#        if not last:
#            last_call[site] = t 
#            return
#        
#        dt = t - last
#        tosleep = self.wait_between_downloads - dt
#        tosleep=int(tosleep+0.5)
#        print tosleep, 
#        if tosleep > 0:
#            logging.debug('sleeping %s sec'%tosleep)
#            time.sleep(tosleep)
#        t = time.time()
#        last_call[site] = t 

    def download(self, url, targetDir, fileName=None, useSessionCookie=False, referer=None):
#        self.sleep(url)
        c = pycurl.Curl()
        if useSessionCookie:
            c.setopt(pycurl.COOKIEFILE, '')
            self._downloadFileInt2(c, referer, tempfile.gettempdir())
            p = self._downloadFileInt2(c, url, targetDir, fileName, referer=referer)
        else:
            p = self._downloadFileInt2(c, url, targetDir, fileName)
        c.close()
        logging.debug('downloaded file name:' + p)
        return p



    def _downloadFileInt2(self, c, url, targetDir, fileName=None, referer=None):
        targetDir = path(targetDir)
        if not targetDir.isdir():
            targetDir.makedirs()
        resolve_file_name = not fileName
        if not fileName:
            fileName = 'xyz987'

        p = targetDir / fileName
        f = open(p, "wb")

        logging.debug('downloading:' + url)

        c.setopt(pycurl.URL, str(url))
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.WRITEDATA, f)
        c.setopt(pycurl.VERBOSE, 1)

        def debug(debug_type, debug_msg):
            if debug_type != 3:
                s = "curl (%d): %s" % (debug_type, debug_msg)
                logging.debug(s.strip())

        c.setopt(pycurl.DEBUGFUNCTION, debug)

        #c.setopt(pycurl.IGNORE_CONTENT_LENGTH, 1)

        if referer:
            # --referer=url
            # Include 'Referer: url' header in HTTP request. Useful for
            # retrieving documents with server-side processing that assume they
            # are always being retrieved by interactive web browsers and only
            # come out properly when Referer is set to one of the pages that
            # point to them.
            c.setopt(pycurl.REFERER, str(referer))

        # TODO: sleep

        try:
            # sometimes exception:
            # pycurl.error: (18, 'transfer closed with outstanding read data remaining')
            c.perform()
        except:
            pass
        eff_url = c.getinfo(pycurl.EFFECTIVE_URL)
        logging.debug('download done')
        logging.debug('EFFECTIVE_URL:' + eff_url)
        if resolve_file_name:
            newPath = targetDir / FileUtils.convertToFileName(eff_url)
            p.rename(newPath)
            p = newPath

        f.close()
        return p

#    def resolveUrl(self, url):
#        c = pycurl.Curl()
#        c.setopt(pycurl.URL, url)
#        def write(s):
#            pass
#        c.setopt(pycurl.WRITEFUNCTION, write)
#        c.setopt(pycurl.FOLLOWLOCATION, 1)
#        c.perform()
#        ret = c.getinfo(pycurl.EFFECTIVE_URL)
#        c.close()
#        return ret
