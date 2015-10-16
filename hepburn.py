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
し	shi
す	su
せ	se
そ	so
た	ta
ち	chi
つ	tsu
て	te
と	to
な	na
に	ni
ぬ	nu
ね	ne
の	no
は	ha
ひ	hi
ふ	fu
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
を	o
ん	n
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
じ	ji
ず	zu
ぜ	ze
ぞ	zo
だ	da
ぢ	ji
づ	zu
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
しゃ	sha
しゅ	shu
しょ	sho
ちゃ	cha
ちゅ	chu
ちょ	cho
ちぇ	che
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
じゃ	ja
じゅ	ju
じょ	jo
びゃ	bya
びゅ	byu
びょ	byo
ぴゃ	pya
ぴゅ	pyu
ぴょ	pyo
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
シ	shi
ス	su
セ	se
ソ	so
タ	ta
チ	chi
ツ	tsu
テ	te
ト	to
ナ	na
ニ	ni
ヌ	nu
ネ	ne
ノ	no
ハ	ha
ヒ	hi
フ	fu
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
ヲ	o
ン	n
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
ジ	ji
ズ	zu
ゼ	ze
ゾ	zo
ダ	da
ヂ	ji
ヅ	zu
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
シャ	sha
シュ	shu
ショ	sho
チャ	cha
チュ	chu
チョ	cho
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
ジャ	ja
ジュ	ju
ジョ	jo
ビャ	bya
ビュ	byu
ビョ	byo
ピャ	pya
ピュ	pyu
ピョ	pyo
ジェ	jie
チェ	chie
ティ	tei
ディ	dei
デュ	deyu
ファ	fua
フィ	fui
フェ	fue
フォ	fuo
ヴァ	bua
ヴィ	bui
ヴ	bu
ヴェ	bue
ヴォ	buo
ー	
'''.strip(u'\n').split(u'\n')))

def normalize(s):
    roman = u''
    l = len(s)
    n = 0
    while n < l:
        c1 = s[n]
        c2 = s[n:n+2]
        if c2 in (u'aa', u'ii', u'uu', u'ee', u'ou', u'oo'):
            n += 1
        elif c2 in (u'nb', u'nm', u'np'):
            c1 = u'm'
        elif c1 in (u'っ', u'ッ'):
            c3 = s[n+1:n+2]
            if s[n:n+3] in (u'っch', u'ッch'):
                c1 = u't'
            elif c3 in u'bcdfghjklmnpqrstvwxyz':
                c1 = c3
            else:
                c1 = ''
        roman += c1
        n += 1
    return roman
