from translate.youdao import Youdao
from translate.baidu import Baidu
from translate.translator import Translator

translators = ['youdao', 'baidu']


def get_translator(translator) -> Translator:
    if translator == 'youdao':
        return Youdao()
    elif translator == 'baidu':
        return Baidu()
    else:
        raise InvalidTranslatorException("Invalid translator: '%s'." % translator)


class InvalidTranslatorException(Exception):
    pass
