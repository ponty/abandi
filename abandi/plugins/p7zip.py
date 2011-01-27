from abandi import cli, version
from yapsy.IPlugin import IPlugin

class P7zip(IPlugin):
    hook = 'unpacker'

    def unpack(self, zip, target_dir):
        ''' 7z should be installed
        '''
        (stdout, _,_) = cli.call('7z e -o' + target_dir + ' -r -y ' + zip)
        ok = 'Everything is OK'.lower() in stdout.lower()
        msg = None
        if not ok:
            msg = stdout
        return msg
    def version(self):
        (stdout,stderr,_) =cli.call('7z')
        return version.extract_version(stdout)
