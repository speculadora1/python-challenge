# Import dependencies
import os
import csv

# Establish .csv file path
filepath = os.path.join('..','Resources','election_data.csv')

with open(filepath, newline = '') as csvreader:
    electionData = csv.reader(csvreader, delimiter = ",")

    # Skip header row
    next(electionData)
    
    # Preview data set
    # for row in budgetData:
    #    print(row)

    # Initialize variables
    votes = 0 # total number of votes cast
    candidates = [] # list of unique candidates receiving votes
    vote_counts = [] # list of corresponding vote counts for each candidate

    for row in electionData:
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_counts.append(0)

    # Return to top of .csv file and skip header row
    csvreader.seek(0)
    next(electionData)

    for row in electionData:
        votes = votes + 1
        vote_counts[candidates.index(row[2])] += 1


print(vote_counts)

print(f"Election Results\n\
-------------------------\n\
Total Votes: {votes}\n\
-------------------------\n\
{candidates[0]}: {(vote_counts[0]/sum(vote_counts)):2.2%} ({vote_counts[0]})\n\
{candidates[1]}: {(vote_counts[1]/sum(vote_counts)):2.2%} ({vote_counts[1]})\n\
{candidates[2]}: {(vote_counts[2]/sum(vote_counts)):2.2%} ({vote_counts[2]})\n\
{candidates[3]}: {(vote_counts[3]/sum(vote_counts)):2.2%} ({vote_counts[3]})")