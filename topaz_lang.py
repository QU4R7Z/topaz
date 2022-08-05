import json
from collections import namedtuple

초성 = [
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]
중성 = [
    "ㅏ",
    "ㅐ",
    "ㅑ",
    "ㅒ",
    "ㅓ",
    "ㅔ",
    "ㅕ",
    "ㅖ",
    "ㅗ",
    "ㅘ",
    "ㅙ",
    "ㅚ",
    "ㅛ",
    "ㅜ",
    "ㅝ",
    "ㅞ",
    "ㅟ",
    "ㅠ",
    "ㅡ",
    "ㅢ",
    "ㅣ",
]
종성 = [
    "",
    "ㄱ",
    "ㄲ",
    "ㄳ",
    "ㄴ",
    "ㄵ",
    "ㄶ",
    "ㄷ",
    "ㄹ",
    "ㄺ",
    "ㄻ",
    "ㄼ",
    "ㄽ",
    "ㄾ",
    "ㄿ",
    "ㅀ",
    "ㅁ",
    "ㅂ",
    "ㅄ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

langset = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "ä",
    "ö",
    "ü",
    "ß",
]

targetarr = [
    "fs",
    "sy",
    "yd",
    "wj",
    "qz",
    "wn",
    "ßk",
    "fm",
    "mp",
    "lg",
    "hk",
    "jh",
    "jz",
    "zr",
    "tg",
    "äf",
    "fd",
    "bc",
    "cw",
    "wb",
    "bz",
    "zk",
    "kt",
    "tc",
    "pg",
    "vl",
    "mk",
    "tk",
    "kj",
    "mj",
    "jk",
    "np",
    "yn",
    "pj",
    "fj",
    "yt",
    "tv",
    "ct",
    "tj",
    "jp",
    "qd",
    "sr",
    "rw",
    "qk",
    "kh",
    "ap",
    "ev",
    "gz",
    "mn",
    "nn",
    "ßb",
    "lb",
    "rg",
    "yj",
    "jt",
    "ck",
    "jn",
    "tß",
    "yi",
    "jl",
    "jq",
    "pf",
    "ft",
    "jc",
    "cg",
    "cß",
    "ßc",
    "rß",
    "dw",
    "wq",
    "kß",
    "gc",
    "gs",
    "zn",
    "yw",
    "wc",
    "lv",
    "vc",
    "qb",
    "vn",
    "lp",
    "pm",
    "ml",
    "ßn",
    "bq",
    "qc",
    "rz",
    "ßz",
    "xj",
    "pk",
    "kc",
    "ww",
    "sw",
    "yp",
    "vr",
    "bg",
    "kl",
    "lc",
    "sl",
    "xr",
    "rq",
    "yk",
    "lf",
    "qf",
    "ßs",
    "gj",
    "kf",
    "oo",
    "tx",
    "cm",
    "bld",
    "zt",
    "kp",
    "fh",
    "rl",
    "bj",
    "jg",
    "sg",
    "lw",
    "js",
    "ys",
    "vm",
    "gm",
    "mq",
    "uq",
    "pv",
    "vk",
    "kv",
    "yy",
    "rk",
    "sn",
    "fn",
    "ss",
    "zc",
    "cv",
    "zs",
    "st",
    "sz",
    "fz",
]

resarr = [
    "fes",
    "söy",
    "ya",
    "woj",
    "qäz",
    "won",
    "ßak",
    "fam",
    "mop",
    "log",
    "häk",
    "jah",
    "joz",
    "zor",
    "tag",
    "äof",
    "fad",
    "boc",
    "caw",
    "wab",
    "biz",
    "zek",
    "ket",
    "toc",
    "pag",
    "vil",
    "mak",
    "tok",
    "koj",
    "mäj",
    "jak",
    "nop",
    "yin",
    "paj",
    "faij",
    "yit",
    "tav",
    "cot",
    "tij",
    "jip",
    "qod",
    "sir",
    "raw",
    "qök",
    "koh",
    "aop",
    "eov",
    "gaz",
    "mon",
    "non",
    "ßab",
    "lob",
    "rag",
    "yoj",
    "jit",
    "cok",
    "jin",
    "taß",
    "yoi",
    "jil",
    "jaq",
    "paf",
    "fit",
    "jac",
    "cog",
    "ceß",
    "ßoc",
    "riß",
    "daw",
    "waq",
    "kiß",
    "gic",
    "gas",
    "zon",
    "yow",
    "wic",
    "liv",
    "voc",
    "qob",
    "von",
    "lap",
    "pom",
    "mal",
    "ßon",
    "boq",
    "qoc",
    "roz",
    "ßoz",
    "xoj",
    "pak",
    "kac",
    "wow",
    "siw",
    "yop",
    "vur",
    "bag",
    "kol",
    "lic",
    "sol",
    "xor",
    "röq",
    "yak",
    "laf",
    "qaf",
    "ßos",
    "goj",
    "kaf",
    "oso",
    "tox",
    "com",
    "bald",
    "zet",
    "kap",
    "foh",
    "rel",
    "boj",
    "jig",
    "sig",
    "law",
    "jis",
    "yas",
    "vom",
    "gom",
    "miq",
    "uaq",
    "pov",
    "vik",
    "kov",
    "yay",
    "rok",
    "son",
    "fyn",
    "sis",
    "zoc",
    "civ",
    "zäs",
    "sit",
    "soz",
    "foz",
]

exclang = [" ", ".", "?", "!", "~", '"', ","]


def extrarule(content: str):
    for i in range(len(targetarr)):
        content = content.replace(targetarr[i], resarr[i])
    return content


def jaso_seperate(글자):
    # 초성 ===> X
    # 중성 ===> Y
    # 종성 ===> Z

    재정렬 = ord(글자) - 0xAC00
    Z = 재정렬 % 28
    Y = (재정렬 // 28) % 21
    X = ((재정렬 // 28) // 21) % 19

    return [초성[X], 중성[Y], 종성[Z]]


with open("topaz_lang.json", "r", encoding="utf8") as f:
    contents = f.read()  # string 타입
    json_data = json.loads(contents)


def topazencoder(content: str):
    content = content.rstrip().lstrip().lower()
    content = list(content)
    returnlang = ""
    for i in content:
        if i in exclang:
            returnlang += i
        else:
            A = jaso_seperate(i)
            for j in A:
                returnlang += json_data[j]
    return extrarule(returnlang)


def topazdecoder(content: str):
    content = list(content)
    returnlang = ""
    larray = []
    for i in content:
        larray.append(i)
    # print(larray)
    larray_chunked = list_chunk(larray, 5)
    # print(larray_chunked)

    for i in larray_chunked:
        a = langset.index(i[0])
        b = langset.index(i[1])
        c = langset.index(i[2])
        d = langset.index(i[3])
        e = langset.index(i[4])
        returnlang += chr(
            a * len(langset) ** 4
            + b * len(langset) ** 3
            + c * len(langset) ** 2
            + d * len(langset)
            + e * 1
        )

    return returnlang


def ask():
    try:
        print("1: to topaz / 2: to original")
        a = input()
        if a == "1":
            print("input")
            b = input()
            print(topazencoder(b))
        else:
            print("input")
            b = input()
            print(topazdecoder(b))

        # print(translate(topazencoder(a)))
    except Exception as e:
        print(e)
    ask()


def translate(content):
    for i in range(len(targetarr)):
        content = content.replace(resarr[i], targetarr[i])
    return content


ask()
