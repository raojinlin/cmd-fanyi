import unittest


from translate.bing import BingTransResult


class BingTransTest(unittest.TestCase):
    def test_result(self):
        html = '''<div><span id="ht_logo"></span><h4>capsule</h4><span class="ht_attr" lang="en">['k&#230;p.sjul]
        </span><ul><li><span class="ht_pos">n.</span><span
        class="ht_trs">太空舱；荚；航天舱；（装药物的）胶囊</span></li></ul><ul><li><span class="ht_pos">adj.</span><span
        class="ht_trs">简略的；小而结实的</span></li></ul><ul><li><span class="ht_pos">v.</span><span
        class="ht_trs">节略；以瓶帽密封</span></li></ul></div> '''
        res = BingTransResult.from_html(html)
        self.assertEqual('capsule', res.get_original())
        self.assertEqual("['k&#230;p.sjul]", res.get_pronunciation())
        self.assertEqual(3, len(res.get_translation()))
        self.assertEqual('n.', res.get_translation()[0].get('pos'))
        self.assertEqual('太空舱；荚；航天舱；（装药物的）胶囊', res.get_translation()[0].get('trans'))
        self.assertEqual('adj.', res.get_translation()[1].get('pos'))
        self.assertEqual('简略的；小而结实的', res.get_translation()[1].get('trans'))
        self.assertEqual('v.', res.get_translation()[2].get('pos'))
        self.assertEqual('节略；以瓶帽密封', res.get_translation()[2].get('trans'))
