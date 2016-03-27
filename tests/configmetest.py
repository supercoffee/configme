__author__ = 'ben'

from configme import configme
import unittest
from os import path

class MyTestCase(unittest.TestCase):
    def test_get_template_path(self):
        default_path = configme.resolve_dir()
        self.assertTrue(path.isabs(default_path))
        self.assertTrue(path.exists(default_path))

        custom_path = configme.resolve_dir('/usr/local/bin')
        self.assertTrue(path.isabs(default_path))
        self.assertTrue(path.exists(custom_path))

        rel_path = configme.resolve_dir('../tests')
        self.assertTrue(path.isabs(rel_path))
        self.assertTrue(path.exists(rel_path))


if __name__ == '__main__':
    unittest.main()
