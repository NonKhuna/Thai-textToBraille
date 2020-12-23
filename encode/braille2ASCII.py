def B2ASCII(ch) :
    ############พญัชนะ##########################
    if ch=='ก' :
        return "g"
    if ch=='ข' :
        return "k"
    if ch=='ฃ' :
        return "0k"
    if ch=='ค' :
        return "u"
    if ch=='ฆ' :
        return ",u"
    if ch=='ฅ' :
        return "-u"
    if ch=='ง' :
        return "}" #same ]
    if ch=='จ' :
        return "j"
    if ch=='ฉ' :
        return "/"
    if ch=='ช' :
        return "+"
    if ch=='ฌ' :
        return ",+"
    if ch=='ซ' :
        return "!"
    if ch=='ด' :
        return "d"
    if ch=='ฎ' :
        return ",d"
    if ch=='ต' :
        return "|"
    if ch=='ฏ' :
        return ",\\"
    if ch=='ถ' :
        return "t"
    if ch=='ฐ' :
        return ",t"
    if ch=='ท' :
        return ")"
    if ch=='ฑ' :
        return ",)"
    if ch=='ฒ' :
        return "-)"
    if ch=='ธ' :
        return "0)"
    if ch=='น' :
        return "n"
    if ch=='ณ' :
        return ",n"
    if ch=='บ' :
        return "v"
    if ch=='ป' :
        return "&"
    if ch=='ผ' :
        return "p"
    if ch=='ฝ' :
        return "x"
    if ch=='พ' :
        return "?"
    if ch=='ภ' :
        return ",?"
    if ch=='ฟ' :
        return "$"
    if ch=='ม' :
        return "m"
    if ch=='ย' :
        return "y"
    if ch=='ญ' :
        return ",y"
    if ch=='ร' :
        return "r"
    if ch=='ล' :
        return "l"
    if ch=='ฬ' :
        return ",l"
    if ch=='ว' :
        return "w"
    if ch=='ส' :
        return "s"
    if ch=='ศ' :
        return ",s"
    if ch=='ษ' :
        return "-s"
    if ch=='ห' :
        return "h"
    if ch=='อ' :
        return "o"
    if ch=='ฮ' :
        return "="


    #########################สระ##############################################
    if ch=='ะ' :
        return "a"
    if ch=='า' :
        return "*"
    if ch=='ิ' :
        return "b"
    if ch=='ี' :
        return "2"
    if ch=='ึ' :
        return "{" #same [
    if ch=='ื' :
        return "5"
    if ch=='ุ' :
        return "c"
    if ch=='ู' :
        return "3"
    if ch=='เ' : 
        return "f"
    if ch=='แ' : 
        return "<"
    if ch=='โ' : 
        return "i"
    if ch=='ำ' : 
        return "z"
    if ch=='ไ' : 
        return ":"
    if ch=='ใ' : 
        return ":1"
    if ch=='ฤ' : 
        return "r1"
    if ch=='ๅ' : 
        return "*"
    if ch=='ฦ' : 
        return "l1"
    ###สระประสม
    if ch=='!1' : #เอะ
        return "fa"
    if ch=='!2' : #แอะ
        return "<a"
    if ch=='!3' : #โอะ
        return "ia"
    if ch=='!4' :  #เอาะ
        return "oa"
    if ch=='!5' :  #เออะ
        return "%a"
    if ch=='!6' : #เออ
        return "%"
    if ch=='!7' : #เอียะ 
        return "(a"
    if ch=='!8' : #เอีย 
        return "("
    if ch=='!9' : #เอือะ 
        return "qa"
    if ch=='!10' : #เอือ 
        return "q"
    if ch=='!11' :  #อัวะ
        return "ea"
    if ch=='!12' :  #อัว
        return "e"
    if ch=='!13' : #เอา 
        return "6"

    ### top word ##################################
    if ch=='่' :
        return "9"
    if ch=='้' :
        return "4"
    if ch=='๊' :
        return "7"
    if ch=='๋' :
        return "8"
    if ch=='ั' :
        return ">"
    if ch=='์' :
        return "0"
    if ch=='ๆ' :
        return "1"
    if ch=='็' :
        return "'"

    #number --------------------------------------------------
    #standard braile thai ถ้า เลขไทย จะขึ้นต้นด้วย จุด 6 แล้วตามด้วย จุด 3456
    if ch == '๐' or ch== '0' :
        return "j"
    if ch == '๑' or ch== '1' :
        return "a"
    if ch == '๒' or ch== '2' :
        return "b"
    if ch == '๓' or ch== '3' :
        return "c"
    if ch == '๔' or ch== '4' :
        return "d"
    if ch == '๕' or ch== '5' :
        return "e"
    if ch == '๖' or ch== '6' :
        return "f"
    if ch == '๗' or ch== '7' :
        return "g"
    if ch == '๘' or ch== '8' :
        return "h"
    if ch == '๙' or ch== '9' :
        return "i"
    

    if ch=='.' :
        return "4"
    if ch=='..' :
        return "_4"
    if ch==',' :
        return "1"
    if ch==',,' :
        return "_4"
    if ch==' ' :
        return " "
    if ch=='?' :
        return "_8"
    if ch=='!' :
        return "_6"
    if ch=='ฯ' :
        return ";2"
    if ch=='-' :
        return "-"
    if ch=='=' :
        return "33"
    if ch=='+' :
        return "346"
    if ch==';' :
        return "_2"
    if ch==':' :
        return "3"
    if ch=='/' :
        return "_/"

    if ch=='(' or ch ==')' :
        return "7"
    if ch=='"1' :
        return "8"
    if ch=='"2' :
        return "0"
    
    