from abandi.exefinder import searchExe
from easyprocess import EasyProcess, extract_version, EasyProcessError
from abandi.iplugin import IPlugin


class openmsx(IPlugin):
    hook = 'runner'
    name = 'openmsx'

    home_url = 'http://openmsx.sourceforge.net/'
    long_name = 'openMSX'
    extensions = ['cas,di1,di2,dsk,xsa,rom,wav']
    platforms = ['msx']
    ubuntu_package = 'openmsx'
    cmd_available = 'openmsx -v'

    def run_game(self, game):
        EasyProcess(['openmsx', searchExe(game.dir, game.name,
                    self.extensions)]).call()

    def version(self):
        return extract_version(EasyProcess('openmsx -v').call().stdout)

    def available(self):
        try:
            EasyProcess(self.cmd_available).call()
            return True
        except EasyProcessError:
            return False
