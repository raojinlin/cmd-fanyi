# encoding: utf-8

import re
import requests
import json

from translate.abstratRequest import AbstractRequest
from translate.util.sign import PyJsHoisted_sign_ as text_sign

from translate.util.baidu_response_format import format_collins
from translate.util.baidu_response_format import format_simple_means
from translate.util.baidu_response_format import format_oxford_entry
from translate.util.baidu_response_format import format_oxford_unbox
from translate.util.baidu_response_format import with_new_line

class BaiduRequest(AbstractRequest):
    def __init__(self):
        super(AbstractRequest, self).__init__()

        self.gtk = ""
        self.token = ""
        self._last_query = ""

        self.api = "https://fanyi.baidu.com/v2transapi"
        self.api_home = "https://fanyi.baidu.com/"
        self.api_lan_detect = 'https://fanyi.baidu.com/langdetect'

        self.headers = {'User-Agent': self.user_agent, 'x-requested-with': 'XMLHttpRequest'}
        self._result = None

    def get_param(self, query, fm="en", to="zh"):
        param =  {
            "from": fm,
            "to": to,
            "query": query,
            "transtype": "translang",
            "simple_means_flag": 3,
            "sign": self.sign(query),
            "token": self.token
        }

        # param.update(self.query_param)

        return param

    def get_token_and_gtk(self):
        if self.token != "" and self.gtk != "":
            return self.token, self.gtk

        resp = requests.get(self.api_home, headers=self.headers)
        content = resp.content.decode('utf-8')
        token = re.findall(r'token: (.*)', content)[0]
        gtk = re.findall(r'gtk = (.\d+\.\d+.)', content)[0]


        self.gtk = gtk.replace("'", "")
        self.token = token.replace("'", "").replace(',', '')

        return self.token, self.gtk

    def sign(self, text):
        _, gtk = self.get_token_and_gtk()
        return text_sign(text, gtk)

    def query(self, text):
        if self._last_query == text:
            return self

        self._last_query = text
        param = self.get_param(text)
        resp = requests.post(self.api, headers=self.headers, data=param)

        content = resp.content.decode('utf-8')
        self._result = json.loads(content)

        return self

    def get_result(self):
        return self._result

    def serialize(self):
        return json.dumps(self.get_result())

    def format(self):
        result = self.get_result()
        if result is None:
            return ""

        text = ''
        dict_result = result.get('dict_result')
        oxford = dict_result.get('oxford')
        collins = dict_result.get('collins')

        simple_means = format_simple_means(dict_result)
        oxford_entry = format_oxford_entry(oxford)
        oxford_unbox = format_oxford_unbox(oxford)
        collins_text = format_collins(collins)

        text += with_new_line(simple_means)
        text += with_new_line(oxford_entry)
        text += with_new_line(oxford_unbox)
        text += with_new_line(collins_text)

        return text
