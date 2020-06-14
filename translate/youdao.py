import re
import json
import xml.etree.ElementTree as xmlElementTree

from urllib import request
from urllib import parse
from translate.util import QueryString
from translate.translator import Translator
from xml2dict import parser as xml2dict
from translate.util.formatBuilder import YoudaoFormatBuilder


class Youdao(Translator):
    def __init__(self):
        super().__init__()

        self.keyfrom = 'chrome.extension'
        self.doctype = 'xml'
        self.dogVersion = '1.0'
        self.xmlVersion = '3.2'
        self.appVer = "3.1.17.4208"
        self.client = 'deskdict'
        self.version = 2.1
        self._result = None
        self._last_query = ''

        self.api_list = {
            'fsearch': {
                'url': 'http://dict.youdao.com/fsearch',
                'data': {
                    "client": self.client,
                    "keyfrom": self.keyfrom,
                    "pos": -1,
                    "doctype": self.doctype,
                    "xmlVersion": self.xmlVersion,
                    "dogVersion": self.dogVersion,
                    "appVer": self.appVer,
                    "le": "eng",
                    "q": None,
                }
            },
            'translate': {
                'url': 'http://fanyi.youdao.com/translate',
                'data': {
                    "client": self.client,
                    "keyfrom": self.keyfrom,
                    "xmlVersion": "1.1",
                    "dogVersion": self.dogVersion,
                    "ue": "utf-8",
                    "version": self.version,
                    "doctype": self.doctype,
                    "i": None,
                    'form': 'AUTO',
                    'to': 'AUTO',
                }
            }
        }

    def do_request(self, url):
        req = request.Request(url, headers={'User-Agent': self.user_agent})
        res = request.urlopen(req)

        if res.status == 200:
            xmldom = xmlElementTree.parse(res)
            return xml2dict(xmldom)

    def fsearch(self, word):
        api = self.api_list['fsearch']

        api['data']['q'] = parse.quote(word)
        return self.do_request(api['url'] + '?' + QueryString.stringify(api['data']))

    def translate(self, text):
        api = self.api_list['translate']

        api['data']['i'] = parse.quote(text)
        return self.do_request(api['url'] + '?' + QueryString.stringify(api['data']))

    def query(self, text):
        if self._last_query != '' and self._last_query == text:
            return self

        self._last_query = text 
        chinese_regex = r'[\u4e00-\u9fa5]'
        words = re.findall(r'\w+', text)

        if re.match(chinese_regex, text):
            words = re.findall(chinese_regex, text)

        if len(words) > 4:
            self._result = self.translate(text)
        else:
            self._result = self.fsearch(text)

        return self

    def get_result(self):
        return self._result

    def serialize(self):
        if self.get_result() is None:
            return ""

        return json.dumps(self.get_result())

    def get_english_chinese(self):
        return self.get_result().get('custom-translation')

    def get_web_interpretation(self):
        return self.get_result().get('yodao-web-dict')

    def format(self, verbose=0):
        builder = YoudaoFormatBuilder()
        if 'translation' in self.get_result():
            builder.of_translation(self.get_result().get('translation'))

        builder.of_phonetic_symbol(
            self.get_result().get("us-phonetic-symbol", ""),
            self.get_result().get("uk-phonetic-symbol", "")
        )

        if self.get_english_chinese():
            builder.of_english_chinese(self.get_english_chinese())

        if self.get_web_interpretation() and verbose >= 1:
            builder.of_web_interpretation(self.get_web_interpretation().get('web-translation'))

        return builder.get_result()

    def get_name(self):
        return "Youdao"


