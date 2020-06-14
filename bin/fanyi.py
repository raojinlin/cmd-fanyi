#!/usr/bin/env python3

import sys
import argparse
import translate

from translate.baidu import Baidu
from translate.util.lang import lang_detect, list_supported_lang


if __name__ == '__main__':
    DEFAULT_TRANSLATE = 'baidu'
    DEFAULT_VERBOSE = 0

    parser = argparse.ArgumentParser("Command line translator")
    parser.add_argument("--text", "-t", metavar="text", type=str, nargs="+", help="Text to be translated", default="")
    parser.add_argument("--json", "-j", action="store_true", help="Output JSON, independent of verbose parameter")
    parser.add_argument('--engine', "-e", metavar="E", type=str, nargs='?', default=DEFAULT_TRANSLATE,
                        help="Specify a translation engine, default: %s" % DEFAULT_TRANSLATE)
    parser.add_argument('--engines', action='store_true', help='List supported engines')
    parser.add_argument('--detect', metavar='text', type=str, help='Language detection and exit')
    parser.add_argument('--trans-from', metavar='F', type=str, nargs='?', default='en',
                        help='Specify the language to be translated. baidu translator only')
    parser.add_argument('--trans-to', metavar='T', type=str, nargs='?', default='zh',
                        help='Specify which language to translate to. baidu translator only')
    parser.add_argument('--cookie', '-C', metavar='cookie', type=str, help='The cookie for http request, "baidu" '
                                                                           'required.')
    parser.add_argument('--list', '-L', action='store_true', help='List supported lang and exit')
    parser.add_argument('--console', '-c', action='store_true', help='open console')
    parser.add_argument('--verbose', '-v', action="count", help='Verbose')
    parser.add_argument('--version', '-V', action='version', version='%(prog)s ' + translate.__version__)

    args = parser.parse_args()
    text = " ".join(args.text)

    if args.engines:
        for engine in translate.factory.translators:
            print(engine)
        exit(0)

    if args.detect is True:
        print(lang_detect(text, args.cookie or ''))
        sys.exit(0)

    if args.list is True:
        list_supported_lang()
        sys.exit(0)

    translator = translate.get_translator(args.engine or DEFAULT_TRANSLATE)

    if isinstance(translator, Baidu) and args.cookie:
        translator.set_cookie(args.cookie)

    if args.trans_from:
        translator.set_trans_from(args.trans_from)

    if args.trans_to:
        translator.set_trans_to(args.trans_to)

    if args.console:
        translate.console(translator, verbose=(args.verbose or DEFAULT_VERBOSE))
        sys.exit(0)

    translator.query(text)
    if args.json:
        sys.stdout.write(translator.serialize())
    else:
        print(translator.format(verbose=(args.verbose or DEFAULT_VERBOSE)))
