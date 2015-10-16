# -*- coding: utf-8 -*-

import unittest
from romanizer import to_hepburn, to_kunrei

class HepbernTestCase(unittest.TestCase):

    def test_hepburn(self):
        self.assertEqual(u'', to_hepburn(u''))
        self.assertEqual(u'aiueo', to_hepburn(u'あいうえお'))
        self.assertEqual(u'gumma', to_hepburn(u'ぐんま'))
        self.assertEqual(u'chimpui', to_hepburn(u'チンプイ'))
        self.assertEqual(u'bampuobuchikin', to_hepburn(u'バンプオブチキン'))
        self.assertEqual(u'kanda', to_hepburn(u'かんだ'))
        self.assertEqual(u'bozuga jozuni byobuni bozuno eokaita', to_hepburn(u'ボウズガ ジョウズニ ビョウブニ ボウズノ エヲカイタ'))
        self.assertEqual(u'beppu', to_hepburn(u'べっぷ'))
        self.assertEqual(u'kotchi', to_hepburn(u'コッチ'))
        self.assertEqual(u'nnnnnn', to_hepburn(u'んんんンンン'))
        self.assertEqual(u'oi toru onishi', to_hepburn(u'おーい とおる おおにし'))
        self.assertEqual(u"shinichi", to_hepburn(u'シンイチ'))

    def test_kunrei(self):
        self.assertEqual(u'', to_kunrei(u''))
        self.assertEqual(u'aiueo', to_kunrei(u'あいうえお'))
        self.assertEqual(u'gunma', to_kunrei(u'ぐんま'))
        self.assertEqual(u'tinpui', to_kunrei(u'チンプイ'))
        self.assertEqual(u'banpuobutikin', to_kunrei(u'バンプオブチキン'))
        self.assertEqual(u'kanda', to_kunrei(u'かんだ'))
        self.assertEqual(u'bouzuga zyouzuni byoubuni bouzuno ewokaita', to_kunrei(u'ボウズガ ジョウズニ ビョウブニ ボウズノ エヲカイタ'))
        self.assertEqual(u'beppu', to_kunrei(u'べっぷ'))
        self.assertEqual(u'kotti', to_kunrei(u'コッチ'))
        self.assertEqual(u'nnnnnn', to_kunrei(u'んんんンンン'))
        self.assertEqual(u'ôi tooru oonisi', to_kunrei(u'おーい とおる おおにし'))
        self.assertEqual(u"sin'iti", to_kunrei(u'シンイチ'))

if __name__ == '__main__':
    unittest.main()
