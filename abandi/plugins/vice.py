from abandi.exefinder import searchExe
from easyprocess import EasyProcess, EasyProcessError
from yapsy.IPlugin import IPlugin


class Vice(IPlugin):
    hook = 'runner'

    long_name = 'VICE'
    home_url = 'http://www.viceteam.org/'
    extensions = ['t64', 'd64', 'prg']
    platforms = ['c64']
    ubuntu_package = 'vice'
    cmd_available = 'x64 -h'

    def run_game(self, game):
        EasyProcess(['x64', searchExe(game.dir, game.name, self.extensions)]).call()

    def version(self):
        ''' no switch for version
        '''
        return 'unknown'

    def available(self):
        try:
            EasyProcess(self.cmd_available).call()
            return True
        except EasyProcessError:
            return False
