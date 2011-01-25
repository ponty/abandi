from abandi import version
from abandi.cli import call
from abandi.exefinder import searchExe
from yapsy.IPlugin import IPlugin



class openmsx(IPlugin):
    hook = 'runner'

    long_name='openmsx'
    extensions=['cas,di1,di2,dsk,xsa,rom,wav']
    platforms=['msx']
    ubuntu_package='openmsx'

    def run_game(self,game):
        (stdout,stderr) =call('openmsx %s' % searchExe(game.dir, game.name, self.extensions))
    def version(self):
        (stdout,stderr) =call('openmsx -v')
        return version.extract_version(stdout)
