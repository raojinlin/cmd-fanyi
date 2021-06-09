# encoding: utf-8
import re
import requests
import json

from translate.translator import Translator
from translate.util.baidu_sign import generate_token

from translate.util.formatBuilder import BaiduFormatBuilder


class Baidu(Translator):
    def __init__(self):
        super().__init__()

        self.gtk = ""
        self.token = ""
        self._last_query = ""

        self.api = "https://fanyi.baidu.com/v2transapi"
        self.api_home = "https://fanyi.baidu.com/"
        self.api_lan_detect = 'https://fanyi.baidu.com/langdetect'

        self._result = None
        self._response = None

        self.session = requests.session()
        self.session.headers = {'User-Agent': self.user_agent, 'x-requested-with': 'XMLHttpRequest'}

    def set_cookie(self, cookie):
        self.session.headers['Cookie'] = cookie

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
        resp = self.session.get(self.api_home)
        baidu_uid = resp.cookies.get('BAIDUID')
        if baidu_uid:
            self.set_cookie('BAIDUID=%s' % baidu_uid)
        resp = self.session.get(self.api_home)
        content = resp.content.decode('utf-8')
        token = re.findall(r'token: (.*)', content)[0]
        gtk = re.findall(r'gtk = (.\d+\.\d+.)', content)[0]

        gtk = gtk.replace("'", "")
        token = token.replace("'", "").replace(',', '')

        return gtk, token

    def sign(self, text):
        if not self.token or not self.gtk:
            self.gtk, self.token = self.get_token_and_gtk()

        return generate_token(text, self.gtk)

    def query(self, text):
        if self._last_query == text:
            return self

        self._last_query = text
        param = self.get_param(text)
        resp = self.session.post(self.api, data=param)

        content = resp.content.decode('utf-8')
        self._result = json.loads(content)
        self._response = resp

        return self

    def get_result(self):
        return self._result

    def serialize(self):
        return json.dumps(self.get_result())

    def __str__(self):
        return self.format(6)

    def format(self, verbose=0):
        result = self.get_result()
        if result is None:
            return ""

        dict_result = result.get('dict_result', {})
        oxford = dict_result.get('oxford')
        collins = dict_result.get('collins')
        liju_result = result.get('liju_result', {})
        double_str = liju_result.get('double')

        builder = BaiduFormatBuilder()

        builder.of_simple_means(dict_result)

        if verbose >= 1:
            builder.of_oxford_entry(oxford)

        if verbose >= 2:
            builder.of_oxford_unbox(oxford)

        if verbose >= 3:
            builder.of_collins(collins)

        if verbose >= 4 and double_str:
            builder.of_double(json.loads(double_str))

        if 'dict_result' not in result:
            builder.of_trans_result(result.get('trans_result'))

        return builder.get_result()

    def get_name(self):
        return "Baidu"
