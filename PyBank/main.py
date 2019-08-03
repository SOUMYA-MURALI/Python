#Importing operating system and the csv file
import os
import csv

#Specifying the path for the output text file 
#Here output file is printing in the current working directory
outputFile = open(os.path.join(os.getcwd(),'outputfile.txt'), 'w')
#print(os.path.join(os.getcwd(),'outputfile.txt'))

#Function to print text to the terminal and to the output file
def printing(text):
    print(text)
    if outputFile:
        outputFile.write(str(text + "\n"))


#Defining variables
row_count = 0
total_sum = 0
previous_column_sum = 0
average_change = 0
change_count = 0

#To set path for the csv file(budget_data.csv)
csvpath = os.path.join('Resources', 'budget_data.csv')

#Open the csv file(budget_data.csv)
with open(csvpath, newline='') as csvfile:

    #csv.reader will read the content in the csv file with delimiter " , "
    csvreader = csv.reader(csvfile, delimiter=',')

    #For removing header "next(csvreader)" is used
    next(csvreader)
    
    #Declaring variables as empty lists
    #To get the values of "Average Change" , "Greatest Increase in Profits" , and "Greatest Decrease in Profits" 
    #Lists such as "date_value" and "change" are used
    date_value = []
    change = []

    #Loop through each row
    for row in csvreader:
        
        column_sum = int(row[1])
        
        if row_count > 0: 

            #adding values to the list "change"      
            change.append(column_sum - previous_column_sum)
            #adding values to the list "date_value"
            date_value.append(row[0])

        #Here "row_count" is used to find out the "Total Months"
        row_count = row_count + 1 

        #The "total_sum" is used to find out the "Total"       
        total_sum = total_sum + column_sum   
        
        previous_column_sum = column_sum

    #For calculating the "Average Change", divide "sum(change)"  by  "len(change)"  
    average_change = round(sum(change) / len(change), 2) 

    #For calculating the "Greatest Increase in Profits"
    greatest_increase = max(change)
    greatest_increase_date_value = str(date_value[change.index(greatest_increase)])

    #For calculating the "Greatest Decrease in Profits"
    greatest_decrease = min(change)
    greatest_decrease_date_value = str(date_value[change.index(greatest_decrease)])
    

#print statements
printing("Financial Analysis")
printing("---------------------------------------------------")
printing("Total Months:" + str(row_count))
printing("Total: $" + str(total_sum))
printing("Average Change:" + str(average_change))
printing("Greatest Increase in Profits: " + str(greatest_increase_date_value) + " ($" + str(greatest_increase) +")")
printing("Greatest Decrease in Profits: " + str(greatest_decrease_date_value) + " ($" + str(greatest_decrease)+")")
  
  
outputFile.close()