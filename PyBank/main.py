# Import dependencies
import os
import csv

# Establish .csv file path
filepath = os.path.join('..','Resources','budget_data.csv')

with open(filepath, newline = '') as csvreader:
    budgetData = csv.reader(csvreader, delimiter = ",")

    # Add header line
    header = next(budgetData)
    #print(f"CSV Header: {header}")
    
    # Preview data set
    #for row in budgetData:
    #    print(row)

    # Initialize variables
    iterator = 1 # tracks loop iteration
    numMonths = 0 # total number of months
    profitLoss = 0 # total profit/loss
    lastPL = 0 # stores previous profit/loss
    diff = 0 # difference in profit/loss from previous month
    plChanges = [] # list of changes in profit/loss
    hiChange = 0 # high change in profit/loss
    hiMonth = "" # month-year of high change
    loChange = 0 # low change in profit/loss
    loMonth = "" # month-year of low change
    
    # Collect data for financial analysis summary
    for row in budgetData:
        numMonths = numMonths + 1
        profitLoss = profitLoss + int(row[1])
        diff = int(row[1]) - lastPL
        if iterator > 1:
            plChanges.append(diff)
        if int(row[1]) > hiChange:
            if iterator > 1:
                hiChange = int(row[1]) - lastPL
                hiMonth = row[0]
        if int(row[1]) < loChange:
            if iterator > 1:
                loChange = int(row[1]) - lastPL
                loMonth = row[0]
        lastPL = int(row[1])
        iterator = iterator + 1

# Print summary output
print(f"Financial Analysis\n\
----------------------------\n\
Total Months: {numMonths}\n\
Total: ${profitLoss}\n\
Average Change: ${round(sum(plChanges)/len(plChanges),2)}\n\
Greatest Increase in Profits: {hiMonth} (${hiChange})\n\
Greatest Decrease in Profits: {loMonth} (${loChange})")