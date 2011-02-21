from easyprocess import EasyProcess
from yapsy.IPlugin import IPlugin

EasyProcess('patool').check()

class patool(IPlugin):
    hook = 'unpacker'

    def unpack(self, zip, target_dir):
        ''' patool should be installed
        '''
        p = EasyProcess(['patool', 'extract', zip, '--outdir', target_dir]).call()
        return p.return_code==0

    def version(self):
        return 'unknown'
