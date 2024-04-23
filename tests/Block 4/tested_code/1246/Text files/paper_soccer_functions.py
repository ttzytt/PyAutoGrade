



import time






def create_board(num_rows, num_columns, board):
    i_r = 0

    while i_r < num_rows:
        board.append([])
        for i in range(num_columns):
            board[i_r].append([])
        i_r += 1

        
(◕‿◕) 
SYMBL

Homepage
›  
Unicode
›  
Character Table
List of Unicode Symbols
Version: 15.1.0
Release date: September 12, 2023
Total number of characters: 149 813
Almost half a million symbols of all kinds, including arrows, mathematical signs, emojis, hieroglyphics, and ancient scripts, are available. Each symbol lies in its assigned cell in the table. Just scroll down to explore the whole variety of Unicode characters. Or use the block navigation on the right — each character block occupies its range in the table divided into 17 planes. Try 
△
Geometric Shapes
 for example. Hover over a character you like to see its name or copy it. Click on the symbol name and go to a separate page to study it.
Complete Unicode Character Table on One Page
F8E0
F8E1
F8E2
F8E3
F8E4
F8E5
F8E6
F8E7
F8E8
F8E9
F8EA
F8EB
F8EC
F8ED
F8EE
F8EF
F8F0
F8F1
F8F2
F8F3
F8F4
F8F5
F8F6
F8F7
F8F8
F8F9
F8FA
F8FB
F8FC
F8FD
F8FE
F8FF
豈
F900
更
F901
車
F902
賈
F903
滑
F904
串
F905
句
F906
龜
F907
龜
F908
契
F909
金
F90A
喇
F90B
奈
F90C
懶
F90D
癩
F90E
羅
F90F
蘿
F910
螺
F911
裸
F912
邏
F913
樂
F914
洛
F915
烙
F916
珞
F917
落
F918
酪
F919
駱
F91A
亂
F91B
卵
F91C
欄
F91D
爛
F91E
蘭
F91F
鸞
F920
嵐
F921
濫
F922
藍
F923
襤
F924
拉
F925
臘
F926
蠟
F927
廊
F928
朗
F929
浪
F92A
狼
F92B
郎
F92C
來
F92D
冷
F92E
勞
F92F
擄
F930
櫓
F931
爐
F932
盧
F933
老
F934
蘆
F935
虜
F936
路
F937
露
F938
魯
F939
鷺
F93A
碌
F93B
祿
F93C
綠
F93D
菉
F93E
錄
F93F
鹿
F940
論
F941
壟
F942
弄
F943
籠
F944
聾
F945
牢
F946
磊
F947
賂
F948
雷
F949
壘
F94A
屢
F94B
樓
F94C
淚
F94D
漏
F94E
累
F94F
縷
F950
陋
F951
勒
F952
肋
F953
凜
F954
凌
F955
稜
F956
綾
F957
菱
F958
陵
F959
讀
F95A
拏
F95B
樂
F95C
諾
F95D
丹
F95E
寧
F95F
怒
F960
率
F961
異
F962
北
F963
磻
F964
便
F965
復
F966
不
F967
泌
F968
數
F969
索
F96A
參
F96B
塞
F96C
省
F96D
葉
F96E
說
F96F
殺
F970
辰
F971
沈
F972
拾
F973
若
F974
掠
F975
略
F976
亮
F977
兩
F978
凉
F979
梁
F97A
糧
F97B
良
F97C
諒
F97D
量
F97E
勵
F97F
呂
F980
女
F981
廬
F982
旅
F983
濾
F984
礪
F985
閭
F986
驪
F987
麗
F988
黎
F989
力
F98A
曆
F98B
歷
F98C
轢
F98D
年
F98E
憐
F98F
戀
F990
撚
F991
漣
F992
煉
F993
璉
F994
秊
F995
練
F996
聯
F997
輦
F998
蓮
F999
連
F99A
鍊
F99B
列
F99C
劣
F99D
咽
F99E
烈
F99F
裂
F9A0
說
F9A1
廉
F9A2
念
F9A3
捻
F9A4
殮
F9A5
簾
F9A6
獵
F9A7
令
F9A8
囹
F9A9
寧
F9AA
嶺
F9AB
怜
F9AC
玲
F9AD
瑩
F9AE
羚
F9AF



    for i_r in range(num_rows):
        for i_c in range(num_columns):
            for i_rr in range(3):
                board[i_r][i_c].append([])
                for i in range(3):
                    board[i_r][i_c][i_rr].append(' ')  
    return board


def extra_turn(board, ball_pos, num_columns):
    counter = 0

    for i_rr in range(3):
        for i_cc in range(3):
            current_space = board[ball_pos[0]][ball_pos[1]][i_rr][i_cc]
            if current_space != ' ' and current_space != '⊙' and current_space != 'x':
                counter += 1
    if ball_pos[0] == 4 and ball_pos[1] == 2 and counter % 2 == 0:
        return True
    if ball_pos[1] == 0 or ball_pos[1] == num_columns - 1:
        return True
    if counter == 1:
        return False
    elif counter % 2 != 0:
        return True
    else:
        return False


def fun_time(switch, len_time):
    if switch
    
(◕‿◕) 
SYMBL

Homepage
›  
Unicode
›  
Character Table
List of Unicode Symbols
Version: 15.1.0
Release date: September 12, 2023
Total number of characters: 149 813
Almost half a million symbols of all kinds, including arrows, mathematical signs, emojis, hieroglyphics, and ancient scripts, are available. Each symbol lies in its assigned cell in the table. Just scroll down to explore the whole variety of Unicode characters. Or use the block navigation on the right — each character block occupies its range in the table divided into 17 planes. Try 
△
Geometric Shapes
 for example. Hover over a character you like to see its name or copy it. Click on the symbol name and go to a separate page to study it.
Complete Unicode Character Table on One Page
ﶀ
FD80
ﶁ
FD81
ﶂ
FD82
ﶃ
FD83
ﶄ
FD84
ﶅ
FD85
ﶆ
FD86
ﶇ
FD87
ﶈ
FD88
ﶉ
FD89
ﶊ
FD8A
ﶋ
FD8B
ﶌ
FD8C
ﶍ
FD8D
ﶎ
FD8E
ﶏ
FD8F
FD90
FD91
ﶒ
FD92
ﶓ
FD93
ﶔ
FD94
ﶕ
FD95
ﶖ
FD96
ﶗ
FD97
ﶘ
FD98
ﶙ
FD99
ﶚ
FD9A
ﶛ
FD9B
ﶜ
FD9C
ﶝ
FD9D
ﶞ
FD9E
ﶟ
FD9F
ﶠ
FDA0
ﶡ
FDA1
ﶢ
FDA2
ﶣ
FDA3
ﶤ
FDA4
ﶥ
FDA5
ﶦ
FDA6
ﶧ
FDA7
ﶨ
FDA8
ﶩ
FDA9
ﶪ
FDAA
ﶫ
FDAB
ﶬ
FDAC
ﶭ
FDAD
ﶮ
FDAE
ﶯ
FDAF
ﶰ
FDB0
ﶱ
FDB1
ﶲ
FDB2
ﶳ
FDB3
ﶴ
FDB4
ﶵ
FDB5
ﶶ
FDB6
ﶷ
FDB7
ﶸ
FDB8
ﶹ
FDB9
ﶺ
FDBA
ﶻ
FDBB
ﶼ
FDBC
ﶽ
FDBD
ﶾ
FDBE
ﶿ
FDBF
ﷀ
FDC0
ﷁ
FDC1
ﷂ
FDC2
ﷃ
FDC3
ﷄ
FDC4
ﷅ
FDC5
ﷆ
FDC6
ﷇ
FDC7
FDC8
FDC9
FDCA
FDCB
FDCC
FDCD
FDCE
﷏
FDCF
﷐
FDD0
﷑
FDD1
﷒
FDD2
﷓
FDD3
﷔
FDD4
﷕
FDD5
﷖
FDD6
﷗
FDD7
﷘
FDD8
﷙
FDD9
﷚
FDDA
﷛
FDDB
﷜
FDDC
﷝
FDDD
﷞
FDDE
﷟
FDDF
﷠
FDE0
﷡
FDE1
﷢
FDE2
﷣
FDE3
﷤
FDE4
﷥
FDE5
﷦
FDE6
﷧
FDE7
﷨
FDE8
﷩
FDE9
﷪
FDEA
﷫
FDEB
﷬
FDEC
﷭
FDED
﷮
FDEE
﷯
FDEF
ﷰ
FDF0
ﷱ
FDF1
ﷲ
FDF2
ﷳ
FDF3
ﷴ
FDF4
ﷵ
FDF5
ﷶ
FDF6
ﷷ
FDF7
ﷸ
FDF8
ﷹ
FDF9
ﷺ
FDFA
ﷻ
FDFB
﷼
FDFC
﷽
FDFD
﷾
FDFE
﷿
FDFF
︀
FE00
︁
FE01
︂
FE02
︃
FE03
︄
FE04
︅
FE05
︆
FE06
︇
FE07
︈
FE08
︉
FE09
︊
FE0A
︋
FE0B
︌
FE0C
︍
FE0D
︎
FE0E
️
FE0F
︐
FE10
︑
FE11
︒
FE12
︓
FE13
︔
FE14
︕
FE15
︖
FE16
︗
FE17
︘
FE18
︙
FE19
FE1A
FE1B
FE1C
FE1D
FE1E
FE1F
︠
FE20
︡
FE21
︢
FE22
︣
FE23
︤
FE24
︥
FE25
︦
FE26
︧
FE27
︨
FE28
︩
FE29
︪
FE2A
︫
FE2B
︬
FE2C
︭
FE2D
︮
FE2E
︯
FE2F
︰
FE30
︱
FE31
︲
FE32
︳
FE33
︴
FE34
︵
FE35
︶
FE36
︷
FE37
︸
FE38
︹
FE39
︺
FE3A
︻
FE3B
︼
FE3C
︽
FE3D
︾
FE3E
︿
FE3F
﹀
FE40
﹁
FE41
﹂
FE42
﹃
FE43
﹄
FE44
﹅
FE45
﹆
FE46
﹇
FE47
﹈
FE48
﹉
FE49
﹊
FE4A
﹋
FE4B
﹌
FE4C
﹍
FE4D
﹎
FE4E
﹏
FE4F

== 1:
        time.sleep(len_time)
        return True
    else:
        time.sleep(0)
        return False




def draw_row(row_number, num_columns, board):
    
    for i_rr in range(3):
        

        
(◕‿◕) 
SYMBL

Homepage
›  
Unicode
›  
Character Table
List of Unicode Symbols
Version: 15.1.0
Release date: September 12, 2023
Total number of characters: 149 813
Almost half a million symbols of all kinds, including arrows, mathematical signs, emojis, hieroglyphics, and ancient scripts, are available. Each symbol lies in its assigned cell in the table. Just scroll down to explore the whole variety of Unicode characters. Or use the block navigation on the right — each character block occupies its range in the table divided into 17 planes. Try 
△
Geometric Shapes
 for example. Hover over a character you like to see its name or copy it. Click on the symbol name and go to a separate page to study it.
Complete Unicode Character Table on One Page
꩐
AA50
꩑
AA51
꩒
AA52
꩓
AA53
꩔
AA54
꩕
AA55
꩖
AA56
꩗
AA57
꩘
AA58
꩙
AA59
AA5A
AA5B
꩜
AA5C
꩝
AA5D
꩞
AA5E
꩟
AA5F
ꩠ
AA60
ꩡ
AA61
ꩢ
AA62
ꩣ
AA63
ꩤ
AA64
ꩥ
AA65
ꩦ
AA66
ꩧ
AA67
ꩨ
AA68
ꩩ
AA69
ꩪ
AA6A
ꩫ
AA6B
ꩬ
AA6C
ꩭ
AA6D
ꩮ
AA6E
ꩯ
AA6F
ꩰ
AA70
ꩱ
AA71
ꩲ
AA72
ꩳ
AA73
ꩴ
AA74
ꩵ
AA75
ꩶ
AA76
꩷
AA77
꩸
AA78
꩹
AA79
ꩺ
AA7A
ꩻ
AA7B
ꩼ
AA7C
ꩽ
AA7D
ꩾ
AA7E
ꩿ
AA7F
ꪀ
AA80
ꪁ
AA81
ꪂ
AA82
ꪃ
AA83
ꪄ
AA84
ꪅ
AA85
ꪆ
AA86
ꪇ
AA87
ꪈ
AA88
ꪉ
AA89
ꪊ
AA8A
ꪋ
AA8B
ꪌ
AA8C
ꪍ
AA8D
ꪎ
AA8E
ꪏ
AA8F
ꪐ
AA90
ꪑ
AA91
ꪒ
AA92
ꪓ
AA93
ꪔ
AA94
ꪕ
AA95
ꪖ
AA96
ꪗ
AA97
ꪘ
AA98
ꪙ
AA99
ꪚ
AA9A
ꪛ
AA9B
ꪜ
AA9C
ꪝ
AA9D
ꪞ
AA9E
ꪟ
AA9F
ꪠ
AAA0
ꪡ
AAA1
ꪢ
AAA2
ꪣ
AAA3
ꪤ
AAA4
ꪥ
AAA5
ꪦ
AAA6
ꪧ
AAA7
ꪨ
AAA8
ꪩ
AAA9
ꪪ
AAAA
ꪫ
AAAB
ꪬ
AAAC
ꪭ
AAAD
ꪮ
AAAE
ꪯ
AAAF
ꪰ
AAB0
ꪱ
AAB1
ꪲ
AAB2
ꪳ
AAB3
ꪴ
AAB4
ꪵ
AAB5
ꪶ
AAB6
ꪷ
AAB7
ꪸ
AAB8
ꪹ
AAB9
ꪺ
AABA
ꪻ
AABB
ꪼ
AABC
ꪽ
AABD
ꪾ
AABE
꪿
AABF
ꫀ
AAC0
꫁
AAC1
ꫂ
AAC2
AAC3
AAC4
AAC5
AAC6
AAC7
AAC8
AAC9
AACA
AACB
AACC
AACD
AACE
AACF
AAD0
AAD1
AAD2
AAD3
AAD4
AAD5
AAD6
AAD7
AAD8
AAD9
AADA
ꫛ
AADB
ꫜ
AADC
ꫝ
AADD
꫞
AADE
꫟
AADF
ꫠ
AAE0
ꫡ
AAE1
ꫢ
AAE2
ꫣ
AAE3
ꫤ
AAE4
ꫥ
AAE5
ꫦ
AAE6
ꫧ
AAE7
ꫨ
AAE8
ꫩ
AAE9
ꫪ
AAEA
ꫫ
AAEB
ꫬ
AAEC
ꫭ
AAED
ꫮ
AAEE
ꫯ
AAEF
꫰
AAF0
꫱
AAF1
ꫲ
AAF2
ꫳ
AAF3
ꫴ
AAF4
ꫵ
AAF5
꫶
AAF6
AAF7
AAF8
AAF9
AAFA
AAFB
AAFC
AAFD
AAFE
AAFF
AB00
ꬁ
AB01
ꬂ
AB02
ꬃ
AB03
ꬄ
AB04
ꬅ
AB05
ꬆ
AB06
AB07
AB08
ꬉ
AB09
ꬊ
AB0A
ꬋ
AB0B
ꬌ
AB0C
ꬍ
AB0D
ꬎ
AB0E
AB0F
AB10
ꬑ
AB11
ꬒ
AB12
ꬓ
AB13
ꬔ
AB14
ꬕ
AB15
ꬖ
AB16
AB17
AB18
AB19
AB1A
AB1B
AB1C
AB1D
AB1E
AB1F

Back to top


0: Basic Multilingual Plane
Basic Latin
0000–007F

Latin-1 Supplement
0080–00FF

Latin Extended-A
0100–017F

Latin Extended-B
0180–024F

IPA Extensions
0250–02AF

Spacing Modifier Letters
02B0–02FF

Combining Diacritical Marks
0300–036F

Greek and Coptic
0370–03FF

Cyrillic
0400–04FF

Cyrillic Supplement
0500–052F

Armenian
0530–058F

Hebrew
0590–05FF

Arabic
0600–06FF

Syriac
0700–074F

Arabic Supplement
0750–077F

Thaana
0780–07BF

NKo
07C0–07FF

Samaritan
0800–083F

Mandaic
0840–085F

Syriac Supplement
0860–086F

Arabic Extended-B
0870–089F

Arabic Extended-A
08A0–08FF

Devanagari
0900–097F

Bengali
0980–09FF

Gurmukhi
0A00–0A7F

Gujarati
0A80–0AFF

Oriya
0B00–0B7F

Tamil
0B80–0BFF

Telugu
0C00–0C7F

Kannada
0C80–0CFF

Malayalam
0D00–0D7F

Sinhala
0D80–0DFF

Thai
0E00–0E7F

Lao
0E80–0EFF

Tibetan
0F00–0FFF

Myanmar
1000–109F

Georgian
10A0–10FF

Hangul Jamo
1100–11FF

Ethiopic
1200–137F

Ethiopic Supplement
1380–139F

Cherokee
13A0–13FF

Unified Canadian Aboriginal Syllabics
1400–167F

Ogham
1680–169F

Runic
16A0–16FF

Tagalog
1700–171F

Hanunoo
1720–173F

Buhid
1740–175F

Tagbanwa
1760–177F

Khmer
1780–17FF

Mongolian
1800–18AF

Unified Canadian Aboriginal Syllabics Extended
18B0–18FF

Limbu
1900–194F

Tai Le
1950–197F

New Tai Lue
1980–19DF

Khmer Symbols
19E0–19FF

Buginese
1A00–1A1F

Tai Tham
1A20–1AAF

Combining Diacritical Marks Extended
1AB0–1AFF

Balinese
1B00–1B7F

Sundanese
1B80–1BBF

Batak
1BC0–1BFF

Lepcha
1C00–1C4F

Ol Chiki
1C50–1C7F

Cyrillic Extended C
1C80–1C8F

Georgian Extended
1C90–1CBF

Sundanese Supplement
1CC0–1CCF

Vedic Extensions
1CD0–1CFF

Phonetic Extensions
1D00–1D7F

Phonetic Extensions Supplement
1D80–1DBF

Combining Diacritical Marks Supplement
1DC0–1DFF

Latin Extended Additional
1E00–1EFF

Greek Extended
1F00–1FFF

General Punctuation
2000–206F

Superscripts and Subscripts
2070–209F

Currency Symbols
20A0–20CF

Combining Diacritical Marks for Symbols
20D0–20FF

Letterlike Symbols
2100–214F

Number Forms
2150–218F

Arrows
2190–21FF

Mathematical Operators
2200–22FF

Miscellaneous Technical
2300–23FF

Control Pictures
2400–243F

Optical Character Recognition
2440–245F

Enclosed Alphanumerics
2460–24FF

Box Drawing
2500–257F

Block Elements
2580–259F

Geometric Shapes
25A0–25FF

Miscellaneous Symbols
2600–26FF

Dingbats
2700–27BF

Miscellaneous Mathematical Symbols-A
27C0–27EF

Supplemental Arrows-A
27F0–27FF

Braille Patterns
2800–28FF

Supplemental Arrows-B
2900–297F

Miscellaneous Mathematical Symbols-B
2980–29FF

Supplemental Mathematical Operators
2A00–2AFF

Miscellaneous Symbols and Arrows
2B00–2BFF

Glagolitic
2C00–2C5F

Latin Extended-C
2C60–2C7F

Coptic
2C80–2CFF

Georgian Supplement
2D00–2D2F

Tifinagh
2D30–2D7F

Ethiopic Extended
2D80–2DDF

Cyrillic Extended-A
2DE0–2DFF

Supplemental Punctuation
2E00–2E7F

CJK Radicals Supplement
2E80–2EFF

Kangxi Radicals
2F00–2FDF

Not defined
2FE0–2FEF

Ideographic Description Characters
2FF0–2FFF

CJK Symbols and Punctuation
3000–303F

Hiragana
3040–309F

Katakana
30A0–30FF

Bopomofo
3100–312F

Hangul Compatibility Jamo
3130–318F

Kanbun
3190–319F

Bopomofo Extended
31A0–31BF

CJK Strokes
31C0–31EF

Katakana Phonetic Extensions
31F0–31FF

Enclosed CJK Letters and Months
3200–32FF

CJK Compatibility
3300–33FF

CJK Unified Ideographs Extension A
3400–4DBF

Yijing Hexagram Symbols
4DC0–4DFF

CJK Unified Ideographs
4E00–9FFF

Yi Syllables
A000–A48F

Yi Radicals
A490–A4CF

Lisu
A4D0–A4FF

Vai
A500–A63F

Cyrillic Extended-B
A640–A69F

Bamum
A6A0–A6FF

Modifier Tone Letters
A700–A71F

Latin Extended-D
A720–A7FF

Syloti Nagri
A800–A82F

Common Indic Number Forms
A830–A83F

Phags-pa
A840–A87F

Saurashtra
A880–A8DF

Devanagari Extended
A8E0–A8FF

Kayah Li
A900–A92F

Rejang
A930–A95F

Hangul Jamo Extended-A
A960–A97F

Javanese
A980–A9DF

Myanmar Extended-B
A9E0–A9FF

Cham
AA00–AA5F

Myanmar Extended-A
AA60–AA7F

Tai Viet
AA80–AADF

Meetei Mayek Extensions
AAE0–AAFF

Ethiopic Extended-A
AB00–AB2F

Latin Extended-E
AB30–AB6F

Cherokee Supplement
AB70–ABBF

Meetei Mayek
ABC0–ABFF

Hangul Syllables
AC00–D7AF

Hangul Jamo Extended-B
D7B0–D7FF

High Surrogates
D800–DB7F

High Private Use Surrogates
DB80–DBFF

Low Surrogates
DC00–DFFF

Private Use Area
E000–F8FF

CJK Compatibility Ideographs
F900–FAFF

Alphabetic Presentation Forms
FB00–FB4F

Arabic Presentation Forms-A
FB50–FDFF

Variation Selectors
FE00–FE0F

Vertical Forms
FE10–FE1F

Combining Half Marks
FE20–FE2F

CJK Compatibility Forms
FE30–FE4F

Small Form Variants
FE50–FE6F

Arabic Presentation Forms-B
FE70–FEFF

Halfwidth and Fullwidth Forms
FF00–FFEF

Specials
FFF0–FFFF

1: Supplementary Multilingual Plane
2: Supplementary Ideographic Plane
3: Tertiary Ideographic Plane
4-13: Not Used
14: Supplementary Special-purpose Plane
15: Supplementary Private Use Area Plane – A
16: Supplementary Private Use Area Plane – B
(◕‿◕)
SYMBL
All images of emoji and characters on the website are for informational purposes, the rights belong to their authors and cannot be used for commercial purposes without their consent.
All character names are official Unicode® names. Code points listed are part of the Unicode Standard.
© SYMBL 2012—2024
Ex: Unicode Character Table
What’s New
Holidays
Emoji Platforms
Found a Bug? Let Us Know
Privacy Policy
1
EN
Symbols
Unicode
Alphabets
Emoji
Collections
Tools
Codes
 Art
Copied!
This site uses 🍪cookies to ensure that you get the best experience. Read more
Accept

ꪳ
U+AAB3
kes sure that it switches lines here
        if i_rr != 0:
            print('')
        
        
        print('│', end="")
        
        for i_c in range(num_columns):
            
            for i_cc in range(3):
                print(' ' + board[row_number][i_c][i_rr][i_cc], end="")
            print(' │', end="")
    print('')


def draw_row_goal(row_number, board, num_columns):
    
    for i_rr in range(3):
        
        if i_rr != 0:
            print('')
        
        
        print('        ', end="")
        print('│', end="")
        
        for i_c in range(1, num_columns + 1):
            
            for i_cc in range(3):
                print(' ' + board[row_number][i_c][i_rr][i_cc], end="")
            print(' │', end="")
    print('')


def erase_border(board, num_columns, num_rows):
    for i_r in range(num_rows):
        for i_rr in range(0, 3, 2):
            board[i_r][0][i_rr][1] = ' '
    for i_r in range(num_rows):
        for i_rr in range(3):
            board[i_r][0][i_rr][0] = ' '

    for i_r in range(num_rows):
        for i_rr in range(3):
            board[i_r][num_columns - 1][i_rr][2] = ' '
    for i_r in range(num_rows):
        for i_rr in range(0, 3, 2):
            board[i_r][num_columns - 1][i_rr][1] = ' '


def show_border(board, num_columns, ball_pos):
    if (board[ball_pos[0]][ball_pos[1]][1][1] != ' ') and ball_pos[1] == 0:
        board[ball_pos[0]][0][0][1] = '|'
        board[ball_pos[0]][0][2][1] = '|'
        board[ball_pos[0]][0][0][0] = '\\'
        board[ball_pos[0]][0][2][0] = '/'
        board[ball_pos[0]][0][1][0] = '-'

    elif (board[ball_pos[0]][ball_pos[1]][1][1] != ' ') and ball_pos[1] == (num_columns - 1):
        board[ball_pos[0]][num_columns - 1][0][1] = '|'
        board[ball_pos[0]][num_columns - 1][2][1] = '|'
        board[ball_pos[0]][num_columns - 1][0][2] = '/'
        board[ball_pos[0]][num_columns - 1][2][2] = '\\'
        board[ball_pos[0]][num_columns - 1][1][2] = '-'


def draw_board(board, num_rows, num_columns):
    print('            x       x       x            ')
    print('        ┌───────┬───────┬───────┐')
    draw_row_goal(0, board, 3)
    print('┌───────┼───────┼───────┼───────┼───────┐ ')
    
    for i in range(1, num_rows - 1):
        draw_row(i, num_columns, board)
        if i < 7:
            print('├───────┼───────┼───────┼───────┼───────┤ ')
    print('└───────┼───────┼───────┼───────┼───────┘')
    draw_row_goal(8, board, 3)
    print('        └───────┴───────┴───────┘')
    print('            ⊙       ⊙       ⊙            ')




def make_move(direction, ball_pos, board, player):
    
    board[ball_pos[0]][ball_pos[1]][1][1] = ' '

    
    
    
    

    if direction == 'north':
        if not board[ball_pos[0]][ball_pos[1]][0][1] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][0][1] = '|'
        board[ball_pos[0] - 1][ball_pos[1]][2][1] = '|'
        ball_pos[0] -= 1

    elif direction == 'south':
        if not board[ball_pos[0]][ball_pos[1]][2][1] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][2][1] = '|'
        board[ball_pos[0] + 1][ball_pos[1]][0][1] = '|'
        ball_pos[0] += 1

    elif direction == 'east':
        if not board[ball_pos[0]][ball_pos[1]][1][2] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][1][2] = '—'
        board[ball_pos[0]][ball_pos[1] + 1][1][0] = '—'
        ball_pos[1] += 1

    elif direction == 'west':
        if not board[ball_pos[0]][ball_pos[1]][1][0] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][1][0] = '—'
        board[ball_pos[0]][ball_pos[1] - 1][1][2] = '—'
        ball_pos[1] -= 1

    elif direction == 'northeast':
        if not board[ball_pos[0]][ball_pos[1]][0][2] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][0][2] = '/'
        board[ball_pos[0] - 1][ball_pos[1] + 1][2][0] = '/'
        ball_pos[1] += 1
        ball_pos[0] -= 1

    elif direction == 'northwest':
        if not board[ball_pos[0]][ball_pos[1]][0][0] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][0][0] = '\\'
        board[ball_pos[0] - 1][ball_pos[1] - 1][2][2] = '\\'
        ball_pos[1] -= 1
        ball_pos[0] -= 1

    elif direction == 'southwest':
        if not board[ball_pos[0]][ball_pos[1]][0][0] == ' ':
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][2][0] = '/'
        board[ball_pos[0] + 1][ball_pos[1] - 1][0][2] = '/'
        ball_pos[1] -= 1
        ball_pos[0] += 1

    elif direction == 'southeast':
        if not (board[ball_pos[0]][ball_pos[1]][2][2] == ' '):
            return "illegal"
        board[ball_pos[0]][ball_pos[1]][2][2] = '\\'
        board[ball_pos[0] + 1][ball_pos[1] + 1][0][0] = '\\'
        ball_pos[1] += 1
        ball_pos[0] += 1

    
    
    else:
        return 'wrong format'
    
    board[ball_pos[0]][ball_pos[1]][1][1] = player

    return 'legal'


def find_winner(board, num_rows):
    for i in range(1, 4):
        if board[num_rows - 1][i][1][1] == 'x':
            return 'x'

    for i in range(1, 4):
        if board[0][i][1][1] == '⊙':
            return '⊙'

(◕‿◕) 
SYMBL

Search results on demand “diagonal”: 119
🮽
Negative Diagonal Cross
Symbols for Legacy Computing
U+1FBBD
&
Copy
🮿
Negative Diagonal Diamond
Symbols for Legacy Computing
U+1FBBF
&
Copy
⟋
Mathematical Rising Diagonal
Miscellaneous Mathematical Symbols-A
U+27CB
&
Copy
⟍
Mathematical Falling Diagonal
Miscellaneous Mathematical Symbols-A
U+27CD
&
Copy
⋰
Up Right Diagonal Ellipsis
Mathematical Operators
U+22F0
&
Copy
⋱
Down Right Diagonal Ellipsis
Mathematical Operators
U+22F1
&
Copy
⤫
Rising Diagonal Crossing Falling Diagonal
Supplemental Arrows-B
U+292B
&
Copy
⤬
Falling Diagonal Crossing Rising Diagonal
Supplemental Arrows-B
U+292C

ˠ
02E0
ˡ
02E1
ˢ
02E2
ˣ
02E3
ˤ
02E4
˥
02E5
˦
02E6
˧
02E7
˨
02E8
˩
02E9
˪
02EA
˫
02EB
ˬ
02EC
˭
02ED
ˮ
02EE
˯
02EF
˰
02F0
˱
02F1
˲
02F2
˳
02F3
˴
02F4
˵
02F5
˶
02F6
˷
02F7
˸
02F8
˹
02F9
˺
02FA
˻
02FB
˼
02FC
˽
02FD

Graduation Cap
Top Hat
School Satchel
Dress
Bikini
Purse
Mans Shoe
Athletic Shoe
Pouch
Handbag
T-Shirt
Womans Sandal
Crown
Lipstick
Womans Clothes
Womans Boots
Ring
Kimono
Gem Stone
Eyeglasses
Jeans
Necktie
High-Heeled Shoe
Prayer Beads
Womans Hat
Dark Sunglasses
Shopping Bags
Billed Cap
Safety Vest
Scarf
Gloves
Coat
Socks
Sari
Hiking Boot
Lab Coat
Flat Shoe
Goggles
Military Helmet
Ballet Shoes
Thong Sandal
One-piece Swimsuit
Briefs
Shorts
Folding Hand Fan
Hair Pick
Helmet with White Cross
Sound
Public Address Loudspeaker
Cheering Megaphone
Postal Horn
Speaker with Cancellation Stroke
Speaker
Speaker with Three Sound Waves
Bell
Bell with Cancellation Stroke
Speaker with One Sound Wave
Music
Control Knobs
Studio Microphone
Microphone
Level Slider
Multiple Musical Notes
Musical Score
Musical Note
Headphone
Radio
Musical Instrument
Violin
Trumpet
Saxophone
Musical Keyboard
Guitar
Drum with Drumsticks
Banjo
Accordion
Long Drum
Flute
Maracas
AD

AD

Phone
Telephone Receiver
Fax Machine
Mobile Phone
Pager
Mobile Phone with Rightwards Arrow At Left
Black Telephone
Computer
Dvd
Optical Disc
Floppy Disk
Minidisc
Personal Computer
Three Button Mouse
Trackball
Desktop Computer
Printer
Battery
Electric Plug
Abacus
Low Battery
Keyboard
Light & Video
Movie Camera
Clapper Board
Izakaya Lantern
Film Frames
Video Camera
Camera with Flash
Camera
Electric Light Bulb
Television
Videocassette
Film Projector
Candle
Right-Pointing Magnifying Glass
Left-Pointing Magnifying Glass
Electric Torch
Diya Lamp
Paper Book
Label
Bookmark Tabs
Notebook
Page with Curl
Closed Book
Ledger
Green Book
Notebook with Decorative Cover
Orange Book
Open Book
Blue Book
Scroll
Books
Page Facing Up
Newspaper
Bookmark
Rolled-Up Newspaper
Money
Money with Wings
Banknote with Pound Sign
Chart with Upwards Trend and Yen Sign
Banknote with Euro Sign
Banknote with Dollar Sign
Banknote with Yen Sign
Credit Card
Money Bag
Receipt
Coin
Mail
Closed Mailbox with Lowered Flag
Closed Mailbox with Raised Flag
Open Mailbox with Raised Flag
Open Mailbox with Lowered Flag
E-Mail Symbol
Outbox Tray
Inbox Tray
Package
Incoming Envelope
Envelope with Downwards Arrow Above
Postbox
Ballot Box with Ballot
Envelope
AD
AD
•
16+

playhop.com


AD


snapnewsfeed.network
AD
T-shirts, stamps, accessories
Writing
Memo
Lower Left Crayon
Lower Left Fountain Pen
Lower Left Paintbrush
Lower Left Ballpoint Pen
Black Nib
Pencil
Office
Chart with Upwards Trend
Pushpin
Bar Chart
Triangular Ruler
Clipboard
Chart with Downwards Trend
Straight Ruler
File Folder
Round Pushpin
Briefcase
Calendar
Tear-Off Calendar
Card Index
Open File Folder
Paperclip
File Cabinet
Card File Box
Card Index Dividers
Linked Paperclips
Spiral Calendar Pad
Wastebasket
Spiral Note Pad
Black Scissors
Lock
Open Lock
Lock
Key
Closed Lock with Key
Lock with Ink Pen
Old Key
Tool
Bow And Arrow
Compression
Dagger Knife
Wrench
Link Symbol
Nut and Bolt
Hammer
Pistol
Shield
Hammer and Wrench
Magnet
Probing Cane
Toolbox
Hook
Ladder
Axe
Carpentry Saw
Boomerang
Screwdriver
Gear
Chains
Pick
Crossed Swords
Scales
Hammer and Pick
Science
Satellite Antenna
Telescope
Microscope
Test Tube
Petri Dish
Dna Double Helix
Alembic
Medical
Syringe
Pill
Stethoscope
Adhesive Bandage
Drop Of Blood
Crutch
X-ray
Household
Bathtub
Elevator
Couch and Lamp
Shopping Trolley
Shower
Bed
Toilet
Door
Lotion Bottle
Fire Extinguisher
Safety Pin
Basket
Broom
Bar of Soap
Sponge
Roll of Paper
Toothbrush
Mouse Trap
Bucket
Plunger
Window
Mirror
Chair
Razor
Bubbles

AD

Other Objects
Moyai
Smoking Symbol
Placard
Headstone
Identification Card
Hamsa
Funeral Urn
Coffin
The emoji group called ¨objects“ is dedicated to various things that people use as they live and breathe.

Numerous household items: clothes, gadgets, furniture, books, money, electronic devices.
Equipment related to professional activity: music instruments, building tools, office stationery, medical and scientific devices.
Free-time attributes: games and cultural environment.
Whatever you do in your leisure time or professional career, every moment of life can be demonstrated with an emoji. From pacifier to coffin.
˾
02FE
˿
02FF
̀
0300
́
0301
̂
0302
̃
0303
̄
0304
̅
0305
̆
0306
̇
0307
̈
0308
̉
0309
̊
030A
̋
030B
̌
030C
̍
030D
̎
030E
̏
030F
̐
0310
̑
0311
̒
0312
̓
0313
̔
0314
̕
0315
̖
0316
̗
0317
̘
0318
̙
0319
̚
031A
̛
031B
̜
031C
̝
031D
̞
031E
̟
031F
̠
0320
̡
0321
̢
0322
̣
0323
̤
0324
̥
0325
̦
0326
̧
0327
̨
0328
̩
0329
̪
032A
̫
032B
̬
032C
̭
032D
̮
032E
̯
032F
̰
0330
̱
0331
̲
0332
̳
0333
̴
0334
̵
0335
̶
0336
̷
0337
̸
0338
̹
0339
̺
033A
̻
033B
̼
033C
̽
033D
̾
033E
̿
033F
̀
0340
́
0341
͂
0342
̓
0343
̈́
0344
ͅ
0345
͆
0346
͇
0347
͈
0348
͉
0349
͊
034A
͋
034B
͌
034C
͍
034D
͎
034E
͏
034F
͐
0350
͑
0351
͒
0352
͓
0353


͔
0354
͕
0355
͖
0356

괰
AD30
괱
AD31
괲
AD32
괳
AD33
괴
AD34
괵
AD35
괶
AD36
괷
AD37
괸
AD38
괹
AD39
괺
AD3A
괻
AD3B
괼
AD3C
괽
AD3D
괾
AD3E
괿
AD3F
굀
AD40
굁
AD41
굂
AD42
굃
AD43
굄
AD44
굅
AD45
굆
AD46
굇
AD47
굈
AD48
굉
AD49
굊
AD4A
굋
AD4B
굌
AD4C
굍
AD4D
굎
AD4E
굏
AD4F
교
AD50
굑
AD51
굒
AD52
굓
AD53
굔
AD54
굕
AD55
굖
AD56
굗
AD57
굘
AD58
굙
AD59
굚
AD5A
굛
AD5B
굜
AD5C
굝
AD5D
굞
AD5E
굟
AD5F
굠
AD60
굡
AD61
굢
AD62
굣
AD63
굤
AD64
굥
AD65
굦
AD66
굧
AD67
굨
AD68
굩
AD69
굪
AD6A
굫
AD6B
구
AD6C
국
AD6D
굮
AD6E
굯
AD6F
군
AD70
굱
AD71
굲
AD72
굳
AD73
굴
AD74
굵
AD75
굶
AD76
굷
AD77
굸
AD78
굹
AD79
굺
AD7A
굻
AD7B
굼
AD7C
굽
AD7D
굾
AD7E
굿
AD7F
궀
AD80
궁
AD81
궂
AD82
궃
AD83
궄
AD84
궅
AD85
궆
AD86
궇
AD87
궈
AD88
궉
AD89
궊
AD8A
궋
AD8B
권
AD8C
궍
AD8D
궎
AD8E
궏
AD8F
궐
AD90
궑
AD91
궒
AD92
궓
AD93
궔
AD94
궕
AD95
궖
AD96
궗
AD97
궘
AD98
궙
AD99
궚
AD9A
궛
AD9B
궜
AD9C
궝
AD9D
궞
AD9E
궟
AD9F
궠
ADA0
궡
ADA1
궢
ADA2
궣
ADA3
궤
ADA4
궥
ADA5
궦
ADA6
궧
ADA7
궨
ADA8
궩
ADA9
궪
ADAA
궫
ADAB
궬
ADAC
궭
ADAD
궮
ADAE
궯
ADAF
궰
ADB0
궱
ADB1
궲
ADB2
궳
ADB3
궴
ADB4
궵
ADB5
궶
ADB6
궷
ADB7
궸
ADB8
궹
ADB9
궺
ADBA
궻
ADBB
궼
ADBC
궽
ADBD
궾
ADBE
궿
ADBF
귀
ADC0
귁
ADC1
귂
ADC2
귃
ADC3
귄
ADC4
귅
ADC5
귆
ADC6
귇
ADC7
귈
ADC8
귉
ADC9
귊
ADCA
귋
ADCB
귌
ADCC
귍
ADCD
귎
ADCE
귏
ADCF
귐
ADD0
귑
ADD1
귒
ADD2
귓
ADD3
귔
ADD4
귕
ADD5
귖
ADD6
귗
ADD7
귘
ADD8
귙
ADD9
귚
ADDA
귛
ADDB
규
ADDC
귝
ADDD
귞
ADDE
귟
ADDF
균
ADE0
귡
ADE1
귢
ADE2
귣
ADE3
귤
ADE4
귥
ADE5
귦
ADE6
귧
ADE7
귨
ADE8
귩
ADE9
귪
ADEA
귫
ADEB
귬
ADEC
귭
ADED
귮
ADEE
귯
ADEF
귰
ADF0
귱
ADF1
귲
ADF2
귳
ADF3
귴
ADF4
귵
ADF5
귶
ADF6
귷
ADF7
그
ADF8
극
ADF9
귺
ADFA
귻
ADFB
근
ADFC
귽
ADFD
귾
ADFE
귿
ADFF


͗
0357
͘
0358
͙
0359
͚
035A
͛
035B
͜
035C
͝
035D
͞
035E
͟
035F
͠
0360
͡
0361
͢
0362
ͣ
0363
ͤ
0364
ͥ
0365
ͦ
0366
ͧ
0367
ͨ
0368
ͩ
0369
ͪ
036A
ͫ
036B
ͬ
036C
ͭ
036D
ͮ
036E
ͯ
036F
Ͱ
0370
ͱ
0371
Ͳ
0372
ͳ
0373
ʹ
0374
͵
0375
Ͷ
0376
ͷ
0377
0378
0379
ͺ
037A
ͻ
037B
ͼ
037C
ͽ
037D
;
037E
Ϳ
037F
0380
0381
0382
0383
΄
0384
΅
0385
Ά
0386
·
0387
Έ
0388
Ή
0389
Ί
038A
038B
Ό
038C
038D
Ύ
038E
Ώ
038F
ΐ
0390
Α
0391
Β
0392
Γ
0393
Δ
0394
Ε
0395
Ζ
0396
Η
0397
Θ
0398
Ι
0399
Κ
039A
Λ
039B
Μ
039C
Ν
039D
Ξ
039E
Ο
039F
Π
03A0
Ρ
03A1
03A2
Σ
03A3
Τ
03A4
Υ
03A5
Φ
03A6
&
Copy
⧄
Squared Rising Diagonal Slash
Miscellaneous Mathematical Symbols-B
U+29C4
&
Copy
⧅
Squared Falling Diagonal Slash
Miscellaneous Mathematical Symbols-B
U+29C5
&
Copy
Face With Diagonal Mouth
Face With Diagonal Mouth
Symbols and Pictographs Extended-A
U+1FAE4
&
Copy
▩
Square with Diagonal Crosshatch Fill
Geometric Shapes
U+25A9
&
Copy
⤯
Falling Diagonal Crossing North East Arrow
Supplemental Arrows-B
U+292F
&
Copy
⤰
Rising Diagonal Crossing South East Arrow
Supplemental Arrows-B
U+2930
&
Copy
𝥕
Signwriting Movement-Diagonal Away Small
Sutton SignWriting
U+1D955
&
Copy
𝥖
Signwriting Movement-Diagonal Away Medium
Sutton SignWriting
U+1D956
&
Copy
𝥗
Signwriting Movement-Diagonal Away Large
Sutton SignWriting
U+1D957
&
Copy
𝥘
Signwriting Movement-Diagonal Away Largest
Sutton SignWriting
U+1D958
&
Copy
𝥙
Signwriting Movement-Diagonal Towards Small
Sutton SignWriting
U+1D959
&
Copy
𝥚
Signwriting Movement-Diagonal Towards Medium
Sutton SignWriting
U+1D95A
&
Copy
𝥛
Signwriting Movement-Diagonal Towards Large
Sutton SignWriting
U+1D95B
&
Copy
𝥜
Signwriting Movement-Diagonal Towards Largest
Sutton SignWriting
U+1D95C
&
Copy
╳
Box Drawings Light Diagonal Cross
Box Drawing
U+2573
&
Copy
𒑲
Cuneiform Punctuation Sign Diagonal Colon
Cuneiform Numbers and Punctuation
U+12472
&
Copy
𒑳
Cuneiform Punctuation Sign Diagonal Tricolon
Cuneiform Numbers and Punctuation
U+12473
&
Copy
𒑴
Cuneiform Punctuation Sign Diagonal Quadcolon
Cuneiform Numbers and Punctuation
U+12474
&
Copy
𝥝
Signwriting Movement-Diagonal Between Away Small
Sutton SignWriting
U+1D95D
&
Copy
𝥞
Signwriting Movement-Diagonal Between Away Medium
Sutton SignWriting
U+1D95E
&
Copy
𝥟
Signwriting Movement-Diagonal Between Away Large
Sutton SignWriting
U+1D95F
&
Copy
𝥠
Signwriting Movement-Diagonal Between Away Largest
Sutton SignWriting
U+1D960
&
Copy
𝥡
Signwriting Movement-Diagonal Between Towards Small
Sutton SignWriting
U+1D961
&
Copy
𝥢
Signwriting Movement-Diagonal Between Towards Medium
Sutton SignWriting
U+1D962
&
Copy
𝥣
Signwriting Movement-Diagonal Between Towards Large
Sutton SignWriting
U+1D963
&
Copy
𝥤
Signwriting Movement-Diagonal Between Towards Largest
Sutton SignWriting
U+1D964
&
Copy
🮮
Box Drawings Light Diagonal Diamond
Symbols for Legacy Computing
U+1FBAE
&
Copy
🮾
Negative Diagonal Middle Right To Lower Centre
Symbols for Legacy Computing
U+1FBBE
&
Copy
⛞
Falling Diagonal In White Circle In Black Square
Miscellaneous Symbols
U+26DE
&
Copy
ৰ
Bengali Letter Ra with Middle Diagonal
Bengali
U+09F0
&
Copy
ৱ
Bengali Letter Ra with Lower Diagonal
Bengali
U+09F1
&
Copy
◩
Square with Upper Left Diagonal Half Black
Geometric Shapes
U+25E9
&
Copy
◪
Square with Lower Right Diagonal Half Black
Geometric Shapes
U+25EA
&
Copy
⬔
Square with Upper Right Diagonal Half Black
Miscellaneous Symbols and Arrows
U+2B14
&
Copy
⬕
Square with Lower Left Diagonal Half Black
Miscellaneous Symbols and Arrows
U+2B15
&
Copy
𝣷
Signwriting Hand-Fist Thumb Side Diagonal
Sutton SignWriting
U+1D8F7
&
Copy
𝦴
Signwriting Movement-Wallplane Wave Diagonal Path Small
Sutton SignWriting
U+1D9B4
&
Copy
𝦵
Signwriting Movement-Wallplane Wave Diagonal Path Medium
Sutton SignWriting
U+1D9B5
&
Copy
𝦶
Signwriting Movement-Wallplane Wave Diagonal Path Large
Sutton SignWriting
U+1D9B6
&
Copy
Ⱦ
Latin Capital Letter T with Diagonal Stroke
Latin Extended-B
U+023E
&
Copy
╱
Box Drawings Light Diagonal Upper Right To Lower Left
Box Drawing
U+2571
&
Copy
╲
Box Drawings Light Diagonal Upper Left To Lower Right
Box Drawing
U+2572
&
Copy
...
(◕‿◕)
SYMBL
All images of emoji and characters on the website are for informational purposes, the rights belong to their authors and cannot be used for commercial purposes without their consent.
All character names are official Unicode® names. Code points listed are part of the Unicode Standard.
© SYMBL 2012—2024
Ex: Unicode Character Table
What’s New
Holidays
Emoji Platforms
Found a Bug? Let Us Know
Privacy Policy
1
EN
Symbols
Unicode
Alphabets
Emoji
Collections
Tools
Codes
 Art
Copied!
This site uses 🍪cookies to ensure that you get the best experience. Read more
Accept
