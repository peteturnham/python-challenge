#importing libraries to read CSV
import os
import csv
#creating a path to read the file
csvpath = os.path.join('Instructions', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # save the csv data in csvreader
    next(csvreader)
    #storing data in row column
    rows = []
    #variable to store length of total months
    month_count = 0
    month_total = 0
    def average(rows):
        return sum(rows[1]) / len(rows)

    for row in csvreader:
        rows.append(row)
        #calulate total_months
        month_count = month_count +1
        #calculate monthly total
        month_total = (int(month_total) + int(row[1]))
   

    print('Financial Analysis')
    print("---------------------------------")
    print('Total Months:', month_count)
    print('Total Month $: ', month_total)
    print(f'the Greatest Increase was', max(rows[1]))
    print(f'the Greatest Decrese was', min(rows[1]))
#print(rows)


        
    
    
            
 
        
        
        

    

          
        