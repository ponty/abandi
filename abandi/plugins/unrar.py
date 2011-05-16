from easyprocess import extract_version
from easyprocess import EasyProcess
from yapsy.IPlugin import IPlugin

# TODO: other method
#EasyProcess('unrar').check()

class Unrar(IPlugin):
    hook = 'unpacker'

    def unpack(self, zip, target_dir):
        ''' unrar should be installed
        '''
        p = EasyProcess(['unrar', 'x', '-y', zip, target_dir]).call()
        if p.return_code:
            return p.stdout
    def version(self):
        return extract_version(EasyProcess('unrar').call().stdout)
