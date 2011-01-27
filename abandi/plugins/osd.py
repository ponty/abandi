from abandi import WebParser
from abandi.game import Game
from yapsy.IPlugin import IPlugin
import logging

class Osd(IPlugin):
    hook='game_source'

    long_name = 'Old School DOS'
    homepage = 'http://www.oldschooldos.com/'
    max_game_id = 121
    icon = 'http://www.oldschooldos.com/images/header.gif'

    def __init__(self):
        self.all_links = None

    def parse_game(self, id):
        game = Game()

        game.id = id

        url = self.getGameHomePage(id)
        if not url:
            return None
        parser = WebParser.WebParser(url)
        game.homePageURL = url
        game.source = self.name
        self.parse(game, parser)
        if not game:
            return None

        if not game.name:
            return None
        return game

    def parse(self, game, parser):
        texts = parser.getTexts()
        game.name = (self.extractName(parser))

        game.size = (self.getTextWith(texts, "Size:"))
        game.releaseYear = (self.getTextWith(texts, "Year:"))
        game.genre = (self.getTextWith(texts, "DOS Games:"))
        game.programmer = (self.getTextWith(texts, "Maker:"))

        images = parser.getImages()
        game.screenshot_url_list = []
        for image in images   :
            if "/screens/" in image     :
                game.screenshot_url_list.append(image)
        game.screenshot_url_list = '|'.join(game.screenshot_url_list)

        links = parser.getLinks()
        for link in links   :
            if (link.endswith(".zip"))     :
                game.game_file_url = (link)
                break
        game.platform = 'dos'


    def extractName(self, parser):
        name = parser.getTextBefore("Maker:")
        if name:
            name = name.replace("\n", "").replace("\r", "").replace("  ", " ").replace("  ", " ")
            name = name.replace("  ", " ").replace("  ", " ").replace("  ", " ")
        return name


    def getTextWith(self, texts, key):
        # example:
        # Size: 30 KB
        for t in texts:
            if key in t:
                return t.replace(key, "").strip()
        return None

    def getGameHomePage(self, id):
        if id < 1:
            return None
        if not self.all_links:
            all = "http://www.oldschooldos.com/allgames.php"
            parser = WebParser.WebParser(all)
            all_links = parser.getLinks()
            all_links = filter((lambda x: 'www.oldschooldos.com' in x and 'action.php' not in x), all_links)
            first = "10thframebowling"
            full_first = filter((lambda x: first in x), all_links)[0]
            all_links = all_links [all_links.index(full_first):]
            all_links=['']+all_links
            logging.debug('found game links:' + '\n'.join([str(all_links.index(x))+':'+x for x in all_links]))
        return all_links[id]
