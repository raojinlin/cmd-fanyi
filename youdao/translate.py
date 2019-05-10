import xml.etree.ElementTree as xmlElementTree

from youdao.utils import QueryString, get_plain_text
from urllib.request import Request, urlopen
from urllib.parse import quote
from xml2dict import parser as xml2dict


class Translate:
    translate_api = 'http://fanyi.youdao.com/translate'
    dict_api = 'http://dict.youdao.com/fsearch'

    dict_params = {
        "client": "deskdict",
        "keyfrom": "chrome.extension",
        "pos": -1,
        "doctype": "xml",
        "xmlVersion": 3.2,
        "dogVersion": 1.0,
        "appVer": "3.1.17.4208",
        "le": "eng",
        "q": None
    }

    translate_params = {
        "client": "deskdict",
        "keyfrom": "chrome.extension",
        "xmlVersion": "1.1",
        "dogVersion": "1.0",
        "ue": "utf-8",
        "version": 2.1,
        "doctype": "xml",
        "i": None,
        'form': 'AUTO',
        'to': 'AUTO'
    }

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/73.0.3683.86 Safari/537.36 "

    def __init__(self, word: str):
        self.word = quote(word)
        self.xml_dom = None
        self._result = {}

    def get_result(self):
        return self._result

    def query(self, word=""):
        """
        The word query
        :type word: str
        :return:
        """
        if word:
            self.word = quote(word)
        req = Request(self.get_translate_url(), headers={"User-Agent": self.user_agent})
        res = urlopen(req)

        if res.status == 200:
            self.xml_dom = xmlElementTree.parse(res)
            self._result = xml2dict(self.xml_dom)

    def translate(self, text=None):
        """
        Literal translation
        :param text:
        :type text: str
        :return:
        """
        if text:
            self.word = text
        req = Request(self.get_translate_url(True), headers={"User-Agent": self.user_agent})
        res = urlopen(req)

        if res.status == 200:
            self.xml_dom = xmlElementTree.parse(res)
            self._result = xml2dict(self.xml_dom)

    def get_translate_url(self, translate=False):
        api = self.dict_api
        params = self.dict_params
        if translate:
            self.translate_params["i"] = self.word
            api = self.translate_api
            params = self.translate_params
        else:
            self.dict_params["q"] = self.word

        return "%(api)s?%(params)s" % {"api": api, "params": QueryString.stringify(params)}

    def english_chinese(self):
        key = 'custom-translation'
        return self.get_result().get(key, None)

    def web_interpretation(self):
        key = 'yodao-web-dict'
        return self.get_result().get(key, None)

    def get_translate_result(self):
        res = ''
        if 'translation' in self.get_result():
            # res += ("input: %s\n" % get_plain_text(self.get_result()['input']))
            res += ("%s\n" % get_plain_text(self.get_result()['translation']))
            return res

        if self.english_chinese():
            res += "英汉翻译:\n"
            trans1 = self.english_chinese()['translation']
            for item in trans1:
                cont = ''
                if type(item) is dict:
                    cont = item['content']
                else:
                    cont = trans1[item]
                res += ("\t" + cont + "\n")

        if self.web_interpretation():
            res += "\n网络释义:\n"
            translation = self.web_interpretation()['web-translation']
            for item in translation:
                res += "\t[%s]\n" % item['key']
                if type(item['trans']) is list:
                    for t in item['trans']:
                        res += "\t\t%s\n" % get_plain_text(t['value'])
                else:
                    for t in item['trans']:
                        res += "\t\t%s\n" % get_plain_text(item['trans'][t])
        return res

    def __str__(self):
        return "\033[33m%s\033[0m" % self.get_translate_result()


if __name__ == '__main__':
    trans = Translate("test")
    trans.query()
    print(trans)


