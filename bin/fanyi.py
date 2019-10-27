#!/usr/bin/env python3

import sys
import argparse
import translate

from translate.util.lang import lang_detect, list_supported_lang

__version__ = '0.0.1'

if __name__ == '__main__':
    DEFAULT_TRANSLATE = 'baidu'
    DEFAULT_VERBOSE = 0

    parser = argparse.ArgumentParser("Command line translator")
    parser.add_argument("text", metavar="text", type=str, nargs="+", help="Text to be translated", default="")
    parser.add_argument("--json", action="store_true", help="Output JSON, independent of verbose parameter")
    parser.add_argument('--engine', metavar="E", type=str, nargs='?', default=DEFAULT_TRANSLATE,
                        help="Specify a translation engine, default: %s" % DEFAULT_TRANSLATE)
    parser.add_argument('--detect', action="store_true", help='Language detection and exit')
    parser.add_argument('--trans-from', metavar='F', type=str, nargs='?', default='en',
                        help='Specify the language to be translated. baidu translate only')
    parser.add_argument('--trans-to', metavar='T', type=str, nargs='?', default='zh',
                        help='Specify which language to translate to. baidu translate only')
    parser.add_argument('--list', '-L', action='store_true', help='List supported lang and exit')
    parser.add_argument('--verbose', '-v', action="count", help='Show details')
    parser.add_argument('--version', '-V', action='version', version='%(prog)s ' + __version__)

    args = parser.parse_args()
    text = " ".join(args.text)

    if args.detect is True:
        print(lang_detect(text))
        sys.exit(0)

    if args.list is True:
        list_supported_lang()
        sys.exit(0)

    translater = translate.requestFactory.get_instance(args.engine or DEFAULT_TRANSLATE)

    if args.trans_from:
        translater.set_trans_from(args.trans_from)

    if args.trans_to:
        translater.set_trans_to(args.trans_to)

    translater.query(text)
    if args.json:
        sys.stdout.write(translater.serialize())
    else:
        print(translater.format(verbose=args.verbose or DEFAULT_VERBOSE))
