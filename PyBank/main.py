
import os
import csv

row_count = 0
total_sum = 0
previous_column_sum = 0
total_change = 0
change_count = 0

#we have to specify the csv file path (from main.py)
csvpath = os.path.join('Resources', 'budget_data.csv')

#file = open(csvpath)
#numline = len(file.readlines())
#print(numline)
#open csvfile to use that,csv.reader will read the content in the csv file with delimiter " , "
with open(csvpath, newline='') as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=',')
    #for removing header "next(csvreader)" is used
    next(csvreader)
        
    #print(csvreader)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    print("Financial Analysis")
    print("---------------------------------------------------")

    for row in csvreader:
        #print(row[1])
        column_sum = int(row[1])
       
        #if isinstance(column_sum, int): # check whether is integer
            #print("is integer")
        #else:
            #print("is string")
          
        if row_count == 0: 
            change = 0
        else:
            change = column_sum - previous_column_sum
            change_count += 1 
        #print("Change is" + ": " + str(change))
        
        total_sum = total_sum + column_sum
        total_change = total_change + change 
        previous_column_sum = column_sum
    
        #row_count += 1
        row_count = row_count + 1

average_change = round(total_change / change_count, 2)

print("Total Months:" + str(row_count))
print("Total: $" + str(total_sum))
print("Total Change: $" + str(total_change))
print("Total Change Count: $" + str(change_count))
print("Average Change:" + str(average_change))



