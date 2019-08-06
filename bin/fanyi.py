import os
import sys
import argparse
import re


from youdao import Translate

translate = Translate()
CHINESE_REGEX = r'[\u4e00-\u9fa5]'

def trans(args):
    """句子翻译"""
    if type(args) is list:
        translate.translate(" ".join(args))
    else:
        translate.translate(args)


def query(args):
    """单词翻译"""
    if type(args) is list:
        translate.query(" ".join(args))
    else:
        translate.query(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("The command line translation script")
    parser.add_argument("source", metavar="S", type=str, nargs="+", help="the source text")
    parser.add_argument("--json", action="store_true", help="serialize the result(json)")
    parser.add_argument("-o", "--output", default="", type=str, help="output the result(json) to file")
    parser.add_argument("-v", "--version", action="store_true", help="show version")

    args = parser.parse_args()
    source_str = " ".join(args.source)
    words = re.findall(r'\w+', source_str)

    if args.version:
        sys.stdout.write("v0.1\n")
        sys.exit(0)

    if re.match(CHINESE_REGEX, source_str):
        words = re.findall(CHINESE_REGEX, source_str)

    if len(words) >= 4:
        trans(args.source)
    else:
        query(args.source)

    if args.json:
        if args.output:
            translate.save(args.output)
        else:
            sys.stdout.write(translate.serialize(2))
    else:
        print(translate)
