from word_tokenizer import  word_sylleble
from pythainlp.tokenize import Tokenizer,word_tokenize,dict_trie
from processASCII import T2B,_number
# text = "แฟนสวยมาก"
# text = "กานดา"

# PATH_TO_CUSTOM_Sylleble = './custom_sylleble.txt'
# listtext=open(PATH_TO_CUSTOM_Sylleble,'r',encoding="utf8").read().split('\n')
# trie = dict_trie(dict_source=listtext)
# print(text[3:])
# print(trie.prefixes(text[3:]))

print(T2B("สือ",15,0))

# for i in text :
#   print(i)