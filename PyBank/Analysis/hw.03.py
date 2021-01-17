#importing libraries to read CSV
import os
import csv
#creating a path to read the file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # save the csv data in csvreader
    next(csvreader)
    #storing data in row column
    rows = []
    #variables to store length totals
    month_count = 0
    month_total = 0
    great_increase = []
    changes=[]
    change=0
#   looping through each list 
    for row in csvreader:
        rows.append(row)
        #calulate total_months
        month_count = month_count +1
        #calculate monthly total
        month_total = (int(month_total) + int(row[1]))
        #subtract next row from current row
        month_change= int(row[1]) - change
        changes.append(month_change)
        change = int(row[1])
        
    #find the average of the list for changes
    average= sum(changes) / len(changes)

    print('Financial Analysis')
    print("---------------------------------")
    print('Total Months:', month_count)
    print('Total: ','$', month_total)
    print('The average change was ', round(average, 2))
    print('The greatest increase in profits was $', max(changes))
    print('The greatest decrease in profits was $', min(changes))

            
 
        
        
        

    

          
        