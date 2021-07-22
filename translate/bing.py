import requests
import re
import json

from translate.translator import Translator


class BingTransResult:
    def __init__(self, original='', pronunciation='', translation=None):
        if translation is None:
            translation = []
        self._original = original
        self._pronunciation = pronunciation
        self._translation = translation

    @classmethod
    def from_html(cls, html):
        original_result = re.search(r'<h4>(.+?)</h4>', html)
        pronunciation_result = re.search(r'<span class="ht_attr".+?>([^<]+?)</span>', html)
        pattern = re.compile(r'<span[^>]+?class=\"ht_pos\">([^<>\"]+?)</span>[^<]*?<span[^>]+?class=\"ht_trs\">([^<>]+?)</span>')
        translations = []

        for it in pattern.findall(html):
            translations.append({
                'pos': it[0],
                'trans': it[1]
            })

        original = original_result.group(1) if original_result else ''
        pronunciation = pronunciation_result.group(1) if pronunciation_result else ''
        return cls(original.strip(), pronunciation.strip(), translations)

    def set_original(self, original):
        self._original = original
        return self

    def get_original(self):
        return self._original

    def set_pronunciation(self, pronunciation):
        self._pronunciation = pronunciation
        return self

    def get_pronunciation(self):
        return self._pronunciation

    def set_translation(self, translation):
        self._translation = translation
        return self

    def get_translation(self):
        return self._translation

    def to_dict(self):
        return {
            'original': self.get_original(),
            'translation': self.get_translation(),
            'pronunciation': self.get_pronunciation()
        }


class Bing(Translator):
    def __init__(self):
        super(Bing, self).__init__()
        self._endpoint = 'https://cn.bing.com/dict/SerpHoverTrans'
        self._session = requests.session()
        self._result = None

    def get_name(self):
        return 'Bing'

    def get_result(self, *args, **kwargs):
        if not self._result:
            return None
        return self._result.to_dict()

    def query(self, text):
        with self._session.get(f"{self._endpoint}?q={text}") as ses:
            self._result = BingTransResult.from_html(ses.text)
        return self

    def format(self, verbose=0):
        if not self._result:
            return ''

        s = f"{self._result.get_original()} {self._result.get_pronunciation()}\n\n"
        for trans in self._result.get_translation():
            s += f"{trans.get('pos')} {trans.get('trans')}\n"

        return s.rstrip()

    def serialize(self, *args, **kwargs):
        r = self.get_result()
        if r:
            return json.dumps(r)
        else:
            return ''


if __name__ == '__main__':
    res = BingTransResult()
    print(res.get_original())
    print(res.get_pronunciation())
    print(res.get_translation())
