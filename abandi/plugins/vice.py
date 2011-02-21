from abandi.exefinder import searchExe
from easyprocess import EasyProcess
from yapsy.IPlugin import IPlugin

EasyProcess('x64 -h').check()

class Vice(IPlugin):
    hook = 'runner'

    long_name = 'VICE'
    home_url = 'http://www.viceteam.org/'
    extensions = ['t64', 'd64', 'prg']
    platforms = ['c64']
    ubuntu_package = 'vice'

    def run_game(self, game):
        EasyProcess('x64 %s' % searchExe(game.dir, game.name, self.extensions)).call()
    def version(self):
        ''' no switch for version
        '''
        return 'unknown'
