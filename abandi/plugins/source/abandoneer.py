from abandi.game import Game
from abandi.iplugin import IPlugin
import logging

class Abandoneer(IPlugin):
    hook='game_source'
    name='abandoneer'
    long_name='Abandoneer'
    homepage='http://www.abandoneer.com/'
    max_game_id=150
    icon='http://www.abandoneer.com/img/transparent.ico'
    platforms = ['dos']

    def __init__(self):
        from abandi import WebParser
        self.WebParser=WebParser
        
    def parse_game(self, id):
        game = Game()

        game.id = id

        url = self.getGameHomePage(id)
        if not url:
            return None
        parser = self.WebParser.WebParser(url)
        game.home_url = url
        game.source = self.name
        self.parse(game, parser)
        if not game:
            return None

        if not game.name:
            return None
        if game.genre:
            if game.genre.lower() == "applications":
                return None
        return game

    def parse(self, game, parser):
        game.name = parser.getTextBefore("Genre:")
        game.releaseYear = parser.getTextAfter("Year:")
        game.genre = parser.getTextAfter("Genre:")
        game.programmer = parser.getTextAfter("Developer:")
        game.screenshot_url_list = '|'.join(self.selectScreenshots(parser.getImages(), game.id))
        game.platform = 'dos'

    def selectScreenshots(self, images, id):
        # example: http://abandoneer.com/img/screenshots/lost_vikings.gif
        selected = [];
        for  image in images:
            if "/screenshots/" in image:
                selected.append(image);
        return selected;

    def getGameHomePage(self, id):
        return "http://abandoneer.com/games.php?gameid=" + str(id)

    def game_file_url(self, game):
        url = "http://abandoneer.com/download.php?gameid="+ str(game.id)
        parser = self.WebParser.WebParser(url,cached=False)
        game_file_url = parser.getFirstLink(".*\\.exe$")
        return game_file_url
