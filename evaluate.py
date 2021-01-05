import os 
from convert import compile_T2B
# stackClass

T=0
F=0
allscore=0
countTestcase=0

list_task = os.listdir(os.getcwd()+r'/testcase')
# list_task = os.listdir(os.getcwd()+r'/testcaseTBT')

def evaluate(task) :
    global allscore ,countTestcase,T,F

    cwd =os.path.join(os.getcwd()+r'/testcase',task)
    # cwd =os.path.join(os.getcwd()+r'/testcaseTBT',task)

    f = open(cwd,"r",encoding="utf8")

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
    
        result = compile_T2B(data[i], 0)
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
                grader+='-'
        else :
            F+=1
            grader+='x'

    allscore+=score
    score=score/alldata*100
    print("score of "+task +" = " +str(score))
    # print(grader)
                



# complie(list_task[7])
for i in list_task :
    evaluate(i)
print("Similar : ",allscore/countTestcase*100)
# print("cntTest :",countTestcase)
print("T :"+str(T) +" F : "+str(F))
