from translate.youdaoRequest import YoudaoRequest
from translate.baiduRequest import BaiduRequest
from translate.abstratRequest import AbstractRequest


def get_instance(request) -> AbstractRequest:
    if request == 'youdao':
        return YoudaoRequest()
    elif request == 'baidu':
        return BaiduRequest()
    else:
        raise UnknownRequestException("Illegal request type: '%s'." % request)


class UnknownRequestException(Exception):
    pass
