import os 
import csv
# importing data
data = os.path.join('..','Resources','election_data.csv')
   

#looping over our data witht the csv module
with open(data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skipping over header row
    next(csvreader)
    voter_data=[]
    candidates={}
    for row in csvreader:
        voter_data.append(row)
    for row in csvreader:
        candidates.update(row[2])




        
print("Election Results")
print("-------------------------------")
print("Total Votes: ", len(voter_data))
print("-------------------------------")
#print(voter_data)
print(candidates)


