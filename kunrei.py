# -*- coding: utf-8 -*-

basic_table = dict(map(lambda s: s.split(u'\t'), u'''
あ	a
い	i
う	u
え	e
お	o
か	ka
き	ki
く	ku
け	ke
こ	ko
さ	sa
し	si
す	su
せ	se
そ	so
た	ta
ち	ti
つ	tu
て	te
と	to
な	na
に	ni
ぬ	nu
ね	ne
の	no
は	ha
ひ	hi
ふ	hu
へ	he
ほ	ho
ま	ma
み	mi
む	mu
め	me
も	mo
や	ya
ゆ	yu
よ	yo
ら	ra
り	ri
る	ru
れ	re
ろ	ro
わ	wa
を	wo
ぁ	a
ぃ	i
ぅ	u
ぇ	e
ぉ	o
が	ga
ぎ	gi
ぐ	gu
げ	ge
ご	go
ざ	za
じ	zi
ず	zu
ぜ	ze
ぞ	zo
だ	da
ぢ	di
づ	du
で	de
ど	do
ば	ba
び	bi
ぶ	bu
べ	be
ぼ	bo
ぱ	pa
ぴ	pi
ぷ	pu
ぺ	pe
ぽ	po
きゃ	kya
きゅ	kyu
きょ	kyo
しゃ	sya
しゅ	syu
しょ	syo
ちゃ	tya
ちゅ	tyu
ちょ	tyo
にゃ	nya
にゅ	nyu
にょ	nyo
ひゃ	hya
ひゅ	hyu
ひょ	hyo
みゃ	mya
みゅ	myu
みょ	myo
りゃ	rya
りゅ	ryu
りょ	ryo
ぎゃ	gya
ぎゅ	gyu
ぎょ	gyo
じゃ	zya
じゅ	zyu
じょ	zyo
でゃ	dya
でゅ	dyu
でょ	dyo
びゃ	bya
びゅ	byu
びょ	byo
ぴゃ	pya
ぴゅ	pyu
ぴょ	pyo
クヮ	kwa
グヮ	gwa
ア	a
イ	i
ウ	u
エ	e
オ	o
カ	ka
キ	ki
ク	ku
ケ	ke
コ	ko
サ	sa
シ	si
ス	su
セ	se
ソ	so
タ	ta
チ	ti
ツ	tu
テ	te
ト	to
ナ	na
ニ	ni
ヌ	nu
ネ	ne
ノ	no
ハ	ha
ヒ	hi
フ	hu
ヘ	he
ホ	ho
マ	ma
ミ	mi
ム	mu
メ	me
モ	mo
ヤ	ya
ユ	yu
ヨ	yo
ラ	ra
リ	ri
ル	ru
レ	re
ロ	ro
ワ	wa
ヲ	wo
ァ	a
ィ	i
ゥ	u
ェ	e
ォ	o
ガ	ga
ギ	gi
グ	gu
ゲ	ge
ゴ	go
ザ	za
ジ	zi
ズ	zu
ゼ	ze
ゾ	zo
ダ	da
ヂ	di
ヅ	du
デ	de
ド	do
バ	ba
ビ	bi
ブ	bu
ベ	be
ボ	bo
パ	pa
ピ	pi
プ	pu
ペ	pe
ポ	po
キャ	kya
キュ	kyu
キョ	kyo
シャ	sya
シュ	syu
ショ	syo
チャ	tya
チュ	tyu
チョ	tyo
ニャ	nya
ニュ	nyu
ニョ	nyo
ヒャ	hya
ヒュ	hyu
ヒョ	hyo
ミャ	mya
ミュ	myu
ミョ	myo
リャ	rya
リュ	ryu
リョ	ryo
ギャ	gya
ギュ	gyu
ギョ	gyo
ジャ	zya
ジュ	zyu
ジョ	zyo
デャ	dya
デュ	dyu
デョ	dyo
ビャ	bya
ビュ	byu
ビョ	byo
ピャ	pya
ピュ	pyu
ピョ	pyo
くゎ	kwa
ぐゎ	gwa
'''.strip(u'\n').split(u'\n')))

long_sound_table = dict(u'aâ iî uû eê oô'.split())
long_sounds = u'aa ii uu ee oo ou'.split()

def normalize(s):
    roman = u''
    l = len(s)
    n = 0
    while n < l:
        c1 = s[n]
        c2 = s[n:n+2]
        c3 = s[n+1:n+2]
        if roman and c1 == u'ー':
            c1 = u''
            if roman[-1] in u'aiueo':
                roman = roman[:-1] + long_sound_table[roman[-1]]
        elif c2 in long_sounds:
            c1 = long_sound_table[c1]
            n += 1
        elif c1 in u'んン':
            c1 = u'n'
            if c3 and c3 in u'aiueoy':
                c1 += u"'"
        elif c1 in u'っッ':
            if c3 in u'bcdfghjklmnpqrstvwxyz':
                c1 = c3
            else:
                c1 = u''
        roman += c1
        n += 1
    return roman
