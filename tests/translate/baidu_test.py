import unittest

from translate.baidu import Baidu

baidu = Baidu()
baidu.set_trans_from('en')
baidu.set_trans_to('zh')


class BaiduTest(unittest.TestCase):
    def test_query(self):
        baidu.query("hello")
        self.assertTrue('dict_result', baidu.get_result())
        self.assertTrue('oxford', baidu.get_result().get('dict_result'))
        self.assertTrue('collins', baidu.get_result().get('dict_result'))

    def test_verbose(self):
        baidu.query('hello')
        self.assertTrue(baidu.format(0) != '')
        self.assertTrue('简明释义' in baidu.format(0))
        self.assertTrue('柯林斯词典' in baidu.format(3))
        self.assertTrue('双语例句' in baidu.format(4))

    def test_translate(self):
        baidu.query('be conservative in what you do, be liberal in what you accept from others.')
        self.assertNotIn('errmsg', baidu.get_result())
