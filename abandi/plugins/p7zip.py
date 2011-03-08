from abandi import version
from easyprocess import Proc
from yapsy.IPlugin import IPlugin

Proc('7z').check()


class P7zip(IPlugin):
    hook = 'unpacker'

    def unpack(self, zip, target_dir):
        ''' 7z should be installed
        '''
        p = Proc(['7z', 'e', '-o' + target_dir , '-r', '-y', zip]).call()
        if p.return_code:
            return p.stdout

    def version(self):
        return version.extract_version(Proc('7z').call().stdout)
