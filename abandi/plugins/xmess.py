from abandi import version
from abandi.exefinder import searchExe
from yapsy.IPlugin import IPlugin

# not working in ubuntu

#class xmess(IPlugin):
#    hook = 'runner'
#
#    long_name='xmess'
#    extensions=['bin']
#    platforms='atari2k6 nes snes megadrive gb c64 c128 msx'.split()
#    ubuntu_package='xmess-sdl'
#
#    def run_game(self,game):
#        (stdout,stderr) =call('xmess %s' % searchExe(game.dir, game.name, self.extensions))
#    def version(self):
#        (stdout,stderr) =call('xmess -help')
#        return version.extract_version(stdout)
