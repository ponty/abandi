from abandi.iplugin import IPlugin


class Soup(IPlugin):
    hook = 'html_parser'
    name = 'soup'

    def __init__(self):
        self.parser = None
        import BeautifulSoup
        self.BeautifulSoup = BeautifulSoup

    def set_html(self, html):
        self.parser = self.BeautifulSoup.BeautifulSoup(html)

    def images(self):
        if self.parser is None:
            return
        ls = []
        elems = self.parser.findAll('img')

        for e in elems:
            src = e["src"]
            ls.append(src)
        return ls

    def links(self):
        if self.parser is None:
            return
        links = []
        elems = self.parser.findAll('a')
        for e in elems:
            href = e["href"]
            links.append(href)
        return links

    def texts(self):
        if self.parser is None:
            return
        texts = []
        elems = self.parser.findAll(text=True)
        for text in elems:
            if str(text.__class__) != "<class 'BeautifulSoup.Comment'>":
                # if (!(node.getParent() instanceof StyleTag))
                if text.strip():
                    texts.append(text)
        return texts

    def version(self):
        return self.BeautifulSoup.__version__
