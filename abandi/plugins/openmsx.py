from abandi import version
from abandi.cli import call
from abandi.exefinder import searchExe
from yapsy.IPlugin import IPlugin



class openmsx(IPlugin):
    hook = 'runner'

    home_url = 'http://openmsx.sourceforge.net/'
    long_name='openMSX'
    extensions=['cas,di1,di2,dsk,xsa,rom,wav']
    platforms=['msx']
    ubuntu_package='openmsx'

    def run_game(self,game):
        (stdout,stderr,_) =call('openmsx %s' % searchExe(game.dir, game.name, self.extensions))
    def version(self):
        (stdout,stderr,_) =call('openmsx -v')
        return version.extract_version(stdout)
