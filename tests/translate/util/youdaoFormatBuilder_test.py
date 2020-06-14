import unittest
import json

from os.path import dirname, join
from translate.util import formatBuilder


class FormatBuilderTest(unittest.TestCase):
    def test_youdao_format(self):
        with open(join(dirname(__file__), '../../../resources/youdao_response.json'), 'rt') as f:
            youdao_result = json.loads(f.read())

        builder = formatBuilder.YoudaoFormatBuilder()
        self.assertTrue(builder.get_result() == "")

        builder.of_phonetic_symbol(youdao_result.get('us-phonetic-symbol', ''), youdao_result.get('uk-phonetic-symbol', ''))
        self.assertTrue('发音' in builder.get_result())
        self.assertTrue('美式' in builder.get_result())
        self.assertTrue('英式' in builder.get_result())

        builder.of_english_chinese(youdao_result['custom-translation'])
        self.assertTrue('英汉翻译' in builder.get_result())
        self.assertTrue('n. 表示问候， 惊奇或唤起注意时的用语' in builder.get_result())

        builder.of_web_interpretation(youdao_result.get('yodao-web-dict').get('web-translation'))
        self.assertTrue('网络释义' in builder.get_result())
        self.assertTrue('Hello' in builder.get_result())
        self.assertTrue('Hello Kitty' in builder.get_result())
        self.assertTrue('Hello Bebe' in builder.get_result())

    def test_youdao_translation_format(self):
        with open(join(dirname(__file__), '../../../resources/youdao_translation.json'), 'rt') as f:
            youdao_translation_result = json.loads(f.read())

        builder = formatBuilder.YoudaoFormatBuilder()
        builder.of_translation(youdao_translation_result['translation'])
        self.assertTrue('TCP实现将遵循稳健性的一般原则:保守在你做什么,在你接受别人的自由。' in builder.get_result())
