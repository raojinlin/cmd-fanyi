import unittest

from translate.youdao import Youdao
from translate.baidu import Baidu
from translate import factory


class FactoryTest(unittest.TestCase):
    def test_get_instance(self):
        """translator factory test"""
        self.assertTrue(isinstance(factory.get_translator('youdao'), Youdao))
        self.assertTrue(isinstance(factory.get_translator('baidu'), Baidu))
        try:
            factory.get_translator('xxxx')
        except factory.InvalidTranslatorException:
            pass
