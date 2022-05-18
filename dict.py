#crating a binary file with initail dictionary
import pickle
dict_2={}
bf_1=open ('game.dat','wb')
pickle.dump(dict_2,bf_1)
bf_1.close()

#input of the answer from the user
import pickle           
import os
def create(userinput):
    lst=[]
    answer={}
    with open(userinput,'ab+') as f:
        a = 'y'
        while a == 'y':
            x=input("enter your name")
            l=input("enter your answer")
            answer[x]=l
            pickle.dump(answer,f)
            a = input("Continue?(y/n)")
    dict_2=answer       
    f.close()

#printing the dict entered by user
import pickle
import os
def disp(userinput):
    if not os.path.isfile(userinput):
        print ("file does not exists")
    else:
        f=open(userinput,'rb')
    sd={}   
    while True:
              try:    
               sd=pickle.load(f)
              except EOFError:
                 break
    print(sd)            
    
    f.close()

#Appending the values
import pickle           
import os
def append(userinput):
    with open("answer.dat",'ab+') as f:
        answer = dict_2
        a = 'y'
        while a == 'y':
            x=input("enter your name")
            l=input("enter your answer")
            answer[x]=l
            pickle.dump(answer,f)
            a = input("Continue?(y/n)")
    dict_2.update(answer)       
    f.close()

#Deleting Record

op = 'y'
while op == 'y':
        print('''
        1)Enter Record
        2)Display Records
        3)Modify Record
        4)Delete Record
        5)Find Record
        6)Close Notebook
                                            ''')
        option = int(input("Enter Option"))
        if option==1:
            append("answer.dat")
            print('OBSERVATION RECORDED')
        elif option==2:
            disp("answer.dat")
        elif option == 6:
            op = 'n'
        


'''
#checking the values (dict_1 already exists, only check for dict_2 in bf_2)

import pickle
import os
if not os.path.isfile('answer.dat'):
    print ("file does not exists")
else:
    bf_2=open('answer.dat','rb')
    display_dict={}   
while True:
    try:    
       display_dict=pickle.load(bf_2)
    except EOFError:
       break
              
    compare_1 = dict_2.values()
    #print (compare_1)
    compare_2 = display_dict.values()
    #print (compare_2)



    compare_1_as_set = set(compare_1)
    intersection = compare_1_as_set.intersection(compare_2)
    #Find common elements of set and list

    intersection_as_list = list(intersection)

    print("the matched value from the original dictionary:-",intersection_as_list)
bf_2.close()    
    
#deleting all the values that the user input from the bf_2  

import pickle

bf_2 = open('answer.dat','r+')
bf_2.seek(0)
bf_2.truncate()

bf_2.close()

'''













