# This is the python file for the second challenge, "PyRoll"

# first, we import the necessary modules so we can 
# navitage to and open csv files in python
import os
import csv
from collections import defaultdict

# next, create variable to the path where the csv lives
csvpath = os.path.join("Resources","election_data.csv")

# read in the csv file using the DictReader class. We create an empty
# list to store all the values in the "Candidate" column
with open(csvpath,encoding='utf') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ',')
    votesList = []
    for col in csvreader:
        votesList.append(col["Candidate"])

# To make things run a little more quickly, we use the set() function to
# get a list of the unique values in the "Candidates" column. We then
# use dictionary comprehension to create a new dictionary with all the 
# votes tallied up by candidate 
setList = list(set(votesList))
votesDict = {i:votesList.count(i) for i in setList}

# Find the total votes
totalVotes = sum(votesDict.values())

# The votes by candidate is already stored as the value in our length_ElectionDict. So,
# let's find the percentage breakdown by candidate
CCSperc = round(votesDict['Charles Casper Stockham'] / totalVotes * 100,3)
DDperc = round(votesDict['Diana DeGette'] / totalVotes * 100,3)
RADperc = round(votesDict['Raymon Anthony Doane'] / totalVotes * 100,3)

# Find the winning politician by first finding the max value of the 
# votesDict dictionary 
winner = list(votesDict.keys())[list(votesDict.values()).index(max(votesDict.values()))]

# Here is a list of text lines we'll loop through to write the results
# Note that we format any numbers with commas as thousands separators
textLines = ["Election Results","-----------------------------------------",
            f"Total Votes: {totalVotes:,}","-----------------------------------------",
            f"Charles Casper Stockham: {CCSperc}% ({votesDict['Charles Casper Stockham']:,})",
            f"Diana DeGette: {DDperc}% ({votesDict['Diana DeGette']:,})",
            f"Raymon Anthony Doane: {RADperc}% ({votesDict['Raymon Anthony Doane']:,})",
            "-----------------------------------------",f"Winner: {winner}",
            "-----------------------------------------"           
]

# Now that we have all the variables we'll need in our print statement,
# let's specify a path to write this to a .txt file
export_path = os.path.join("analysis","results.txt")

# open file in write mode
with open(export_path,'w') as results:
    for x in textLines:
        results.write(x)
        results.write("\n")

# Print results to the gitbash terminal
for x in textLines:
    print(x)
