# -*- coding: utf-8 -*-

import kunrei
import hepburn

def translate(table, s):
    roman = u'';
    l = len(s)
    n = 0
    while n < l:
        c1 = s[n]
        c2 = s[n:n+2]
        if c2 in table:
            roman += table[c2]
            n += 1
        elif c1 in table:
            roman += table[c1]
        else:
            roman += c1
        n += 1
    return roman

def to_kunrei(s):
    s = translate(kunrei.basic_table, s)
    s = kunrei.normalize(s)
    return s

def to_hepburn(s):
    s = translate(hepburn.basic_table, s)
    s = hepburn.normalize(s)
    return s
