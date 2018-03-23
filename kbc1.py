def use_lifeline(lifeline_count,list1,list,no_of_question):
    if lifeline_count==1:
        print("You have selected audience poll\nThe predictions by audience are:")
        list2=list1
        right=random.randint(45,60)
        wrong1=random.randint(10,20)
        wrong2=random.randint(0,10)
        wrong3=100-right-wrong1-wrong2
        print(str(list1[5]) + " : " + str(right) + "%")
        del list2[int(list1[6])]
        print(str(list2[1]) + " : " + str(wrong1) + "%")
        print(str(list2[2]) + " : " + str(wrong2) + "%")
        print(str(list2[3]) + " : " + str(wrong3) + "%")
        return no_of_question
        
    if lifeline_count==2:
        print("You have selected phone a friend lifeline\nCalling...")
        print("You have 30 sec,your time starts now..")
        for i in range(30,0,-1):
            sys.stdout.write("\r"+str(i))
            time.sleep(1)
        probablity=random.randint(1,4)
        print("probablit is : "+str(probablity))
        if probablity is 1 or probablity is 2 or probablity is 3:
             print("THE ANSWER IS : "+list[0][5])
        return no_of_question
    
    if lifeline_count is 3:
        print("The question has been changed\nThe new question is : ")
        no_of_question
        return no_of_question


import random
import mysql.connector
import time
import sys
conn=mysql.connector.connect(user='root',password='12345678',host='localhost',database='kbc')
mycursor=conn.cursor()
print ("KAUN BANEGA CROREPATI")
print("1->5000\n2->10000\n3->20000\n4->40000\n5->80000\n6->160000\n7->320000\n8->640000\n9->12500000")
print("10->2500000\n11->5000000\n12->10000000\n13->70000000")
print ("FORMATTING QUESTIONS....")
qstn_asked=[]
not_out=True
no_of_question=5
lifeline_count=0
while not_out:
    if (len(qstn_asked))==no_of_question:
        print("You have won the game")
        break
    x=random.randint(1,5)
    if x not in qstn_asked:
        qstn_asked.append(x)
        print("x is : "+str(x))
        mycursor.execute("select question,optionA,optionB,optionC,optionD,answer,option_number from qna where id="+str(x))
        list=mycursor.fetchall()
        list1=[]
        for x in list:
            for y in x:
                #print(y)
                list1.append(y)
        time.sleep(1)
        print("Question : "+list[0][0])
        print("Option A : "+list[0][1])
        print("Option B : "+list[0][2])
        print("Option C : "+list[0][3])
        print("Option D : "+list[0][4])
        time.sleep(5)
        probablity=random.randint(1,4)
        print("probablit is : "+str(probablity))
        if probablity is 1 or probablity is 2 or probablity is 3:
             print("THE ANSWER IS : "+list[0][5])
        elif lifeline_count>=3:
            not_out=False
            print("YOU HAVE LOSED THE GAME")
            break
        else:
            lifeline_count+=1
            print("Lifeline used")
            no_of_question=use_lifeline(lifeline_count,list1,list,no_of_question)
