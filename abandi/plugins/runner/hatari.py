from abandi.exefinder import searchExe
from easyprocess import EasyProcess, extract_version, EasyProcessError
from abandi.iplugin import IPlugin


class hatari(IPlugin):
    hook = 'runner'
    name='hatari'

    long_name = 'Hatari'
    home_url = 'http://hatari.berlios.de/'
    extensions = ['bin']
    platforms = ['atari2k6']
    ubuntu_package = 'hatari'
    cmd_available = 'hatari -v'

    def run_game(self, game):
        EasyProcess(['hatari', searchExe(game.dir, game.name, self.extensions)]).call()

    def version(self):
        return extract_version(EasyProcess('hatari -v').call().stdout)

    def available(self):
        try:
            EasyProcess(self.cmd_available).call()
            return True
        except EasyProcessError:
            return False
