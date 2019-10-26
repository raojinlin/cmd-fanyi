import os
import sys
import argparse
import re
import translate

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Command line translator")
    parser.add_argument("source", metavar="S", type=str, nargs="+", help="Text to be translated")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument('-l', '--list', action="store_true", help="List supported translation engines")
    parser.add_argument('--engine', metavar="E", type=str, nargs='?', const="youdao", help="Specify a translation engine, default: youdao")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")

    args = parser.parse_args()
    source_str = " ".join(args.source)
    words = re.findall(r'\w+', source_str)

    if args.version:
        sys.stdout.write("v0.1\n")
        sys.exit(0)

    translater = translate.requestFactory.get_instance(args.engine or 'youdao')
    translater.query(source_str)

    if args.json:
        sys.stdout.write(translater.serialize())
    else:
        print(translater.format())
