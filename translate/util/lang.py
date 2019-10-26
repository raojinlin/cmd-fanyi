import requests
import json

API_LAN_DETECT = 'https://fanyi.baidu.com/langdetect'


def lang_detect(text, headers):
    try:
        resp = requests.post(API_LAN_DETECT, headers=headers, data={'query': text})
        content = resp.content.decode('utf-8')
        result = json.loads(content)
        return result.get('lan', 'en')
    except:
        return 'en'
