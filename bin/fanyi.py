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

    print(translate)


def query(args):
    """单词翻译"""
    if type(args) is list:
        translate.query(" ".join(args))
    else:
        translate.query(args)
    print(translate)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("an command line translate script")
    parser.add_argument("source", metavar="S", type=str, nargs="+", help="the source text")

    args = parser.parse_args()
    source_str = " ".join(args.source)
    words = re.findall(r'\w+', source_str)

    if re.match(CHINESE_REGEX, source_str):
        words = re.findall(CHINESE_REGEX, source_str)

    if len(words) >= 4:
        trans(args.source)
    else:
        query(args.source)
