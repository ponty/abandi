from abandi.exefinder import searchExe
from easyprocess import EasyProcess, extract_version, EasyProcessError
from os.path import dirname, basename
from abandi.iplugin import IPlugin


class Dosbox(IPlugin):
    hook = 'runner'
    name='dosbox'

    long_name = 'DOSBox'
    home_url = 'http://www.dosbox.com/'
    extensions = ['exe', 'bat', 'com']
    platforms = ['dos']
    ubuntu_package = 'dosbox'
    cmd_available = 'dosbox -version'

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

    def available(self):
        try:
            EasyProcess(self.cmd_available).call()
            return True
        except EasyProcessError:
            return False
