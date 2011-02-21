from abandi import version
from abandi.exefinder import searchExe
from easyprocess import EasyProcess
from yapsy.IPlugin import IPlugin


EasyProcess('zsnes -?').check()

class zsnes(IPlugin):
    hook = 'runner'

    long_name='ZSNES'
    home_url = 'http://www.zsnes.com/'

    # from help:
    extensions='SMC,SFC,SWC,FIG,MGD,MGH,UFO,BIN,GD3,GD7,USA,EUR,JAP,AUS,ST,BS,DX2,048,058,078,1,A,GZ,ZIP,JMA'.lower().split(',')

    platforms=['snes']
    ubuntu_package='zsnes'

    def run_game(self,game):
        EasyProcess('zsnes "%s"' % searchExe(game.dir, game.name, self.extensions)).call()
    def version(self):
        ''' no switch for version
        '''
        return 'unknown'
