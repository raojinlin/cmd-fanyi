class AbstractRequest(object):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/73.0.3683.86 Safari/537.36 "

    def get_result(self, *args, **kwargs):
        """get translate result: dict"""
        raise MethodNotImplementedException("subclass of AbstractRequest method get_result not implemented.");

    def query(self, *args, **kwargs):
        """do the translate result
        
        @return self
        """
        raise MethodNotImplementedException("subclass of AbstractRequest method query not implemented.");

    def serialize(self, *args, **kwargs):
        """json.dumps()"""
        raise MethodNotImplementedException("subclass of AbstractRequest method serialize not implemented.");

    def format(self):
        """"""
        raise MethodNotImplementedException("subclass of AbstractRequest method view not implemented.")


class MethodNotImplementedException(Exception): pass
