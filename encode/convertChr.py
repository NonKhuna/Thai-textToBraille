
def charToBraile(ch) :

    ############พญัชนะ##########################
    if ch=='ก' :
        return "1245"
    if ch=='ข' :
        return "13"
    if ch=='ฃ' :
        return "356|13"
    if ch=='ค' :
        return "136"
    if ch=='ฆ' :
        return "6|136"
    if ch=='ฅ' :
        return "36|136"
    if ch=='ง' :
        return "12456"
    if ch=='จ' :
        return "245"
    if ch=='ฉ' :
        return "34"
    if ch=='ช' :
        return "346"
    if ch=='ฌ' :
        return "6|346"
    if ch=='ซ' :
        return "2346"
    if ch=='ด' :
        return "145"
    if ch=='ฎ' :
        return "6|145"
    if ch=='ต' :
        return "1256"
    if ch=='ฏ' :
        return "6|1256"
    if ch=='ถ' :
        return "2345"
    if ch=='ฐ' :
        return "6|2345"
    if ch=='ท' :
        return "23456"
    if ch=='ฑ' :
        return "6|23456"
    if ch=='ฒ' :
        return "36|23456"
    if ch=='ธ' :
        return "356|23456"
    if ch=='น' :
        return "1345"
    if ch=='ณ' :
        return "6|1345"
    if ch=='บ' :
        return "1236"
    if ch=='ป' :
        return "12346"
    if ch=='ผ' :
        return "1234"
    if ch=='ฝ' :
        return "1346"
    if ch=='พ' :
        return "1456"
    if ch=='ภ' :
        return "6|1456"
    if ch=='ฟ' :
        return "1246"
    if ch=='ม' :
        return "134"
    if ch=='ย' :
        return "13456"
    if ch=='ญ' :
        return "6|13456"
    if ch=='ร' :
        return "1235"
    if ch=='ล' :
        return "123"
    if ch=='ฬ' :
        return "6|123"
    if ch=='ว' :
        return "2456"
    if ch=='ส' :
        return "234"
    if ch=='ศ' :
        return "6|234"
    if ch=='ษ' :
        return "36|234"
    if ch=='ห' :
        return "125"
    if ch=='อ' :
        return "135"
    if ch=='ฮ' :
        return "123456"


    #########################สระ##############################################
    if ch=='ะ' :
        return "1"
    if ch=='า' :
        return "16"
    if ch=='ิ' :
        return "12"
    if ch=='ี' :
        return "23"
    if ch=='ึ' :
        return "246"
    if ch=='ื' :
        return "26"
    if ch=='ุ' :
        return "14"
    if ch=='ู' :
        return "25"
    if ch=='เ' : 
        return "124"
    if ch=='แ' : 
        return "126"
    if ch=='โ' : 
        return "24"
    if ch=='ำ' : 
        return "1356"
    if ch=='ไ' : 
        return "156"
    if ch=='ใ' : 
        return "156|2"
    if ch=='ฤ' : 
        return "1235|2"
    if ch=='ๅ' : 
        return "16"
    if ch=='ฦ' : 
        return "123|2"
    ###สระประสม
    if ch=='!1' : #เอะ
        return "124|1"
    if ch=='!2' : #แอะ
        return "126|1"
    if ch=='!3' : #โอะ
        return "24|1"
    if ch=='!4' :  #เอาะ
        return "135|1"
    if ch=='!5' :  #เออะ
        return "146|1"
    if ch=='!6' : #เออ
        return "146"
    if ch=='!7' : #เอียะ 
        return "12356|1"
    if ch=='!8' : #เอีย 
        return "12356"
    if ch=='!9' : #เอือะ 
        return "12345|1"
    if ch=='!10' : #เอือ 
        return "12345"
    if ch=='!11' :  #อัวะ
        return "15|1"
    if ch=='!12' :  #อัว
        return "15"
    if ch=='!13' : #เอา 
        return "235"

    ### top word ##################################
    if ch=='่' :
        return "35"
    if ch=='้' :
        return "256"
    if ch=='๊' :
        return "2356"
    if ch=='๋' :
        return "236"
    if ch=='ั' :
        return "345"
    if ch=='์' :
        return "356"
    if ch=='ๆ' :
        return "2"
    if ch=='็' :
        return "3"

    #number --------------------------------------------------
    #standard braile thai ถ้า เลขไทย จะขึ้นต้นด้วย จุด 6 แล้วตามด้วย จุด 3456
    if ch == '๐' or ch== '0' :
        return "245"
    if ch == '๑' or ch== '1' :
        return "1"
    if ch == '๒' or ch== '2' :
        return "12"
    if ch == '๓' or ch== '3' :
        return "14"
    if ch == '๔' or ch== '4' :
        return "145"
    if ch == '๕' or ch== '5' :
        return "15"
    if ch == '๖' or ch== '6' :
        return "124"
    if ch == '๗' or ch== '7' :
        return "1245"
    if ch == '๘' or ch== '8' :
        return "125"
    if ch == '๙' or ch== '9' :
        return "24"
    

    if ch=='.' :
        return "256"
    if ch=='..' :
        return "456|256"
    if ch==',' :
        return "3"
    if ch==',,' :
        return "456|2"
    if ch==' ' :
        return " "
    if ch=='?' :
        return "456|236"
    if ch=='!' :
        return "456|235"
    if ch=='ฯ' :
        return "56|23"
    if ch=='-' :
        return "36"
    if ch=='=' :
        return "56|2356"
    if ch=='+' :
        return "346"
    if ch==';' :
        return "456|23"
    if ch==':' :
        return "456|25"
    if ch=='/' :
        return "456|34"

    if ch=='(' or ch ==')' :
        return "2356"
    if ch=='"1' :
        return "236"
    if ch=='"2' :
        return "356"
    
    