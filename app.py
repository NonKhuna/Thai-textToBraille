import os 
from convert import compile_T2B
import sys

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = sys.argv[1:]

twopayang=0
result = ''

def to_raw(string):
    return string.replace("\\","\\\\")

# transform pattern
# 0 is t2s (text to spelling word)
# 1 is t2bc (text to braille comp code)
type_translate = 0
if "-m" in opts :
    idx = args.index("-m")
    type_translate = int(args[idx+1])

if "-p" in opts :
    idx_path = args.index("-p")
    path_name = to_raw(str(args[idx_path+1]))
    files = open(path_name, 'r' ,encoding="utf8")
    for i in files :
        result+= compile_T2B(i, type_translate) + '\n'
    print(result)

if "-t" in opts :
    idx_text = args.index("-t")
    data = str(args[idx_text+1])
    result = compile_T2B(data, type_translate)
    print(result)
    # file = open(a)

    

