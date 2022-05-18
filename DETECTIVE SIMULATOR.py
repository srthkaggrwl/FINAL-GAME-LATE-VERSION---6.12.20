                                                                      #modules imported

import csv
import os
import time

header = ['S.NO','Notebook Tags','Notebook Tag Name','Score']
#records = [['1','OBJECT1','clock',''],['2','OBJECT2','canvas',''],['3','OBJECT3','unfinishedpainting','']]
with open("score_board.csv",'w') as file:
    csv_w = csv.writer(file,lineterminator='\n')
    csv_w.writerow(header)
    #for i in range(len(records)):
      #csv_w.writerow(records[i])

                                                                       





                                                                            #NOTEBOOK

def NOTEBOOK():




 print('''
            1)Enter Record
            2)Display Records
            3)Modify Record
            4)Delete Record
            5)Find Record
            6)Empty Records
            7)Close Notebook''')
 print()
       
 ans='y'
 while ans in ('yY'): 


                                                                                #APPEND

    
  operation = int(input("enter operation you want to perform (1/2/3/4/5/6/7):-"))    
  if operation==1:
     

         print("""What do you want to enter in your Notebook:- i)objects
                                    ii)suspects   """)
         print()
         choice = int(input("enter your choice (1/2):-"))
         if choice == 1:
             c2=1
             c1=0
             with open('score_board.csv','r') as file:
                 data = csv.reader(file)
                 rows = []
                
                 for rec in data:
                     if c1==0:     # for the header 
                        c1 = c1 + 1
                        
                     else:
                         if ('OBJECT') in rec[1]:
                             c2 = c2 + 1
                             c1 = c1 + 1
                         else:
                             c1 = c1 + 1
                 
    
                             
             with open('score_board.csv','a') as file:
                 csv_w = csv.writer(file,lineterminator='\n')
                 list_append = []
                 s_no = c1
                 csv_tags = 'OBJECT' + str(c2)
                 csv_tag_name = input("enter object you want to store in the notebook:-")
                 #list_objects = ['canvas','painting',]
                 score=''
                 list_append.append(s_no)
                 list_append.append(csv_tags)
                 list_append.append(csv_tag_name.lower())
                 list_append.append(score)
                 print(list_append)

                 csv_w.writerow(list_append)
                 #operation = int(input("enter the operation you want to perform:-"))

         elif choice == 2:
            
             c2=1
             c1=0
             
             with open('score_board.csv','r') as file:
                 data = csv.reader(file)
                 rows = []
                
                 for rec in data:
                     if c1==0:     # for the header 
                        c1+=1
                        
                     else:
                         if ('SUSPECT') in rec[1]:
                             c2 = c2 + 1
                             c1 = c1 + 1
                         else:
                             c1 = c1 + 1
    
                             
             with open('score_board.csv','a') as file:
                 csv_w = csv.writer(file,lineterminator='\n')
                 list_append = []
                 s_no = c1
                 csv_tags = 'SUSPECT' + str(c2)
                 score=''
                 csv_tag_name = input("enter suspects name you want to store in the notebook:-")
                 list_append.append(s_no)
                 list_append.append(csv_tags)
                 list_append.append(csv_tag_name.lower())
                 list_append.append(score)
                 print(list_append)
                 print()

                 csv_w.writerow(list_append)
                 #operation = int(input("ente the operation you want to perform:-"))

                 
                                                                                #DISPLAY

  if operation == 2:
      with open("score_board.csv") as file:
          data = csv.reader(file)
          #print(file)
          for rec in data:
              print(rec)
          print()    

      #operation = int(input("enter the operation you want to perform:-"))
          
              

                                                                                #MODIFY

  if operation == 3:
     record_name = input("enter the initial record you want to modify:-")
     
     with open('score_board.csv','r') as file:
               data = csv.reader(file)
               rows = []
               c=0
               c1=0
              
               for rec in data:
                  rows.append(rec)
                  #print(rec)

               for rec in rows:
                  if c==0:
                    c+=1
                    
                  elif rec[2] == record_name:
                    modify_record_name = input("enter the new record:-")
                    rec[2] = modify_record_name
                    c1 = c1 + 1

                    
               #print("final records",rows)

               if c1==0:
                 print("no such record found with the name",record_name)
                 print()
                     


     with open('score_board.csv','w') as file:
        #header = ['S.NO','Notebook Tags','Notebook Tag Name']
        csv_w = csv.writer(file,lineterminator='\n')
        #csv_w.writerow(header)
        print("records successfully modified!!")
        print()
        for rec in rows:
          print(rec)
          csv_w.writerow(rec)
        print()
        
         

                                                                                    #DELETE
          
  if operation == 4:
            with open('score_board.csv','r+') as file:
               data = csv.reader(file)
               rows = []
               c=0
               c1=0
               record_name = input("enter the record to be deleted:-")
               
               
               for rec in data:
                  rows.append(rec)

               for rec in rows:
                     if c == 0:
                           c+=1
                     else:
                        if rec[2] == record_name :
                              rec[:] = []
                              c1 = c1 + 1
                              print("Record successfully deleted")
                              print()
               if c1 == 0:
                 print("no such record found with the name", record_name)
                 print()
               

            with open('score_board.csv','w') as file:
                
                csv_w = csv.writer(file,lineterminator='\n')
                

                for rec in rows:
                    if rec == []:
                        pass
                    else:    
                      csv_w.writerow(rec)



                                                                                #FINDING RECORD
                  
  if operation == 5:
    with open('score_board.csv') as file:
      data = csv.reader(file)
      c=0
      c1=0
      rows=[]
      record_name = input("enter the tag of record of which details have to be found:-")

      for rec in data:
        rows.append(rec)

      for rec in rows:
        if c==0:
          c+=1
        else:
          if rec[1].lower() == record_name.lower():
            print(rec)
            print()
            c1 = c1 + 1
      if c1 == 0:
        print("no such record found with the name", record_name)
        print()


                                                                         #EMPTY RECORDS

  if operation == 6:
    conformation = input("Are you sure you want to empty all the records (y/n):-")
    if conformation in 'yY':
      header = ['S.NO','Notebook Tags','Notebook Tag Name','Score']
      with open("score_board.csv",'w') as file:
        csv_w = csv.writer(file,lineterminator='\n')
        csv_w.writerow(header)
        print("all the records are successfully deleted from storage")
        print()



                                                                         #CLOSE NOTEBOOK


  if operation == 7:
      print("the notebook has been successfully closed!!")
      print()
      for i in range(1):
          key=input("Press enter to continue the game.....")
          if key == '\n':
              continue
 
      for i in range(60):
              print(' ',end='')
      for i in range(50):
              print('-',end='')

      break        
            

     

          
          

        

      
    

                
                                                                        #MAIN MENU

            
def main():
    for i in range (167):
        print('*',end='')
    print()
    print('''                                                               WELCOME TO DETECTIVE SIMULATOR ver 4.0''')
    for i in range (167):
        print('*',end='')
    print()
    print('''
                                                                            MAIN MENU

                                               * THIS SIMULATOR IS DESIGNED TO TEST YOUR LOGICAL THINKING SKILLS.
                                               
                                               * IF YOU ARE VERY CONFIDENT ABOUT YOUR SKILLS, GO AHEAD AND START SOLVING... GOOD LUCK!! :)

                                               * READING THE INSTRUCTIONS IS HIGHLY ADVISED TO UNDERSTAND THE BASIC STRUCTURE OF THE GAME...
                                                 "THIS GAME IS NOT LIKE THE OTHERS"...!! :)

                                              
                                               1. INSTRUCTIONS
                                                  To know about basics of detective skills and important instructions (*ADVISED)                                               

                                               2. START
                                                  To start solving crimes
      
                                               3. EXIT
                                                  To Exit the Simulator
    ''')
    for i in range (167):
        print('*',end='')
    print()
    for i in range(2):
        print()

main ()


def proceed():

    ch = input("Proceed to Game? (Y/N)") 
    if ch == "Y" or ch == "y":
        return START()



def mainmenu_enter():
    choice = int(input("Enter Choice (1/2/3):-"))
    return choice
    
       
        
def Instructions():
    print('''                                                                           INSTRUCTIONS:

                                               1. STORE OBSERVATIONS IN THE NOTEBOOK.
                                                    
                                               2. THE NOTEBOOK IS VISUAL DIARY THAT YOU POSSES TO STORE OBSERVATIONS AND USEFUL DATA TO HELP YOU SOLVE THE
                                                  CASE AND CATCH THE KILLER.
                                                    
                                               3. THE OBSERVATIONS WILL BE RECORDED IN THE FORM OF:-
                                                           TAG : OBJECT/ SUSPECT
                                                           FOR EXAMPLE ;- "OBJECT1":"PISTOL"
                                                           *tags will be auto generated
                                                                
                                               4. YOU WILL BE MARKED FOR EACH RECORD YOU ENTER INTO THE NOTEBOOK.

                                               5. THERE ARE NUMEROUS FUNCTIONS YOU CAN PERFORM WITH YOUR NOTEBOOK.
                                                    
                                               6. IMPORTANT OBSERVATIONS LIKE THE MURDER WEAPON AND THE EVIDENCE WILL RESULT INTO GREATER POINTS.
                                                    
                                               7. READ THE GIVEN PARAGRAPHS SLOWLY TO FIND OUT CLUES EFFICIENTLY AND FINALLY WIN!!.

                                               8. SCORING:
                                                     RIGHT ANSWER                               = +1000
                                                     EACH RECORD ENTERED IN THE NOTEBOOK        = +50
                                                     EACH VALID RECORD ENTERED IN THE NOTEBOOK  = +100 
                  ''')
    print()

    
    for i in range(1):
          key=input("Press enter to start the game.....")
          if key == '\n':
              continue
            
          for i in range(60):
              print(' ',end='')
          for i in range(50):
              print('-',end='')
            
      
        
    for i in range(3):
        print()
    return GAME()



                                                                          #ENDGAME
          
def ENDGAME(name):
        import pickle
        score = 0
        file2 = open("REALITY.txt","r")
        s = file2.read()
        words = s.split()
        sd = {}
        file1 = open("answer.dat",'rb')  
        while True:
              try:    
                   sd=pickle.load(file1)
              except EOFError:
                     break
        #print(sd)    
        for i in sd.values():
            for j in words:
                if i.lower().strip() in j.lower():
                    #score+= 100
                    pass
        print()
        for i in range(167):
              print('*',end='')
        print()      
        print("                                                                              RESULTS")
        for i in range(167):
              print('*',end='')
        print()
        
        if name.lower().strip() in ['mr.henrycrowe','henry','mr.henry','mr.crowe','henry crowe','henrycrowe','mr.henry crowe','mr. henry crowe','mr henry crowe','mr. henry','mr. crowe','mr henry','mr crowe']:
            print()
            print('''RIGHT ANSWER : You have brought the murderer to justice!!!.......
               Seems you really have the skill of deduction and logical thinking....... well done :).....you really have the nerve!!!.... Hope we see you again...
               Mentioned below is your final score.....''')
            print()
            score += 1000
        else:
            print()
            print('''WRONG ANSWER : You have failed to brought the murderer to justice!!!
               Well don't lose hope and try again........ Hope to see you again....
               Mentioned below is your final score..''')
            print()



        with open("score_board.csv") as file:
         data = csv.reader(file)
         c=0
         rows=[]
         compare_objects = []
         for rec in data:
           rows.append(rec)
           compare_objects.append(rec[2])
         #print(rows)  
         #print(compare_objects)
         #print()

         file_obj = open('objects.txt')
         lines = file_obj.read()
         #print(lines)
         s=lines.split()
         #print(s)
         records_matched_obj = []
         for i in range(len(compare_objects)):
           #print(compare_objects[i])
           for j in range(len(s)):
            #print(s[j])
            if compare_objects[i] == s[j]:
              records_matched_obj.append(s[j])
         #print(records_matched_obj)

         file_obj = open('suspects.txt')
         lines = file_obj.read()
         #print(lines)
         s=lines.split()
         #print(s)
         records_matched_sus = []
         for i in range(len(compare_objects)):
           #print(compare_objects[i])
           for j in range(len(s)):
            #print(s[j])
            if compare_objects[i] == s[j]:
              records_matched_sus.append(s[j])
         #print(records_matched_sus)
         #print()
      
     
         for i in range(len(rows)):
          #print(rows[i][2])
          for j in range(len(records_matched_obj)):
           #print(records_matched[j])
           if rows[i][2] == records_matched_obj[j]:
             #print(rows[i][2])
             rows[i][3] = 100
             #print(rec[i][3])
         #print(rows)
         #print()

         for i in range(len(rows)):
          #print(rows[i][2])
          for j in range(len(records_matched_sus)):
            #print(records_matched[j])
            if rows[i][2] == records_matched_sus[j]:
              #print(rows[i][2])
              rows[i][3] = 100
              #print(rec[i][3])
         #print(rows)
         #print()


        with open('score_board.csv','w') as file:
          csv_w = csv.writer(file,lineterminator='\n')
          print("Mentioned below - your score for each valid observations you entered in your NOTEBOOK... ")
          print()
          for rec in rows:
           print(rec)
           csv_w.writerow(rec)
          print()

          
        with open('score_board.csv','r') as file:
            csv_w = csv.writer(file,lineterminator = '\n')
            data = csv.reader(file)
            rows=[]
            c=0
            c1=0
            for rec in data:
                rows.append(rec)
                c+=1
            if c == 1:
                print("Did you forget to enter records in the NOTEBOOK, well that carry points.... Better luck with the score next time....:) ")
            #print(rows)

            if c>1 :
                score = score + c*50


            for rec in rows:
                if rec[3] == '100':
                    #print(rec[3])
                    score += 100
                    c1 = c1 + 1

            if c1==0 and c>1:
                print("Well NONE of the records you entered in your notebook is vaild!!!")
                print()
            if c1 >0 and c1 <6:
                print("Could have entered more valid records in the  NOTEBOOK!!...")
                print()
                score = score + 50
            if c1 >= 6:
                score = score + 100
            #print(score)        
                
    
        file1.close()
        file2.close()
        
        l = len(sd)
        #score += l*10
        print('Your FINAL COMBINED SCORE :-',score)
        print()
        
        if  score <= 500:
            print("Your Remark:- BAD!")
            
        elif  score > 500 and score <= 1000:
            print("Your Remark:- GOOD!")
 
            
        elif score > 1000:
            print("""Your Remark:- EXCELLENT!....
Hey Hey seems you entered most of the valid records in the NOTEBOOK....Not every person carry that ability...
you really have good logical thinking and vision.... well done mate... :)""")
            
        '''elif  score>= 1000 and score <= 2000:
            print("Your Remark:- ","AVERAGE!")
        elif  score >= 2000 and score <= 3000:
            print("Your Remark:- ","ABOVE AVERAGE!")'''

        file1.close()
        print()
        seconds = time.time()
        global local_time_2
        local_time_2 = time.ctime(seconds)
        #local_time_2 = global(local_time_2)
        print("End time n date:- ",local_time_2)
        print()
        print()

        final_answer = input("""Enter 'Y' To know the real KILLER with appropriate REASONS!!
                                  OR
Enter ENTER to skip:- """)
        
        if final_answer.lower() == 'y':
          print()
          print()
          print("GIVEN BELOW IS THE SOLUTION TO THE CRIME SCENE.... ")
          print()
          file = open ("real answer.txt")
          lines = file.read()
          print(lines)
        else:
          pass

        for i in range(5):
           print()
           
        print("""
                                                            Thanks for playing DETECTIVE SIMULATOR ver 4.0.
                                                                  Hope you had a great experience!!
                                                                    Have a wonderful day ahead:)
                                                                Hope we meet you soon, till then SAYONARA!!!
                                                                    
""")
        for i in range(167):
              print('-',end='')
        

                                                                       # LEVELS

def GAME():
    file1 = open("CASE.txt","r")
    position = [502,331,366,390,155,478 ,707,555,500]
    
    seconds = time.time()
    global local_time_1
    local_time_1 = time.ctime(seconds)
    #local_time_1 = global(local_time_1)
    print("Start time N date:-",local_time_1)
    
    name = input('''Enter Name:-''')
    age=int(input("enter age:-"))
    for i in range(2):
        print()
    for i in position:
            print ("                                                                           ",file1.read(i))
            print()
            print("What you would like to do Detective",name.upper()," ? " )
            print()
            print('               1) Open Notebook ')
            print('               2) Proceed with the case file ')
            print('               3) Use the help of Hints')
            print()
            print("ADVISORY:- DO NOT FORGET TO ENTER RECORDS IN YOUR NOTEBOOK FROM TIME TO TIME..... THESE RECORDS CARRY POINTS....")
            print()
            a = int(input("Enter Option (1/2/3):-"))
            if a == 1:
                   NOTEBOOK()
            elif a == 2:
                    print(" "*65, "-"*50)
                    continue
            elif a == 3:
                    file2 = open("Evidence.txt","r")
                    s = file2.read()
                    for i in range(2):
                        print()
                    print("Here are some of the evidences found at the crime scene...")
                    print()
                    print(s)
                    print()
                    key=input("Press enter to continue further.....")
                    if key=='\n':
                        continue
                    print(" "*65, "-"*50)
                    for i in range(2):
                        print()
                    
                    a = 1
                    file2.close()
    if i == 500:
            for i in range(167):
                print("-",end='')
            for i in range(3):
                print()
                
            print("                                                                        REPORT SUBMISSION")
            print()
            print('''Mentioned below are some of the names of the people who were very close to MR.BASIL.

                                       1)Mr.Dorian Wilde - A frequent visitor
                                       2)Mrs.Crowe - Mr.Henry's beloved wife
                                       3)Mr.Henry Crowe - A close friend who lived close by''')
            print()
            print("Now it is your turn...",name.upper(),"...find out the killer of Mr.Basil and bring him to justice !!")
            print()
            murd = input("Enter SUSPECT'S NAME:-")
            ENDGAME(murd)

            

                                                                          # MainMENU
def choicee():
    a = mainmenu_enter()
    if a == 1:
       
        print ( Instructions())
    elif a == 2:
        print(GAME())
    elif a == 3:
        print()
        print()
        print()
        print("""
                                                            Thanks for playing DETECTIVE SIMULATOR ver 4.0.
                                                                  Hope you had a great experience!!
                                                                    Have a wonderful day ahead:)
                                                                Hope we meet you soon, till then SAYONARA!!!
                                                                    
""")
    
        for i in range(167):
              print('-',end='')
        pass

choicee()

 
