
from abandi.iplugin import IPlugin
from abandi.game import Game
import logging

log = logging.getLogger(__name__)


class Gamebase64(IPlugin):
    hook = 'game_source'
    name = 'gb64'

    long_name = 'Gamebase 64'
    homepage = 'http://www.gamebase64.com'
    max_game_id = 22000
    platforms = ['c64']

    def __init__(self):
        from abandi import WebParser
        self.WebParser = WebParser

    def parseLinks(self, game, parser):
        game.name = parser.getTextAfter("progress")
        game.releaseYear = parser.getTextAfter("published")
        game.publisher = parser.getTextAfter("published", 2)
        game.musician = self.checkIfReal(parser.getTextAfter("musician"))
        game.programmer = self.checkIfReal(parser.getTextAfter("programmer"))
        game.language = parser.getTextAfter("language")
        game.genre = parser.getTextAfter("genre")

        for text in parser.getLinks():
            if (text.endswith(".zip")):
                game.game_file_url = text
            if (text.endswith(".sid")):
                game.music_file_url = text

    def checkIfReal(self, text):
        ''' filters NONE,UNKNOWN,.. out '''
        if not text:
            return None

        low = text.lower()
        if "none" not in low and "unknown" not in low:
            return text

        return None

    def selectScreenshots(self, images, id):
        selected = []
        for image in images:
            if image.endswith(".png"):
                if not image in selected:
                    selected.append(image)
        return selected

    def parse_game(self, id):
        game = Game()

        game.id = id

        url = self.getGameHomePage(id)
        parser = self.WebParser.WebParser(url)
        game.home_url = url
        game.source = self.name
        self.parseLinks(game, parser)

        game.screenshot_url_list = '|'.join(self.selectScreenshots(parser.getImages(), id))

        if not game or not game.name or "Banner Exchange" in game.name:
            return None
        if not game.game_file_url:
            log.debug('no file to download for "%s"' % game.name)
            return None

        game.platform = 'c64'
        return game

    def getGameHomePage(self, id):
        url = "http://www.gamebase64.com/game.php?id=" + str(id)
        return url
