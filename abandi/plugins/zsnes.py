from abandi import version
from abandi.cli import call
from abandi.exefinder import searchExe
from yapsy.IPlugin import IPlugin



class zsnes(IPlugin):
    hook = 'runner'

    long_name='zsnes'

    # from help:
    extensions='SMC,SFC,SWC,FIG,MGD,MGH,UFO,BIN,GD3,GD7,USA,EUR,JAP,AUS,ST,BS,DX2,048,058,078,1,A,GZ,ZIP,JMA'.lower().split(',')

    platforms=['snes']
    ubuntu_package='zsnes'

    def run_game(self,game):
        (stdout,stderr) =call('zsnes "%s"' % searchExe(game.dir, game.name, self.extensions))
    def version(self):
        ''' no switch for version
        '''
        (stdout, stderr) = call('zsnes -?')
        v =  None if stderr.strip() else 'unknown'
        return v
