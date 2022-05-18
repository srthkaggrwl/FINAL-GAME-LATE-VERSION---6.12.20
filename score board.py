import csv


header = ['S.NO','Notebook Tags','Notebook Tag Name','Score']
records = [['1','OBJECT1','clock',''],['2','OBJECT2','canvas',''],['3','OBJECT3','unfinishedpainting','']]
with open("score_board.csv",'w') as file:
    csv_w = csv.writer(file,lineterminator='\n')
    csv_w.writerow(header)
    for i in range(len(records)):
      csv_w.writerow(records[i])


print('''
            1)Enter Record
            2)Display Records
            3)Modify Record
            4)Delete Record
            5)Find Record
            6)Empty Records  ''')
       
ans='y'
while ans in ('yY'): 


  #APPEND
  operation = int(input("enter operation you want to perform"))    
  if operation==1:
     

         print("""What do you want to append:- i)objects
                            ii)suspects   """)
         choice = int(input("enter your choice (1/2):-"))
         if choice == 1:
             c2=1
             c1=0
             with open('score_board.csv','r') as file:
                 data = csv.reader(file)
                 rows = []
                
                 for rec in data:
                     #print(rec[1])
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
                 csv_tag_name = input("enter object you want to append:-")
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
                         if ('suspect') in rec[1]:
                             c2 = c2 + 1
                             c1 = c1 + 1
                         else:
                             c1 = c1 + 1
    
                             
             with open('score_board.csv','a') as file:
                 csv_w = csv.writer(file,lineterminator='\n')
                 list_append = []
                 s_no = c1
                 csv_tags = 'suspect' + str(c2)
                 score=''
                 csv_tag_name = input("enter suspects name you want to append:-")
                 list_append.append(s_no)
                 list_append.append(csv_tags)
                 list_append.append(csv_tag_name.lower())
                 list_append.append(score)
                 print(list_append)

                 csv_w.writerow(list_append)
                 #operation = int(input("ente the operation you want to perform:-"))













































































                 
                 
  #DISPLAY

  if operation == 2:
      with open("score_board.csv") as file:
          data = csv.reader(file)
          #print(file)
          for rec in data:
              print(rec)

      #operation = int(input("enter the operation you want to perform:-"))
              
'''
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
                     


     with open('score_board.csv','w') as file:
        #header = ['S.NO','Notebook Tags','Notebook Tag Name']
        csv_w = csv.writer(file,lineterminator='\n')
        #csv_w.writerow(header)

        for rec in rows:
          print(rec)
          csv_w.writerow(rec)


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
               if c1 == 0:
                 print("no such record found with the name", record_name)
               

            with open('score_board.csv','w') as file:
                
                csv_w = csv.writer(file,lineterminator='\n')
                

                for rec in rows:
                  csv_w.writerow(rec)



  if operation == 5:
    with open('score_board.csv') as file:
      data = csv.reader(file)
      c=0
      c1=0
      rows=[]
      record_name = input("enter the record of which details have to be found:-")

      for rec in data:
        rows.append(rec)

      for rec in rows:
        if c==0:
          c+=1
        else:
          if rec[2] == record_name:
            print(rec)
            c1 = c1 + 1
      if c1 == 0:
        print("no such record found with the name", record_name)


  if operation == 6:
    conformation = input("Are you sure you want to empty all the records (y/n):-")
    if conformation in 'yY':
      header = ['S.NO','Notebook Tags','Notebook Tag Name','Score']
      with open("score_board.csv",'w') as file:
        csv_w = csv.writer(file,lineterminator='\n')
        csv_w.writerow(header)
        print("all the records are successfully deleted from storage")





  if operation == 0:
    with open("score_board.csv") as file:
      data = csv.reader(file)
      c=0
      rows=[]
      compare_objects = []
      for rec in data:
        rows.append(rec)
        compare_objects.append(rec[2])
      #print(rows)  
      print(compare_objects)

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
      print(records_matched_sus)            
      
     
      for i in range(len(rows)):
       #print(rows[i][2])
       for j in range(len(records_matched_obj)):
         #print(records_matched[j])
         if rows[i][2] == records_matched_obj[j]:
           #print(rows[i][2])
           rows[i][3] = 10
           #print(rec[i][3])
      print(rows)

      for i in range(len(rows)):
       #print(rows[i][2])
       for j in range(len(records_matched_sus)):
         #print(records_matched[j])
         if rows[i][2] == records_matched_sus[j]:
           #print(rows[i][2])
           rows[i][3] = 10
           #print(rec[i][3])
      print(rows)      


    with open('score_board.csv','w') as file:
       csv_w = csv.writer(file,lineterminator='\n')
       for rec in rows:
         print(rec)
         csv_w.writerow(rec)'''

     

          
          

        

      
    
