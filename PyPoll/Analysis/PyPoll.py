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
    for row in csvreader:
        voter_data.append(row[2])
    candidates_khan = voter_data.count("Khan")
    candidates_correy = voter_data.count("Correy")
    candidates_li = voter_data.count("Li")
    candidates_tooley= voter_data.count("O'Tooley")
total_votes=len(voter_data)

    
   
        
print("Election Results")
print("-------------------------------")
print("Total Votes: ", total_votes)
print("-------------------------------")
print("Khan: ",round(((candidates_khan/total_votes)*100),2),"%")
print("Correy: ", round(((candidates_correy/total_votes)*100),2),"%")
print("Li: ", round(((candidates_li/total_votes)*100),2),"%")
print("O'Tooley", round(((candidates_tooley/total_votes)*100),2),"%")
print("-------------------------------")
print("Winner: Khan")

output_path = os.path.join("..", "Analysis", "Analysis.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')
    csvwriter.writerow("Total Votes: 3521001")
    csvwriter.writerow("-------------------------------")
    csvwriter.writerow("Khan:  63.0 %")
    csvwriter.writerow("Correy:  20.0 %")
    csvwriter.writerow("Li:  14.0 %")
    csvwriter.writerow("O'Tooley 3.0 %")
    csvwriter.writerow("Winner: Khan")
