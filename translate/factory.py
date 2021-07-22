from translate.youdao import Youdao
from translate.baidu import Baidu
from translate.bing import Bing
from translate.translator import Translator


translators = ['youdao', 'baidu', 'bing']


def get_translator(translator) -> Translator:
    if translator == 'youdao':
        return Youdao()
    elif translator == 'baidu':
        return Baidu()
    elif translator == 'bing':
        return Bing()
    else:
        raise InvalidTranslatorException("Invalid translator: '%s'." % translator)


class InvalidTranslatorException(Exception):
    pass
