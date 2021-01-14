#importing libraries to read CSV
import os
import csv
#creating a path to read the file
csvpath = os.path.join('Instructions', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # save the csv data in csvreader
    next(csvreader)
    #looping through each row
    rows = []
    month_total = 0
    month_count = 0
    month_average = 0
    great_profit=0
    for row in csvreader:
        rows.append(row)
        #calulate total_months
        month_count = month_count +1
        #calculate monthly total
        month_total = (int(month_total) + int(row[1]))
        #calculate month average
        #find greatest increase
    great_profit= 0
    if int(row[1]) > great_profit:
        great_profit = int(row[1])
    else:
        great_profit= 0
            
   
    print('Financial Analysis')
    print("---------------------------------")
    print('Total Months:', month_count)
    print('Total Month $: ', month_total)
    print(great_profit)

#print(rows)


        
    
    
            
 
        
        
        

    

          
        