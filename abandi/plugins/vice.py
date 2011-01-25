from abandi.cli import call
from abandi.exefinder import searchExe
from yapsy.IPlugin import IPlugin

class Vice(IPlugin):
    hook = 'runner'

    long_name = 'VICE'
    extensions = ['t64', 'd64', 'prg']
    platforms = ['c64']
    ubuntu_package = 'vice'

    def run_game(self, game):
        call('x64 %s' % searchExe(game.dir, game.name, self.extensions))
    def version(self):
        ''' no switch for version
        '''
        (stdout, stderr) = call('x64 -h')
        v =  None if stderr.strip() else 'unknown'
        return v
