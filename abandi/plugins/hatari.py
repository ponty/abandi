from abandi import version
from abandi.cli import call
from abandi.exefinder import searchExe
from yapsy.IPlugin import IPlugin



class hatari(IPlugin):
    hook = 'runner'

    name='hatari'
    extensions=['bin']
    platforms=['atari2k6']
    ubuntu_package='hatari'

    def run_game(self,game):
        (stdout,stderr) =call('hatari %s' % searchExe(game.dir, game.name, self.extensions))
    def version(self):
        (stdout,stderr) =call('hatari -v')
        return version.extract_version(stdout)
