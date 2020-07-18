import os 
from processASCII import T2B,_number
# from process import T2B,_number
from word_tokenizer import word_sylleble
# stackClass

T=0
F=0
twopayang=0
allscore=0
countTestcase=0

# list_task = os.listdir(os.getcwd()+r'/testcase')
list_task = os.listdir(os.getcwd()+r'/testcaseTBT')
def complie(task) :
    # cwd =os.path.join(os.getcwd()+r'/testcase',task)
    cwd =os.path.join(os.getcwd()+r'/testcaseTBT',task)
    f = open(cwd,"r",encoding="utf8")
    global allscore ,countTestcase,T,F,twopayang
    #แยกบรรทัด -1 ตัด enter
    data= []
    for i in f :
        data.append(i[:-1])

    #จำนวน testcase 
    alldata = len(data)/2
    countTestcase+=alldata
    #display score
    score = 0
    grader = ''

    
    quote=1
    number=''
    for i in range(0,len(data),2) :
        text =word_sylleble(data[i])[0]
        debug=word_sylleble(data[i])[1]

        # print(text)
        result = ''
        if len(text) > 2 :
            # print(text)
            twopayang+=1

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
                result += T2B(number,len(text),quote)
                number=''
            result += T2B(j,len(text),quote)
            # print("not same:\n%"+result+"%"+'\n'+"%"+data[i+1]+"%")

        
        if number!='' :
            result += T2B(number,len(text),quote)
            number=''

        # print(data[i] +"฿"+result+'฿'+result)
        if(i+1<len(data) and len(result)==len(data[i+1])) :
            notsame=0
            for j in range(len(result)) :
                if result[j]!=data[i+1][j] :
                    notsame=1
                    break
            if notsame==0 :
                grader+='P' # grader
                score+=1
                T+=1
            elif notsame == 1 :
                F+=1
                # print(debug)
                # print(text)
                # print(data[i] +" "+result+' '+data[i+1])
                # print("not same:\n"+result+""+'\n'+""+data[i+1]+"")
                grader+='-'
        else :
            # print(debug)
            # print(text)
            # print(data[i] +" "+result+' '+data[i+1])
            # print("fail x : \n"+result+""+'\n'+""+data[i+1]+"")
            F+=1
            grader+='x'

    allscore+=score
    score=score/alldata*100
    print("score of "+task +" = " +str(score))
    print(grader)
                



# complie(list_task[7])
for i in list_task :
    complie(i)
print("Similar : ",allscore/countTestcase*100)
# print("cntTest :",countTestcase)
print("T :"+str(T) +" F : "+str(F))
# print("Twopayang :"+str(twopayang) )