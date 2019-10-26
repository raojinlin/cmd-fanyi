# encoding: utf-8 import re
import re
import requests
import json

from translate.abstratRequest import AbstractRequest
from translate.util.sign import PyJsHoisted_sign_ as text_sign

from translate.util.baidu_response_format import format_collins
from translate.util.baidu_response_format import format_simple_means
from translate.util.baidu_response_format import format_oxford_entry
from translate.util.baidu_response_format import format_oxford_unbox
from translate.util.baidu_response_format import format_trans_result
from translate.util.baidu_response_format import with_new_line
from translate.util.baidu_response_format import format_liju_double


class BaiduRequest(AbstractRequest):
    def __init__(self):
        super().__init__()

        self.gtk = ""
        self.token = ""
        self._last_query = ""

        self.api = "https://fanyi.baidu.com/v2transapi"
        self.api_home = "https://fanyi.baidu.com/"
        self.api_lan_detect = 'https://fanyi.baidu.com/langdetect'

        self.headers = {'User-Agent': self.user_agent, 'x-requested-with': 'XMLHttpRequest'}
        self._result = None

    def get_param(self, query):
        param = {
            "from": self.trans_from,
            "to": self.trans_to,
            "query": query,
            "transtype": "translang",
            "simple_means_flag": 3,
            "sign": self.sign(query),
            "token": self.token
        }

        return param

    def get_token_and_gtk(self):
        resp = requests.get(self.api_home, headers=self.headers)
        content = resp.content.decode('utf-8')
        token = re.findall(r'token: (.*)', content)[0]
        gtk = re.findall(r'gtk = (.\d+\.\d+.)', content)[0]

        gtk = gtk.replace("'", "")
        token = token.replace("'", "").replace(',', '')

        return gtk, token

    def sign(self, text):
        if not self.token or not self.gtk:
            self.gtk, self.token = self.get_token_and_gtk()

        return text_sign(text, self.gtk)

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

    def format(self, verbose=0):
        result = self.get_result()
        if result is None:
            return ""

        text = ''
        dict_result = result.get('dict_result', {})
        oxford = dict_result.get('oxford')
        collins = dict_result.get('collins')
        liju_result = result.get('liju_result', {})
        double_str = liju_result.get('double')

        text += with_new_line(format_simple_means(dict_result))

        if verbose >= 1:
            text += with_new_line(format_oxford_entry(oxford))

        if verbose >= 2:
            text += with_new_line(format_oxford_unbox(oxford))

        if verbose >= 3:
            text += with_new_line(format_collins(collins))

        if verbose >= 4 and double_str:
            double_text = format_liju_double(json.loads(double_str))
            text += double_text

        if 'dict_result' not in result:
            text += format_trans_result(result.get('trans_result'))

        return text
