from pythainlp.tokenize import Tokenizer,word_tokenize,dict_trie
from pythainlp.corpus.common import thai_words,thai_syllables

import re
from TCC import tcc_pos
from collections import defaultdict
from heapq import heappush, heappop


pat_eng = re.compile(r'''(?x)
[-a-zA-Z]+|   # english
\d[\d,\.]*|   # number
[ \t]+|       # space
\r?\n         # newline
''')



PATH_TO_CUSTOM_Sylleble = './custom_sylleble.txt'
listtext=open(PATH_TO_CUSTOM_Sylleble,'r',encoding="utf8").read().split('\n')

def serialize(words_at, p, p2):   
  # find path ทั้งหมด แบบ depth first
  if p in words_at:
    for w in words_at[p]:
      p_ = p + len(w)
      if p_== p2:
        yield [w]
      elif p_ < p2:
        for path in serialize(words_at, p_, p2):
          yield [w]+path

def onecut(trie,text):
  words_at = defaultdict(list)  # main data structure
  allow_pos = tcc_pos(text)     # ตำแหน่งที่ตัด ต้องตรงกับ tcc
  
  q = [0]       # min-heap queue
  last_p = 0    # last position for yield
  while q[0] < len(text):
      p = heappop(q)

      for w in trie.prefixes(text[p:]):
          p_ = p + len(w)
          if p_ in allow_pos:  # เลือกที่สอดคล้อง tcc
            words_at[p].append(w)
            if p_ not in q:
              heappush(q, p_)   

      # กรณี length 1 คือ ไม่กำกวมแล้ว ส่งผลลัพธ์ก่อนนี้คืนได้
      if len(q)==1:
          paths = serialize(words_at, last_p, q[0])
          for w in min(paths, key=len):
            yield w
          last_p = q[0]

      # กรณี length 0  คือ ไม่มีใน dict
      if len(q)==0:
          m = pat_eng.match(text[p:])
          if m: # อังกฤษ, เลข, ว่าง
              i = p + m.end()
          else: # skip น้อยที่สุด ที่เป็นไปได้
              for i in range(p+1, len(text)):
                  if i in allow_pos:   # ใช้ tcc ด้วย ทั้งจุดเริ่มและจบ
                      ww = [w for w in trie.prefixes(text[i:]) if (i+len(w) in allow_pos)]
                      m = pat_eng.match(text[i:])
                      if ww or m:
                          break
              else:
                  i = len(text)
          w = text[p:i]
          words_at[p].append(w)
          yield w
          last_p = i
          heappush(q, i)
          

def word_sylleble(text) :
    tokens=[]
    if text :
        trie = dict_trie(dict_source=listtext)
        tokens.extend(onecut(trie,text=text))
    return [tokens,text]

# print(word_sylleble("ผมไปเรียนหนังสือเสมอ"))


