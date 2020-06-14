from .factory import get_translator
from .util import get_plain_text
from .translator import Translator

__all__ = ['Translator', 'get_plain_text', 'get_translator', 'console']
__version__ = '0.01'


def console(translator: Translator, verbose=0):
    prompt = '[%s] >>> ' % translator.get_name()
    while True:
        text = input(prompt)
        if text == 'quit':
            break
        elif not text:
            continue
        else:
            translator.query(text)
            print(translator.format(verbose))
