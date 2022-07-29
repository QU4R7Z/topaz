import hashlib
import re

langset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß', 'ю', 'ф', 'д', 'б', 'ж', 'и', 'ꙗ', 'ѱ', 'ъ', 'ы', 'щ', 'г', 'ч', 'ц',
           'ѡ', 'к', 'л', 'н', 'є']
print(len(langset), 1114112 / len(langset))
print(len(langset), len(set(langset)))

targetarr = ['fs', 'sy', 'yd', 'wj', 'qz', 'wn', 'ßk', 'fm', 'mp', 'lg', 'hk', 'jh', 'jz', 'zr', 'tg', 'äf', 'fd',
             'bc', 'cw', 'wb', 'bz', 'zk', 'kt', 'tc', 'pg', 'vl', 'mk', 'tk', 'kj', 'mj', 'jk', 'np', 'yn', 'pj',
             'fj', 'yt', 'tv', 'ct', 'tj', 'jp', 'qd', 'sr', 'rw', 'qk', 'kh', 'ap', 'ev', 'gz', 'mn', 'nn', 'ßb',
             'lb', 'rg', 'yj', 'jt', 'ck', 'jn', 'tß', 'yi', 'jl', 'jq', 'pf', 'ft', 'jc', 'cg', 'cß', 'ßc', 'rß',
             'dw', 'wq', 'kß', 'gc', 'gs', 'zn', 'yw', 'wc', 'lv', 'vc', 'qb', 'vn', 'lp', 'pm', 'ml', 'ßn', 'bq',
             'qc', 'rz', 'ßz', 'xj', 'pk', 'kc', 'ww', 'sw', 'yp', 'vr', 'bg', 'kl', 'lc', 'sl', 'xr', 'rq', 'yk',
             'lf', 'qf', 'ßs', 'gj', 'kf', 'oo', 'tx', 'cm', 'bld', 'zt', 'kp', 'fh', 'rl', 'bj', 'jg', 'sg', 'lw',
             'js', 'ys', 'vm', 'gm', 'mq', 'uq', 'pv', 'vk', 'kv', 'yy', 'rk']

resarr = ['fes', 'söy', 'ya', 'woj', 'qäz', 'won', 'ßak', 'fam', 'mop', 'log', 'häk', 'jah', 'joz', 'zor', 'tag',
          'äof', 'fad', 'boc', 'caw', 'wab', 'biz', 'zek', 'ket', 'toc', 'pag', 'vil', 'mak', 'tok', 'koj', 'mäj',
          'jak', 'nop', 'yin', 'paj', 'faij', 'yit', 'tav', 'cot', 'tij', 'jip', 'qod', 'sir', 'raw', 'qök', 'koh',
          'aop', 'eov', 'gaz', 'mon', 'non', 'ßab', 'lob', 'rag', 'yoj', 'jit', 'cok', 'jin', 'taß', 'yoi', 'jil',
          'jaq', 'paf', 'fit', 'jac', 'cog', 'ceß', 'ßoc', 'riß', 'daw', 'waq', 'kiß', 'gic', 'gas', 'zon', 'yow',
          'wic', 'liv', 'voc', 'qob', 'von', 'lap', 'pom', 'mal', 'ßon', 'boq', 'qoc', 'roz', 'ßoz', 'xoj', 'pak',
          'kac', 'wow', 'siw', 'yop', 'vur', 'bag', 'kol', 'lic', 'sol', 'xor', 'röq', 'yak', 'laf', 'qaf', 'ßos',
          'goj', 'kaf', 'oso', 'tox', 'com', 'bald', 'zet', 'kap', 'foh', 'rel', 'boj', 'jig', 'sig', 'law', 'jis',
          'yas', 'vom', 'gom', 'miq', 'uaq', 'pov', 'vik', 'kov', 'yay', 'rok']

exclang = [' ', '.', '?', '!', '~', '"', ',']

ascii_exclang = [ord(i) for i in exclang]


def extrarule(content: str):
    """
    for i in range(len(targetarr)):
        content = content.replace(targetarr[i], resarr[i])
    """
    return content


def convert_iter(num, base):
    tmp = ''
    while num:
        tmp = '{:02d}'.format(num % base) + tmp
        num //= base

    return '{:010d}'.format(int(tmp))


def list_chunk(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def topazencoder(content: str):
    content = content.rstrip().lstrip().lower()
    content = list(content)
    returnlang = ""
    for i in content:
        if i in exclang:
            returnlang += i
        else:
            print(ord(i))
            r = list(convert_iter(int(ord(i)), len(langset)))
            f = int(r[0] + r[1])
            b = int(r[2] + r[3])
            d = int(r[4] + r[5])
            e = int(r[6] + r[7])
            k = int(r[8] + r[9])
            print(f, b, d, e, k)

            returnlang += langset[f] + langset[b] + langset[d] + langset[e] + langset[k]
    return extrarule(returnlang)


def topazdecoder(content: str):
    content = list(content)
    returnlang = ""
    larray = []
    for i in content:
        if i in exclang:
            returnlang += i
        else:
            larray.append(i)
    print(larray)
    larray_chunked = list_chunk(larray, 5)
    print(larray_chunked)
    for i in larray_chunked:
        a = langset.index(i[0])
        b = langset.index(i[1])
        c = langset.index(i[2])
        d = langset.index(i[3])
        e = langset.index(i[4])
        returnlang += chr(
            a * len(langset) ** 4 + b * len(langset) ** 3 + c * len(langset) ** 2 + d * len(langset) + e * 1)

    return returnlang


def ask():
    print("input")
    a = input()
    print(topazencoder(a))
    # print(translate(topazencoder(a)))
    ask()


def translate(content):
    for i in range(len(targetarr)):
        content = content.replace(resarr[i], targetarr[i])
    return content


print(topazencoder("안녕"))
print(topazdecoder("aavbжaasѡx"))
