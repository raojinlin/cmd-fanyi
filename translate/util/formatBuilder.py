from translate.util.baidu_response_format import *
from translate.util import get_plain_text


__all__ = ['BaiduFormatBuilder', 'YoudaoFormatBuilder']


class BaseFormatBuilder:
    def get_result(self) -> str: pass

    def __str__(self):
        return self.get_result()


class BaiduFormatBuilder(BaseFormatBuilder):
    def __init__(self):
        self.parts = {}

    def of_simple_means(self, simple):
        self.parts['simple'] = format_simple_means(simple)

        return self

    def of_oxford_entry(self, oxford):
        self.parts['oxford_entry'] = format_oxford_entry(oxford)

        return self

    def of_oxford_unbox(self, oxford):
        self.parts['ox_ford_unbox'] = format_oxford_unbox(oxford)
        return self

    def of_collins(self, collins):
        self.parts['collins'] = format_collins(collins)
        return self

    def of_double(self, double_data):
        self.parts['double'] = format_liju_double(double_data)
        return self

    def of_trans_result(self, trans_result):
        self.parts['trans_result'] = format_trans_result(trans_result)
        return self

    def _assembling(self, *keys, with_newline=True):
        result = ''
        for key in keys:
            if key in self.parts:
                value = self.parts[key]
                if with_newline:
                    value = with_new_line(value)
                result += value
        return result

    def get_result(self):
        return self._assembling('simple', 'oxford_entry', 'oxford_unbox', 'collins', 'double', 'trans_result')


class YoudaoFormatBuilder(BaseFormatBuilder):
    def __init__(self):
        self._parts = {}

    def of_phonetic_symbol(self, en, uk):
        res = ""
        if en:
            res += "    美式: \033[01m%s\033[0m\n" % en
        if uk:
            res += "    英式: \033[01m%s\033[0m\n" % uk

        if res:
            res = "发音:\n%s\n" % res

        self._parts['phonetic'] = res

        return self

    def of_english_chinese(self, data):
        if not data:
            self._parts['english_chinese'] = ''
            return self

        res = "英汉翻译:\n"
        trans1 = data['translation']
        for item in trans1:
            cont = ''
            if type(item) is dict:
                cont = item['content']
            else:
                cont = trans1[item]
            res += ("    " + cont + "\n")

        self._parts['english_chinese'] = res
        return self

    def of_web_interpretation(self, translation):
        if not translation:
            self._parts['interpretation'] = ''
            return self

        res = "\n网络释义:\n"
        for item in translation:
            if type(item) is not str:
                res += "    [%s]\n" % item['key']
            else:
                continue
            for t in item['trans']:
                if type(item['trans']) is list:
                    res += "        * %s\n" % get_plain_text(t['value'])
                else:
                    res += "        * %s\n" % get_plain_text(item['trans'][t])

        self._parts['interpretation'] = res
        return self

    def of_translation(self, translation):
        self._parts['translation'] = "%s\n" % get_plain_text(translation)
        return self

    def get_result(self):
        res = ''

        if 'translation' in self._parts:
            res += self._parts['translation']

        if 'phonetic' in self._parts:
            res += self._parts['phonetic']

        if 'english_chinese' in self._parts:
            res += self._parts['english_chinese']

        if 'interpretation' in self._parts:
            res += self._parts['interpretation']

        return res

