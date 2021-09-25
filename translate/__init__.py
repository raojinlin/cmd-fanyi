from functools import lru_cache
from .factory import get_translator
from .util import get_plain_text
from .translator import Translator

__all__ = ['Translator', 'get_plain_text', 'get_translator', 'console', '__version__']
__version__ = '0.0.4'


class ConsoleCommand(object):
    def __init__(self):
        self._commands = {}

    def add_command(self, command, help):
        self._commands[command] = help
        return self

    def print_help(self):
        print('available commands:')
        for command in self._commands:
            print('    ' + command + '%40s' % self._commands[command])


@lru_cache()
def translate(text, translator: Translator, verbose):
    return translator.query(text).format(verbose)


def console(translator: Translator, verbose=0):
    prompt = '[%s] >>> ' % translator.get_name()
    command = ConsoleCommand()
    command.\
        add_command('@quit', 'quit the console').\
        add_command('@cache:info', 'Show the lru cache info.').\
        add_command('@cache:clear', 'Clear the lru cache info')
    while True:
        text = input(prompt)
        if text == '@quit':
            break
        elif text == '@help':
            command.print_help()
        elif text == '@cache:info':
            print(translate.cache_info())
        elif text == '@cache:clear':
            translate.cache_clear()
            print('cache cleared.')
        elif not text:
            continue
        else:
            print(translate(text, translator, verbose))
