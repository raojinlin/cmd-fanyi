import requests
import json

from os import path


def lang_detect(text, cookie=''):
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36'
                             ' (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    if cookie:
        headers['Cookie'] = cookie
    try:
        resp = requests.post(
            'https://fanyi.baidu.com/langdetect',
            headers=headers,
            data={'query': text}
        )
        content = resp.content.decode('utf-8')
        result = json.loads(content)
        return result.get('lan', 'en')
    except Exception as _:
        return 'en'


def get_lang_obj():
    with open(path.join(path.dirname(__file__), '../../resources/countries.json'), 'rt') as json_file:
        return json.loads(json_file.read())


def exists_lang(lang):
    return lang in get_lang_obj()


def list_supported_lang():
    lang = get_lang_obj()

    for code in lang:
        print(code, lang[code])

