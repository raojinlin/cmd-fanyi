import unittest

from translate.factory import get_translator

youdao = get_translator('youdao')


class YoudaoTest(unittest.TestCase):
    def test_query(self):
        youdao.query('hello')
        self.assertTrue('发音' in youdao.format())
        self.assertTrue('helˈō' in youdao.format())
        self.assertTrue('həˈləʊ' in youdao.format())
        self.assertTrue('英汉翻译' in youdao.format())
        self.assertTrue('表示问候， 惊奇或唤起注意时的用语' in youdao.format())
        self.assertTrue('网络释义' in youdao.format(1))
        self.assertTrue('Hello Kitty' in youdao.format(1))
