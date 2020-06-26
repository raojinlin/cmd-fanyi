# encoding: utf-8


class Translator(object):
    """翻译器抽象类"""

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/73.0.3683.86 Safari/537.36 "

    def __init__(self):
        self.trans_from = 'zh'
        self.trans_to = 'en'

    def get_result(self, *args, **kwargs):
        """获取翻译后的结果，类型如'字典(dict)'"""
        raise MethodNotImplementedException("subclass of AbstractRequest method get_result not implemented.")

    def query(self, *args, **kwargs):
        """单词或文本翻译接口
        @return self
        """
        return self

    def serialize(self, *args, **kwargs):
        """序列化"""
        raise MethodNotImplementedException("subclass of AbstractRequest method serialize not implemented.")

    def format(self, verbose=0):
        """格式化, 返回格式化的文本"""
        raise MethodNotImplementedException("subclass of AbstractRequest method view not implemented.")

    def set_trans_from(self, trans_from):
        """待翻译文字语种"""
        self.trans_from = trans_from

    def set_trans_to(self, trans_to):
        """翻译到哪个语种"""
        self.trans_to = trans_to

    def get_name(self):
        return ""


class MethodNotImplementedException(Exception):
    pass
