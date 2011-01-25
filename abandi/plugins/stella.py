from abandi import version
from abandi.cli import call
from abandi.exefinder import searchExe
from yapsy.IPlugin import IPlugin



class Stella(IPlugin):
    hook = 'runner'

    long_name='stella'
    extensions=['bin']
    platforms=['atari2k6']
    ubuntu_package='stella'

    def run_game(self,game):
        (stdout,stderr) =call('stella %s' % searchExe(game.dir, game.name, self.extensions))
    def version(self):
        (stdout,stderr) =call('stella -help')
        return version.extract_version(stdout)
