from abandi import WebParser, game_platform
from abandi.game import Game
from yapsy.IPlugin import IPlugin

class Oscomp(IPlugin):
    hook='game_source'

    long_name = 'Oldschool Computer'
    homepage = 'http://oscomp.hu/'
    max_game_id = 1230
    icon = 'http://oscomp.hu/sys/img/hdr.jpg'
    # TODO: check all
    platforms = 'dos c64 c128 cplus4 msx megadrive mastersystem gb atari2k6 nes snes amiga'.split()

    def parse_game(self, id):
        game = Game()

        game.id = id

        url = self.getGameHomePage(id)
        parser = WebParser.WebParser(url)
        game.homePageURL = url
        game.source = self.name
        self.parse(game, parser)

        if not game:
            return None

        if not game.name:
            return None

        if (game.genre.lower()==("emulator")):
            return None

        if (game.genre.lower()==("operation system")):
            return None

        if (game.genre.lower()==("music")):
            return None

        if (game.genre.lower()==("utilities")):
            return None

        if (game.genre.lower()==("document")):
            return None

        return game

    def parse(self, game, parser):
        game.name = (parser.getTextBefore("Platform"))

        game.size = (parser.getTextAfter("File size"))
        game.releaseYear = (parser.getTextAfter("Release"))
        game.genre = (parser.getTextAfter("Category"))
        game.programmer = (parser.getTextAfter("Author"))

        # FIXME
        game.screenshot_url_list = "http://oscomp.hu/img.php?" + str(game.id)

        game.game_file_url = ("http://oscomp.hu/dlgame.php?" + str(game.id))

        parsedPlatform = parser.getTextAfter("Platform")
        game.platform = game_platform.id(parsedPlatform)


    def getGameHomePage(self, id):
        url = "http://oscomp.hu/?lang/en&details/" + str(id)
        return url

    def download_options(self, game):
        downloadOptions = dict(useSessionCookie=True, referer=game.homePageURL)
        return downloadOptions
