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
    greatest_increase=0
    greatest_decrease = 0
    for row in csvreader:
        rows.append(row)
        #calulate total_months
        month_count = month_count +1
        #calculate monthly total
        month_total = (int(month_total) + int(row[1]))
        #find greatest increase
    #intialize variable for greatest profit increase
    #if row is bigger than greatest profit
    if int(row[1]) > greatest_increase:
        #greatest profit is equal to row 1
        greatest_increase = int(row[1])
        #else, greatest profit is equal to 0
    #if row is less than lowest profit
    if int(row[1]) < greatest_decrease:
        greatest_decrease = row[1]
  
    
            
   
    print('Financial Analysis')
    print("---------------------------------")
    print('Total Months:', month_count)
    print('Total Month $: ', month_total)
    print(greatest_decrease)
#print(rows)


        
    
    
            
 
        
        
        

    

          
        