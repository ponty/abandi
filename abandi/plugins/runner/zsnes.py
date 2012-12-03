from abandi.exefinder import searchExe
from easyprocess import EasyProcess, EasyProcessError
from abandi.iplugin import IPlugin


class zsnes(IPlugin):
    hook = 'runner'
    name = 'zsnes'

    long_name = 'ZSNES'
    home_url = 'http://www.zsnes.com/'

    # from help:
    extensions = 'SMC,SFC,SWC,FIG,MGD,MGH,UFO,BIN,GD3,GD7,USA,EUR,JAP,AUS,ST,BS,DX2,048,058,078,1,A,GZ,ZIP,JMA'.lower().split(',')

    platforms = ['snes']
    ubuntu_package = 'zsnes'
    cmd_available = 'zsnes -?'

    def run_game(self, game):
        EasyProcess(
            ['zsnes', searchExe(game.dir, game.name, self.extensions)]).call()

    def version(self):
        ''' no switch for version
        '''
        return 'unknown'

    def available(self):
        try:
            EasyProcess(self.cmd_available).call()
            return True
        except EasyProcessError:
            return False
