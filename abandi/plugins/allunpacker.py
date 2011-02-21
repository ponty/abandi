from abandi import unpacker
from yapsy.IPlugin import IPlugin

class Allunpacker(IPlugin):
    hook = 'unpacker'

    def unpack(self, zip, target_dir):
        '''
        '''
        ls = unpacker.unpackers()
        ls = [x for x in ls if x.name != 'allunpacker']

        allmsg = ''
        for x in ls:
            msg = x.unpack(zip, target_dir)
            if not msg:
                return
            allmsg +=msg
        return allmsg
