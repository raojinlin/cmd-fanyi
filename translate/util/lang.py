import requests
import json


def lang_detect(text):
    try:
        resp = requests.post(
            'https://fanyi.baidu.com/langdetect',
            headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36'
                                   ' (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'},
            data={'query': text}
        )
        content = resp.content.decode('utf-8')
        result = json.loads(content)
        return result.get('lan', 'en')
    except Exception as _:
        return 'en'
