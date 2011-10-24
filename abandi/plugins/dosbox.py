from easyprocess import extract_version
from abandi.exefinder import searchExe
from easyprocess import EasyProcess
from os.path import dirname, basename
from yapsy.IPlugin import IPlugin

EasyProcess('dosbox -version').check()

class Dosbox(IPlugin):
    hook = 'runner'

    long_name = 'DOSBox'
    home_url = 'http://www.dosbox.com/'
    extensions = ['exe', 'bat', 'com']
    platforms = ['dos']
    ubuntu_package = 'dosbox'

    def run_game(self, game):
        gameExe = searchExe(game.dir, game.name, self.extensions)
        command = ['dosbox', 
                   '-exit',
                   '-c', "mount c " + dirname(gameExe), 
                   '-c', 'c:', 
                   '-c', basename(gameExe)
                   ]
        EasyProcess(command).call()
    def version(self):
        return extract_version(EasyProcess('dosbox -version').call().stdout)
