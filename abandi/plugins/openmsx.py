from easyprocess import extract_version
from abandi.exefinder import searchExe
from easyprocess import EasyProcess
from yapsy.IPlugin import IPlugin

EasyProcess('openmsx -v').check()


class openmsx(IPlugin):
    hook = 'runner'

    home_url = 'http://openmsx.sourceforge.net/'
    long_name = 'openMSX'
    extensions = ['cas,di1,di2,dsk,xsa,rom,wav']
    platforms = ['msx']
    ubuntu_package = 'openmsx'

    def run_game(self, game):
        EasyProcess(['openmsx' , searchExe(game.dir, game.name, self.extensions)]).call()
    def version(self):
        return extract_version(EasyProcess('openmsx -v').call().stdout)
