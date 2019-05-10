import sys
import argparse
from youdao.translate import Translate

translate = Translate("")


def trans(args):
    if type(args) is list:
        translate.translate(" ".join(args))
    else:
        translate.translate(args)

    print(translate)


def query(args):
    if type(args) is list:
        translate.query(" ".join(args))
    else:
        translate.query(args)
    print(translate)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("an command line translate script")
    parser.add_argument("source", metavar="S", type=str, nargs="+", help="the source text")

    args = parser.parse_args()
    if len(args.source) >= 4:
        trans(args.source)
    else:
        query(args.source)



