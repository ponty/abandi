from abandi import cli, version
from yapsy.IPlugin import IPlugin

class Unrar(IPlugin):
    hook = 'unpacker'

    def unpack(self, zip, target_dir):
        ''' unrar should be installed
        '''
        (stdout, _) = cli.call('unrar x -y {0} {1}'.format(zip,target_dir))
        ok = 'All OK'.lower() in stdout.lower()
        msg = None
        if not ok:
            msg = stdout
        return msg
    def version(self):
        (stdout,stderr) =cli.call('unrar')
        return version.extract_version(stdout)
