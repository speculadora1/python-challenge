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
    numMonths = 0
    profitLoss = 0
    lastPL = 0
    diff = 0
    plChanges = []
    hiChange = 0
    hiMonth = ""
    loChange = 0
    loMonth = ""
    
    # Collect data for financial analysis summary
    for row in budgetData:
        numMonths = numMonths + 1
        profitLoss = profitLoss + int(row[1])
        diff = int(row[1]) - lastPL
        if lastPL != 0:
            plChanges.append(diff)
        if int(row[1]) > hiChange:
            hiMonth = row[0]
            if lastPL != 0:
                hiChange = int(row[1]) - lastPL
        if int(row[1]) < loChange:
            loMonth = row[0]
            if lastPL != 0:
                loChange = int(row[1]) - lastPL
        lastPL = int(row[1])

# Print summary output
print(f"Financial Analysis\n\
----------------------------\n\
Total Months: {numMonths}\n\
Total: ${profitLoss}\n\
Average Change: ${round(sum(plChanges)/len(plChanges),2)}\n\
Greatest Increase in Profits: {hiMonth} (${hiChange})\n\
Greatest Decrease in Profits: {loMonth} (${loChange})")