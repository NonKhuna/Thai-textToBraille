import stackClass
from encode.braille2ASCII import B2ASCII as c2Braile


stack = stackClass.stack()

_frontVerb=['เ','แ','ไ','ใ','โ']
_char = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ล', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ','ฤ','ฦ','ญ']
_top = ['่','้','๊','๋','็']
_number=["0","1","2","3","4","5","6","7","8",'๑','๒','๓','๔','๕','๖','๗','๘','๙','๐']
_numthai=['๑','๒','๓','๔','๕','๖','๗','๘','๙','๐']

def T2CB(text,numSylleble,quote) :
    stateNumber=0
    result = ''

    if text == 'ฯลฯ' :
        return ";l"
    if text == "..." :
        return ",,,"

    for index in range(len(text)) :
        ch = text[index]
        
        #number
        if (ch in _number) or (ch in ['.',',','-','/'] and stateNumber==1):
            if stateNumber==0 :
                if ch in _numthai :
                    result += '6|'
                result+='3456|'
                stateNumber=1
            result+=c2Braile(ch)
            # print(ch)
            continue
        else :
            stateNumber=0
        
        # ()
        if ch == '('  :
            stack.alphaIn.append(ch)
            continue
        elif ch == ')' :
            stack.alphaFi.append(ch)
            continue

        #ฯ
        if ch == 'ฯ' :
            result+=c2Braile(ch)
            continue

        #quote ""
        if ch =='"' :
            if quote ==0 :
                result+=c2Braile('"1')
            else :
                result+=c2Braile('"2')
            continue

        # , 
        if ch == ',' and stateNumber==0 :
            result+=c2Braile(',,')
            continue
        
        #space
        if ch == ' ' :
            result+=c2Braile(ch)
            continue

        #dot   
        if ch == '.' : #end
            if numSylleble>2:
                stack.alphaFi.append('..')
            else :
                stack.alphaFi.append('.')
            result+=clearStack(text)
            continue

        #alpha
        if ch in _char :
            if stack.isalphaFi :
                if stack.verb=='ั' and ch == 'ว':
                    changeV("!12")
                elif ch=='อ' and stack.haveFrontVerb and stack.verb=='$2':
                    changeV("!10")
                elif ch=='อ' and stack.haveFrontVerb and  stack.verb == 'เ':  # เออ
                    if index+1 < len(text) and text[index+1] in _char or len(stack.alphaIn)==0:
                        stack.alphaIn.append(ch)
                    elif len(stack.alphaIn)>0:
                        changeV("!6")
                elif ch=='ย' and stack.haveFrontVerb and stack.verb=='$1':
                    changeV("!8")
                else :
                    stack.alphaFi.append(ch)

            elif ch=='อ' and stack.haveFrontVerb and  stack.verb == 'เ':  # เออ
                if (index+1 < len(text) and ( text[index+1] in _char or text[index+1]=='ิ' )) or len(stack.alphaIn)==0:
                    stack.alphaIn.append(ch)
                elif len(stack.alphaIn)>0:
                    changeV("!6")
            else :
                stack.alphaIn.append(ch)
        elif ch == '์' :
            if text[index-1] in ['ิ','ุ'] :
                stack.alphaFi.append(text[index-1])
                stack.verb=''
            stack.alphaFi.append(ch)

            
        elif ch in _top :
            stack.top.append(ch)
            stack.isalphaFi=1
        else  :
            if ch in _frontVerb :
                result+=clearStack(text)
                stack.verb=ch
                stack.haveFrontVerb=1;
            else :
                if ch == 'ะ' and stack.verb!='' :
                    if stack.verb=='!12' :
                        changeV("!11")
                    if stack.verb=='เ' :
                        changeV("!1")
                    if stack.verb=='แ' :
                        changeV("!2")
                    if stack.verb=='โ' :
                        changeV("!3")
                    if stack.verb=='!6' :
                        changeV("!5")
                    if stack.verb=='!13' :
                        changeV("!4")
                    if stack.verb=='!8' :
                        changeV("!7")
                    result+=clearStack(text)

                elif ch=='า' and stack.haveFrontVerb :
                    if stack.verb=='เ' :
                        changeV("!13")
                elif ch=='ิ' and stack.haveFrontVerb :
                    if stack.verb=='เ' :
                        changeV("!6")
                        stack.isalphaFi=1

                elif ch=='ี' and stack.haveFrontVerb :
                    if stack.verb=='เ' :
                        changeV("$1")
                        stack.isalphaFi=1

                elif ch=='ื' and stack.haveFrontVerb :
                    if stack.verb=='เ' :
                        changeV("$2")
                        stack.isalphaFi=1

                elif ch=='ุ' and stack.haveFrontVerb : #เหตุ
                    if stack.verb=='เ' :
                        stack.alphaFi.append(ch)

                elif stack.haveFrontVerb == 0 :
                    if len(stack.verb)!=0 and stack.verb =='า' : #ชาติ
                        stack.alphaFi.append(ch)
                        continue 
                    stack.verb=ch
                    stack.isalphaFi=1
                    # print()
    
    # stack.show()
    result+=clearStack(text)
    return result

def clearStack(text) :
    result = ''
    if stack.haveFrontVerb :
        if  stack.verb in _frontVerb:
            result+=c2Braile(stack.verb)
            result+=addAlphaIn()
            result+=addTop()
            result+=addAlphaFi()
        else :
            result+=topAfterVerb()
    else :
        #สระกลุ่มที่อยู่ตรงกลาง
        #สระ า (อ,ว) จะอยู่ในรูปของ alphaFi หรือ alphaIn
        if stack.verb==''  or  stack.verb in ['า'] :
            result+=topBeforeVerb()
        else :
            result+=topAfterVerb()
        
    stack.reset()
    return result

def topBeforeVerb():
    result=addAlphaIn()
    result+=addTop()
    result+=addVerb()
    result+=addAlphaFi()
    return result

def topAfterVerb():
    result=addAlphaIn()
    result+=addVerb()
    result+=addTop()
    result+=addAlphaFi()
    return result

def addAlphaFi() :
    txt=''
    for i in stack.alphaFi :
        txt += c2Braile(i) 
    return txt

def addTop() :
    txt=''
    for i in stack.top :
        txt += c2Braile(i) 
    return txt 

def addAlphaIn() :
    txt = ''
    for i in stack.alphaIn :
        txt += c2Braile(i) 
    return txt
    
def addVerb() :
    if stack.verb!='' :
        return c2Braile(stack.verb)
    else :
        return ''

def changeV(text) :
    stack.verb=text