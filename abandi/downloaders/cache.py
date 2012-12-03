from abandi import FileUtils
from abandi.downloaders.urllib import Urllib
from abandi.iplugin import IPlugin
import path


class Cache (IPlugin):
    hook = 'downloader'
    name = 'cache'

    def __init__(self):
        self.backend = None

    def download(self, url, targetDir, fileName=None, **kw):
        # assert self.backend
        targetDir = path.path(targetDir)

        if url:
            if not fileName:
                fileName = FileUtils.convertToFileName(url)
            pfad = targetDir / fileName
            if pfad.isfile() and pfad.getsize():
                return pfad

        pl = Urllib()
        return pl.download(url, targetDir, fileName, **kw)

#    def resolveUrl(self, url):
#        targetDir = TargetDir.create(TargetDir.RESOLVE)
#        os.makedirs(targetDir)
#        fileName = FileUtils.convertToFileName(url)
#        filePath = os.path.join(targetDir, FileUtils.convertToFileName(fileName))
#        if filePath.isfile()  and os.path.getsize(filePath):
#            text = FileUtils.readFileAsString(filePath)
#            return text
#
#        text = WGet.WGet().resolveUrl(url)
#        if not text:
#            text = ""
#
#        FileUtils.writeFileAsString(filePath.getAbsolutePath(), text)
#        return text
