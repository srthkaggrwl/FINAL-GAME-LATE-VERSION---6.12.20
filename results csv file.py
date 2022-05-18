import csv
header = ['Name','key','value']

with open('results.csv','w') as file:
    csv_w = csv.writer(file,lineterminator='\n') #csv_w = csv_writer
    csv_w.writerow(header)

with open ('results.csv','a') as file:
    csv_w = csv.writer(file,lineterminator = '\n')
    list_append = []
    list_append.append(x)
    list_append.append(l)
    
with open('results.csv') as file:
   data = csv.reader(file)
   for record in data:
         print(record)    
