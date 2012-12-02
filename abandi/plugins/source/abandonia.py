
from abandi.downloader import Downloader
from abandi.game import Game
from abandi.iplugin import IPlugin
import logging
from abandi import config


class Abandonia(IPlugin):
    hook = 'game_source'
    name = 'abandonia'

    long_name = 'Abandonia'
    homepage = 'http://www.abandonia.com/'
    max_game_id = 1100
    icon = ''
    platforms = ['dos', 'win']

    def __init__(self):
        from abandi import WebParser
        self.WebParser = WebParser

    def parse_game(self, id):
        game = Game()

        game.id = id

        url = self.getGameHomePage(id)
        if not url:
            return None
        parser = self.WebParser.WebParser(url)

        # buy it!
        all_images = '|'.join(parser.getImages())
        if 'buy' in all_images.lower():
            return None
        if 'protected' in all_images.lower():
            return None

        game.home_url = url
        game.source = self.name
        self.parse(game, parser)
        if not game:
            return None

        if not game.name:
            return None
        # example: http://www.abandonia.com/en/games/248/index.html
        if game.name.lower == "download":
            return None

        return game

    def parse(self, game, parser):
        game.name = parser.getTextBefore("Producer")
        game.releaseYear = parser.getTextAfter("Year")
        # game.genre =
        # game.programmer =
        # game.setSize(parser.getTextAfter("Size:"));
        game.publisher = parser.getTextAfter("publisher")
        game.screenshot_url_list = '|'.join(self.selectScreenshots(parser.getImages(), game.id))
        if "bootdisk" in parser.getImages():
            game.platform = 'dos'
        elif "dosbox" in parser.getImages():
            game.platform = 'dos'
        elif "winxp" in parser.getImages():
            game.platform = 'win'
        else:
            game.platform = 'dos'


    def selectScreenshots(self, images, id):
        # example: /files/games/352/Daughter of Serpents_7.jpg
        selected = []
        for  image in images:
            if "games/" + str(id) + "/" in image:
                selected.append(image)
        return selected

    def getGameHomePage(self, id):
        return "http://www.abandonia.com/en/games/" + str(id) + "/index.html"

    def download_options(self, game):
        parent = "http://www.abandonia.com/en/downloadgame/" + str(game.id) + "/index.html"
        downloadOptions = dict(useSessionCookie=True, referer=parent)
        return downloadOptions

    def game_file_url(self, game):
        parent = "http://www.abandonia.com/en/downloadgame/" + str(game.id) + "/index.html"

        # old
        # parser = WebParser.WebParser(parent, cached=False)
        # game_file_url = parser.getFirstLink(".*files.abandonia.com/download.*")

        # example:
#        function go_to_downloadGame()
#        {
#            window.open("http://files.abandonia.com/download.php?game=Return+to+Ringworld&amp;secure=52f031ad8496c642cbbac42baf293a1c&amp;td=1347598121");
#        }

        fname = Downloader(cached=False).download(parent, config.CACHE)
        page = open(fname).read()
        s = page.split('go_to_downloadGame')[1]
        game_file_url = s.split('"')[1]
        return game_file_url
