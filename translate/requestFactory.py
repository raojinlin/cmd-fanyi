from translate.youdaoRequest import YoudaoRequest

def get_instance(request):
    if request == 'youdao':
        return YoudaoRequest()
    elif request == 'google':
        pass
    else:
        raise UnknownRequestException("Illegal request type: '%s'." % request)

class UnknownRequestException(Exception): pass
