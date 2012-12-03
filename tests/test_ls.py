from abandi.lsplugin import list_plugins
from abandi.lsrunner import list_runners
from abandi.lssrc import list_sources
from abandi.lsversion import list_versions
import unittest


class TestLs(unittest.TestCase):

    def test(self):
        list_versions()
        list_plugins()
        list_runners()
        list_sources()
