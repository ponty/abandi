from abandi import version
from easyprocess import EasyProcess
from yapsy.IPlugin import IPlugin

EasyProcess('7z').check()


class P7zip(IPlugin):
    hook = 'unpacker'

    def unpack(self, zip, target_dir):
        ''' 7z should be installed
        '''
        p = EasyProcess('7z e -o' + target_dir + ' -r -y ' + zip).call()
        if p.return_code:
            return p.stdout

    def version(self):
        return version.extract_version(EasyProcess('7z').call().stdout)
