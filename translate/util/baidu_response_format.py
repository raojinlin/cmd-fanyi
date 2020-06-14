# encoding: utf-8

__all__ = ['format_simple_means', 'format_oxford_entry', 'format_oxford_unbox',
           'format_collins', 'with_new_line', 'format_trans_result', 'format_liju_double']


def indent(level=4):
    return " " * level


def format_examples(examples):
    text = ''
    for example in examples:
        ex = replace_html_blod(example.get('ex', ''))
        tran = example.get('tran')
        # tts_mp3 = example.get('tts_mp3', '')
        # tts_size = example.get('tts_size', '')

        text += "%s\n" % ex
        text += '\033[04m%s\033[0m\n\n' % tran
        # text += 'mp3 url: \033[04m%s\033[0m, mp3 size: %s\n\n' % ("https://fanyi.baidu.com/" + tts_mp3, tts_size)

    return text


def replace_html_blod(text):
    replace_prefix = text.replace('<b>', '\033[1m')
    replace_suffix = replace_prefix.replace('</b>', '\033[0m')

    return replace_suffix


def with_new_line(text):
    if text is None or text == '':
        return text
    return text + '\n'


def with_italic(text):
    return "\033[2m%s\033[0m" % text


def bold_title(title):
    return "\033[1m%s\033[0m" % title


def format_simple_means(result):
    simple_means = result.get('simple_means')

    if simple_means is None:
        return ''

    symbols = simple_means.get('symbols')
    text = bold_title('简明释义') + "\n"

    def format_means(means):
        s = ''
        for mean in means:
            if type(mean) is dict:
                word_mean = mean.get('word_mean', '')
                inner_means = mean.get('means', [])

                s += word_mean + ' ' + "; ".join(inner_means) + '\n'
            elif type(mean) is str:
                s += mean + ';'
        return s

    for symbol in symbols:
        parts = symbol.get('parts', '')
        ph_am = symbol.get('ph_am', '')
        ph_en = symbol.get('ph_en')
        
        text += "%s %s\n" % (ph_am, ph_en)
        for part in parts:
            line = part.get('part', '') + format_means(part.get('means'))
            text += line + "\n"

    return text


def format_oxford_entry(oxford):
    if type(oxford) is not dict or 'entry' not in oxford:
        return ""

    entrys = oxford.get('entry')
    text = bold_title('牛津词典:') + "\n"

    for entry in entrys:
        entry_name = entry.get('name')
        text += entry_name + "\n"

        entry_data_list = entry.get('data')
        for entry_data in entry_data_list:
            data = entry_data.get('data', []) 
            ng_data = filter(lambda item: item.get('tag') == 'n-g', data)

            for i, ng in enumerate(ng_data):
                ng_details = ng.get('data', [])

                for j, ng_detail in enumerate(ng_details):
                    if 'chText' not in ng_detail:
                        continue
                    ch_text = ng_detail.get('chText', '')
                    en_text = ng_detail.get('enText', '')

                    if j == 0:
                        ch_text = "%d.%s" % (i + 1, ch_text)
                        en_text = "%s" % en_text

                    else:
                        ch_text = "\033[2m%s\033[0m" % ch_text
                        en_text = "\033[2m%s\033[0m\n" % en_text

                    text += ch_text + "\n"
                    text += en_text + "\n"
    return text


def format_oxford_unbox(oxford):
    if type(oxford) is not dict or 'unbox' not in oxford:
        return ""

    text = ""
    unbox = oxford.get('unbox')

    for box in unbox:
        box_type = box.get('type')
        box_data = box.get('data', [])

        if box_type == 'more_about':
            text += bold_title('补充说明') + "\n"

        for datum in box_data:
            if datum.get('tag') == 'title':
                text += datum.get('text', '') + '\n'
            else:
                text_data = datum.get('data', [])
                for i, text_datum in enumerate(text_data):
                    if type(text_datum) is str:
                        text += text_datum
                    elif 'data' in text_datum:
                        for j, datum in enumerate(text_datum.get('data', [])):
                            text += format_oxford_tag(datum, j)
                    else:
                        text += format_oxford_tag(text_datum, i)
    return text


def format_oxford_tag(datum, i):
    text = ''
    ch_text = datum.get('chText', '')
    en_text = "* " + datum.get('enText', '')

    if i > 0:
        ch_text = "\033[02m%s\033[0m" % ch_text
        en_text = "\033[02m%s\033[0m" % en_text

    text += en_text + '\n'
    text += ch_text + '\n\n'

    return text


def format_collins(collins):
    text = bold_title('柯林斯词典:') + '\n'

    if collins is None:
        return ""

    if 'menus' in collins:
        menus = collins.get('menus', [])

        for menu in menus:
            text += format_entrys(menu.get('entry', []))
    if 'entry' in collins:
        text += format_entrys(collins.get('entry', []))

    return text

                        
def format_entrys(entry):
    if not entry:
        return ""
    text = ''

    for n, item in enumerate(entry):
        if item.get('type') != 'mean':
            continue

        values = item.get('value', [])
        for value in values:
            define = value.get('def')
            trans = value.get('tran')
            means = value.get('mean_type')

            posp = " ".join(map(lambda item: item.get('label'), value.get('posp', [])))

            text += with_new_line("%s. %s %s" % (with_italic(str(n + 1)), posp, trans))
            text += with_new_line(replace_html_blod(define))

            for mean in means:
                info_type = mean.get('info_type')
                
                if info_type == 'example':
                    examples = mean.get(info_type, [])
                    text += format_examples(examples)

                if info_type == 'posc':
                    posc = mean.get(info_type)
                    for pos in posc:
                        examples = pos.get('example')
                        define = pos.get('def', '')
                        text += with_new_line(replace_html_blod(define))

                        text += format_examples(examples)
    return text


def format_trans_result(result):
    if not result:
        return ''

    text = ''
    data = result.get('data', [])
    keywords = result.get('keywords', [])

    for datum in data:
        text += datum.get('dst') + '\n'

    if len(keywords) > 0:
        text += bold_title('重点词汇:') + '\n'

    for keyword in keywords:
        text += keyword.get('word', '') + ': ' + "; ". join(keyword.get('means', [])) + '\n' 

    return text


def format_liju_double(double_data):
    text = ""

    for data in double_data:
        ch_text_list, en_text_list, provider = data[0:3]
        ch_text = " ".join(map(lambda item: item[0], ch_text_list))
        en_text = " ".join(map(lambda item: item[0], en_text_list))

        text += with_new_line(ch_text)
        text += with_new_line(en_text)

        if provider:
            text += '\033[2m' + provider + '\033[0m\n\n'

    if text != "":
        text = bold_title("双语例句:\n\n") + text

    return text


