import os 
import csv
# importing data
data = os.path.join('..','Resources','election_data.csv')
with open(data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skipping over header row
    next(csvreader)
    total_vote = []
    for row in csvreader:
        total_vote.append(row)
print(len(total_vote))
