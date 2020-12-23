from processASCII import T2CB,_number
from process import T2SB
from word_tokenizer import word_sylleble

# fs 0 ==> T2SB #default
# fs 1 ==> T2CB
def compile_T2B(text, fs=0) :
    quote=1
    number=''
    if text[-1] == '\n' :
        text = text[:-1]

    # Tokenize word
    text =word_sylleble(text)[0]

    result = ''

    for index in range(len(text)):
        j=text[index]
        if j=='#' :
            break
            
        if j == '"' :
            if quote==0 :
                quote=1
            else :
                quote=0
        
        if j in _number:
            number+=j
            continue
        else :
            stateNumber=0
            
        if j in ['.',',','-','/'] :
            if index-1 >= 0 and text[index-1] in _number:
                number+=j
                continue
                
        if number!='' :
            if fs :
                result += T2CB(number,len(text),quote)
            else :
                result += T2SB(number,len(text),quote)
            number=''
        if fs :
            result += T2CB(j, len(text),quote)
        else :
            result += T2SB(j, len(text),quote)

    
    if number!='' :
        if fs :
            result += T2CB(number,len(text),quote)
        else :
            result += T2SB(number,len(text),quote)
        number=''

    return result