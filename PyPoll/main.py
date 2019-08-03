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

#To set path for the csv file(election_data.csv)
csvpath = os.path.join("Resources", "election_data.csv")
#print(os.path.join("Resources", "election_data.csv"))

#Open the csv file(election_data.csv)
with open(csvpath, newline="") as csvfile:
    
    #csv.reader will read the content inside the csv file with delimiter " , "
    csvreader = csv.reader(csvfile, delimiter=",")
    #For removing header "next(csvreader)" is used
    next(csvfile)
    
    #Declare variables as empty dictionaries and lists
    row_count = 0
    candidate = []
    uniquie_candidate = []
    candiate_votes = []
    candidate_votes_percentage = []
   
    for row in csvreader:
        
        candidate.append(row[2])

        #Here "row_count" is used to find out the total number of votes cast ie "Total Votes"
        row_count = row_count + 1
    
    uniquie_candidate = list(set(candidate))

    #print(uniquie_candidate)
    
    # Print Statements
    printing("Election Results")
    printing("-------------------------------")
    printing("Total Votes: " + str(row_count))
    printing("-------------------------------")

    for name in uniquie_candidate:

        #print(name)
        votes_per_candidate = candidate.count(name)
        candiate_votes.append(votes_per_candidate)
        #print(votes_per_candidate)
        votes_percentage_per_candiate = round((votes_per_candidate/row_count) * 100,3)
        candidate_votes_percentage.append(votes_percentage_per_candiate)
        #print(votes_percentage_per_candiate)
        printing(name + ": " + str(votes_percentage_per_candiate) + "% (" + str(votes_per_candidate) + ")") 
        
    
    #print(candiate_votes)
    #print(candidate_votes_percentage)
    max_votes = max(candiate_votes)
    min_votes = min(candiate_votes)
    #print(max_votes)
    #print(uniquie_candidate)
    
    winner = str(uniquie_candidate[candiate_votes.index(max_votes)])
    printing("-------------------------------")
    printing("Winner: " + winner)
    printing("-------------------------------")


outputFile.close()
    