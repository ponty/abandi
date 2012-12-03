from abandi import config
from abandi.downloader import Downloader
from abandi.htmlparser import HtmlParser
from path import path
import logging
import re

SLASH = "/"


class WebParser:
    def __init__(self, url, cached=True):
        logging.debug('parsing:' + url)
        self.images = None
        self.links = None
        self.texts = None
        if url:
            self.url = url.strip()
            self.loadPage(cached)
            self.parser = HtmlParser()
            self.parser.set_html(path(self.page).text())

    def loadPage(self, cached):
        downloader = Downloader(cached)
        targetDir = config.CACHE
        self.page = downloader.download(self.url, targetDir)

    def parseImgTags(self):
        list = []
        for x in self.parser.images():
            srcFull = self.getAbsUrl(x)
            srcFull = srcFull.replace(" ", "%20")
            srcFull = srcFull.replace("&amp", "&")
            srcFull = srcFull.replace("&#039", "'")
            list.append(srcFull)
        return list

    def getAbsUrl(self, url):
        absUrl = ''
        if url.startswith("http"):
            absUrl = url
        else:
            absUrl = self.concatUrl(self.getBaseUrl(), url)
        return absUrl

    def concatUrl(self, baseUrl, url2):
        if baseUrl.endswith(SLASH) and url2.startswith(SLASH):
            return baseUrl + url2[1:]
        else:
            if not baseUrl.endswith(SLASH) and not url2.startswith(SLASH):
                return baseUrl + SLASH + url2
            else:
                return baseUrl + url2

    def getBaseUrl(self):
        ''' http://base/.../ -> http://base '''
        slashPos = self.url.find(SLASH, 7)
        base = ''
        if slashPos >= 0:
            base = self.url[0:slashPos]
        else:
            base = self.url
        return base

    def getImages(self):
        if not self.images:
            self.images = self.parseImgTags()
        return self.images

    def getImage(self, i):
        if len(self.getImages()) > i:
            return self.getImages()[i]
        return None

    def getLinks(self):
        if not self.links:
            self.links = self.parser.links()
        return self.links

    def getTexts(self):
        ''' trimmed '''
        if not self.texts:
            self.texts = []
            for text in self.parser.texts():
                text = text.strip()
                if text:
                    if text != ",":
                        if "&nbsp" not in text:
                            if "{" not in text:
                                self.texts.append(text)
        return self.texts

    def getTextRelative(self, str, plus):
        texts = self.getTexts()
        i = 0
        for text in texts:
            if text.lower().find(str.lower()) >= 0:
                return texts[i + plus]
            i = i + 1
        return None

    def getTextAfter(self, string, i=1):
        return self.getTextRelative(string, i)

    def getTextBefore(self, string, i=1):
        return self.getTextRelative(string, -i)

    def getRelFavIconList(self):
        list = []
        #--------------------------- NodeFilter filter = new TagNameFilter("link")
        #--------------------------------------------------------------------- try
            #--------- Node[] nodelist = parser.parse(filter).toNodeArray()
            #------------------------------------------- for (Node node : nodelist)
                #----------------------------------------------- Tag tag = (Tag)node
                    #------------------------------------ rel = tag.getAttribute("rel")
                #------------------------ if (rel.equalsIgnoreCase("SHORTCUT ICON"))
                        #----------------------------- list.add(tag.getAttribute("href"))
        #----------------------------------------------- catch (ParserException e)
            #-------------------------------------------------- e.printStackTrace()
        return list

    def getRelFavIcon(self):
        relFavIconList = self.getRelFavIconList()
        if len(relFavIconList) > 0:
            return relFavIconList[0]
        else:
            return None
            #// return "favicon.ico"

    def getFavIcon(self):
        ''' http://www.chami.com/tips/internet/110599I.html
        Method 1: "www.chami.com/favicon.ico"
        Method 2: LINK REL="SHORTCUT ICON" HREF="/~your_directory/logo.ico" '''
        relIco = self.getRelFavIcon()
        ico = None
        if not relIco:
            ico = self.concatUrl(self.getBaseUrl(), relIco)
        return ico

    def getFirstLink(self, regex):
        links = self.getLinks()
        for l in links:
            if re.match(regex, l):
                return l
        return None
