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
    
    # Preview data set (uncommented as needed)
    #for row in budgetData:
    #    print(row)

    # Initialize variables
    numMonths = 0
    profitLoss = 0
    # Count number of rows (months) in data set
    for row in budgetData:
        numMonths = numMonths + 1
        profitLoss = profitLoss + int(row[1])

# Print summary output
print(f"Financial Analysis\n\
----------------------------\n\
Total Months: {numMonths}\n\
Total: ${profitLoss}")