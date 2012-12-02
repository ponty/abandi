from abandi.exefinder import searchExe
from easyprocess import EasyProcess, extract_version, EasyProcessError
from abandi.iplugin import IPlugin


class Stella(IPlugin):
    hook = 'runner'
    name='stella'

    home_url = 'http://stella.sourceforge.net/'
    long_name = 'Stella'
    extensions = ['bin']
    platforms = ['atari2k6']
    ubuntu_package = 'stella'
    cmd_available = 'stella -help'

    def run_game(self, game):
        EasyProcess(['stella', searchExe(game.dir, game.name, self.extensions)]).call()

    def version(self):
        return extract_version(EasyProcess('stella -help').call().stdout)

    def available(self):
        try:
            EasyProcess(self.cmd_available).call()
            return True
        except EasyProcessError:
            return False
