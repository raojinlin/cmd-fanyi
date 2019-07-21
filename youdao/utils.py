class QueryString:
    @staticmethod
    def parse(query_string):
        result = {}
        for query in query_string.split("&"):
            key_value = query.split("=")
            if len(key_value) == 2:
                key, value = key_value
                result[key] = value
        return result

    @staticmethod
    def stringify(query_dict: dict) -> str:
        result_list = []
        for key in query_dict:
            result_list.append("%s=%s" % (key, query_dict[key]))
        return "&".join(result_list)


def get_plain_text(text):
    """
    clear \n and left space
    :param text: input text
    :type text str
    :return: str
    """
    if not text or not isinstance(text, str):
        return ""

    return text.lstrip().replace("\n", "").replace("\r", "")
