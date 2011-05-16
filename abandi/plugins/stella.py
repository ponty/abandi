from easyprocess import extract_version
from abandi.exefinder import searchExe
from easyprocess import EasyProcess
from yapsy.IPlugin import IPlugin

EasyProcess('stella -help').check()


class Stella(IPlugin):
    hook = 'runner'

    home_url = 'http://stella.sourceforge.net/'
    long_name = 'Stella'
    extensions = ['bin']
    platforms = ['atari2k6']
    ubuntu_package = 'stella'

    def run_game(self, game):
        EasyProcess(['stella', searchExe(game.dir, game.name, self.extensions)]).call()
    def version(self):
        return extract_version(EasyProcess('stella -help').call().stdout)
