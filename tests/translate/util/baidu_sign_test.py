import unittest

from translate.util.baidu_sign import generate_token


class BaiduSignTest(unittest.TestCase):
    def test_token(self):
        gtk = '320305.131321201'
        self.assertEqual(generate_token('hello', gtk), '54706.276099')
        self.assertEqual(generate_token('hello world are you ok ? this is funny.', gtk), '865383.644950')
        self.assertEqual(generate_token('你好', gtk), '232427.485594')
        self.assertEqual(generate_token('抽刀断水水更流，举杯消愁愁更愁。', gtk), '641727.862606')
