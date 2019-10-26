import sys
import argparse
import translate

__version__ = '0.0.1'

if __name__ == '__main__':
    DEFAULT_TRANSLATE = 'baidu'
    DEFAULT_VERBOSE = 0

    parser = argparse.ArgumentParser("Command line translator")
    parser.add_argument("source", metavar="S", type=str, nargs="+", help="Text to be translated")
    parser.add_argument("--json", action="store_true", help="Output JSON, independent of verbose parameter")
    parser.add_argument('--engine', metavar="E", type=str, nargs='?', const=DEFAULT_TRANSLATE,
                        help="Specify a translation engine, default: %s" % DEFAULT_TRANSLATE)
    parser.add_argument('--trans-from', metavar='F', type=str, nargs='?', const='en', help='Specify the language to be '
                                                                                           'translated')
    parser.add_argument('--trans-to', metavar='T', type=str, nargs='?', const='zh', help='Specify which language to '
                                                                                         'translate to')
    parser.add_argument('--verbose', '-v', action="count", help='Show details')
    parser.add_argument('--version', '-V', action='version', version='%(prog)s ' + __version__)

    args = parser.parse_args()
    source_str = " ".join(args.source)

    translater = translate.requestFactory.get_instance(args.engine or DEFAULT_TRANSLATE)

    if args.trans_from:
        translater.set_trans_from(args.trans_from)

    if args.trans_to:
        translater.set_trans_to(args.trans_to)

    translater.query(source_str)
    if args.json:
        sys.stdout.write(translater.serialize())
    else:
        print(translater.format(verbose=args.verbose or DEFAULT_VERBOSE))
