import unittest
import os
from anastasiaplugins.anastasiaplugins import PluginBase

class TestAnistasiaPlugins(unittest.TestCase):
    def setUp(self):
        conf_file = "conf/test_conf.ini"
        test_conf = os.path.abspath(os.path.join(os.path.dirname(__file__), conf_file))
        print(test_conf)
        self.context = {}
        self.plugin_handler = PluginBase(conf_file, self.context)
        print(self.plugin_handler.conf.sections())


    def test_example(self):
        self.assertTrue(self.context.get("test_one"))


if __name__ == "__main__":
    unittest.main()