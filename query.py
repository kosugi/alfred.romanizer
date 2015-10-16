# -*- coding: utf-8 -*-
#
# romanize Hiragana/Katakana sentence.
#
# query MUST be escaped double quotation marks and backslashes.
#

import re
import sys
import codecs
import unicodedata
from xml.sax.saxutils import escape
from romanizer import to_hepburn, to_kunrei

alt_escape_rule = {u'"': u'&quot;', u"'": u'&#39;'}
def h(value):
    return escape(value, alt_escape_rule)

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
    q = sys.argv[1].decode('UTF-8') if 1 < len(sys.argv) else u"""{query}"""
    q = unicodedata.normalize('NFKC', q)
    h_text = to_hepburn(q)
    k_text = to_kunrei(q)
    print u'''<?xml version="1.0"?>
<items>
  <item uid="h_result" arg="{h_text}" valid="yes">
    <title>{h_text}</title>
    <subtitle>Hepburn system</subtitle>
  </item>
  <item uid="k_result" arg="{k_text}" valid="yes">
    <title>{k_text}</title>
    <subtitle>Kunrei system</subtitle>
  </item>
</items>'''.format(h_text=h(h_text), k_text=h(k_text))
