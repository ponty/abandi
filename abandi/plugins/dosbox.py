from abandi import cli, version
from abandi.cli import call
from abandi.exefinder import searchExe
from os.path import dirname, basename
from yapsy.IPlugin import IPlugin

class Dosbox(IPlugin):
    hook='runner'

    name='dosbox'
    extensions=['exe','bat','com']
    platforms=['dos']
    ubuntu_package='dosbox'

    def run_game(self,game):
        gameExe = searchExe(game.dir, game.name, self.extensions)
        vars = (dirname(gameExe), basename(gameExe))
        command = 'dosbox -c "mount c %s" -c c: -c %s' % vars
        cli.call(command)
    def version(self):
        (stdout,stderr) =call('dosbox -version')
        return version.extract_version(stdout)
