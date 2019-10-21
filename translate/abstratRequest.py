# encoding: utf-8


class AbstractRequest(object):
    """抽象翻译请求"""
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/73.0.3683.86 Safari/537.36 "

    def get_result(self, *args, **kwargs):
        """获取翻译后的结果，类型如'字典(dict)'"""
        raise MethodNotImplementedException("subclass of AbstractRequest method get_result not implemented.");

    def query(self, *args, **kwargs):
        """单词或文本翻译接口
        @return self
        """
        raise MethodNotImplementedException("subclass of AbstractRequest method query not implemented.");

    def serialize(self, *args, **kwargs):
        """序列化"""
        raise MethodNotImplementedException("subclass of AbstractRequest method serialize not implemented.");

    def format(self):
        """格式化, 返回格式化的文本
        @return str
        """
        raise MethodNotImplementedException("subclass of AbstractRequest method view not implemented.")


class MethodNotImplementedException(Exception): pass
