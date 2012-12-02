from abandi.iplugin import IPlugin


class Lxml(IPlugin):
    '''
    exception in   gb64 1002
    '''
    hook='html_parser'
    name='lxml'
    
    def __init__(self):
        self.parser = None
        self.alllinks = None
        from lxml.html import fromstring
        self.fromstring = fromstring
        
    def set_html(self, html):
        self.parser = self.fromstring(html)
        self.alllinks = list(self.parser.iterlinks())

    def images(self):
        if self.parser is  None:
            return
        list = []
        for a, b, src, _ in  self.alllinks:
            if a.tag == 'img' and b == 'src':
                list.append(src)
        return list

    def links(self):
        if self.parser is  None:
            return
        links = []
        for a, b, href, _ in  self.alllinks:
            if a.tag == 'a' and b == 'href':
                links.append(href)
        return links

    def texts(self):
        if self.parser is  None:
            return
        texts = []
        elems = filter(len, map((lambda s:s.strip()), self.parser.xpath("//text()")))
        for text in elems:
            if text:
                texts.append(text)
        return texts
