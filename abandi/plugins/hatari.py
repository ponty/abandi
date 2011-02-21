from abandi import version
from abandi.exefinder import searchExe
from easyprocess import EasyProcess
from yapsy.IPlugin import IPlugin


EasyProcess('hatari -v').check()

class hatari(IPlugin):
    hook = 'runner'

    long_name = 'Hatari'
    home_url = 'http://hatari.berlios.de/'
    extensions = ['bin']
    platforms = ['atari2k6']
    ubuntu_package = 'hatari'

    def run_game(self, game):
        EasyProcess(['hatari', searchExe(game.dir, game.name, self.extensions)]).call()
    def version(self):
        return version.extract_version(EasyProcess('hatari -v').call().stdout)
