import re

pat_tcc = """\
เc็c
เcctาะ
เccีtยะ
เccีtย(?=[เ-ไก-ฮ]|$)
เccอะ
เcc็c
เcิc์c
เcิtc
เcีtยะ?
เcืtอะ?
เc[ิีุู]tย(?=[เ-ไก-ฮ]|$)
เctา?ะ?
cัtวะ
c[ัื]tc[ุิะ]?
c[ิุู]์
c[ะ-ู]t
c็
ct[ะาำ]?
แc็c
แcc์
แctะ
แcc็c
แccc์
โctะ
[เ-ไ]ct
""".replace('c','[ก-ฮ]').replace('t', '[่-๋]?').split()

def tcc(w):
    p = 0
    pat = re.compile("|".join(pat_tcc))
    while p<len(w):
        m = pat.match(w[p:])
        if m:
            n = m.span()[1]
        else:
            n = 1
        yield w[p:p+n]
        p += n

def tcc_pos(text):
    p_set = set()
    p = 0
    for w in tcc(text):
        # print(w)
        # print(text[p:p+len(w)])
        p += len(w)
        p_set.add(p)
    return p_set
