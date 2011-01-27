from abandi import cli
from yapsy.IPlugin import IPlugin

class patool(IPlugin):
    hook = 'unpacker'

    def unpack(self, zip, target_dir):
        ''' patool should be installed
        '''
        (_, _, r) = cli.call('patool extract {0} --outdir {1}'.format(zip,target_dir))
        return r==0

    def version(self):
        (stdout,stderr, _) =cli.call('patool')
        if not stderr.split():
            return 'unknown'
