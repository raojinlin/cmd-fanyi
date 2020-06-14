import os
import json
import unittest

from translate.util import formatBuilder


class BaiduFormatBuilderTest(unittest.TestCase):
    def test_format_builder(self):
        builder = formatBuilder.BaiduFormatBuilder()
        with open(os.path.join(os.path.dirname(__file__), '../../../resources/baidu_response.json'), 'rt') as f:
            content = f.read()
        resp = json.loads(content)
        dict_result = resp.get('dict_result', {})
        oxford = dict_result.get('oxford', {})
        double_liju = resp.get('liju_result').get('double')

        builder \
            .of_simple_means(dict_result) \
            .of_oxford_entry(oxford) \
            .of_oxford_unbox(oxford) \
            .of_collins(dict_result.get('collins')) \
            .of_double(json.loads(double_liju))

        if 'dict_result' not in resp:
            builder.of_trans_result(resp.get('trans_result'))

        self.assertTrue('简明释义' in builder.get_result())
        self.assertTrue('有人邀请他们去参加一个印度教徒的婚礼，但他们不清楚这样的庆典会是怎样一种场面。' in builder.get_result())
        self.assertTrue('They had been invited to a Hindu wedding and were not sure '
                        'what happened on such occasions.' in builder.get_result())
        self.assertTrue('这种字体很优美，至今仍深受设计人员喜欢。' in builder.get_result())
        self.assertTrue('Such is the elegance of this typeface '
                        'that it is still a favourite of designers.' in builder.get_result())
        self.assertTrue('柯林斯词典:' in builder.get_result())
        self.assertTrue('DET 这样的;那样的;上述的;诸如此类的' in builder.get_result())
        self.assertTrue("You say you feel that you're being made to choose, and so you are. Such choices as this are "
                        "a by-product of freedom..." in builder.get_result())
        self.assertTrue('你说自己感觉是在被迫作选择，确实如此，而这样的选择是自由的附带品。' in builder.get_result())
        self.assertTrue('PHRASE 就是这样;就是如此;就是这么回事儿' in builder.get_result())
        self.assertTrue('双语例句:' in builder.get_result())
        self.assertTrue('There have been previous attempts at coups . We regard such methods as entirely unacceptable'
                        in builder.get_result())
        self.assertTrue('该 联盟 的 每 一 位 成员 国 都 同意 采取 其 认为 必要 的 行动 ， 包括 动用 武力 。' in builder.get_result())
        self.assertTrue('《柯林斯高阶英汉双解学习词典》' in builder.get_result())

