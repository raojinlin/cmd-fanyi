from translate.youdaoRequest import YoudaoRequest
from translate.baiduRequest import BaiduRequest

def get_instance(request):
    if request == 'youdao':
        return YoudaoRequest()
    elif request == 'baidu':
        return BaiduRequest()
    else:
        raise UnknownRequestException("Illegal request type: '%s'." % request)

class UnknownRequestException(Exception): pass
