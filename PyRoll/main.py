# This is the python file for the second challenge, "PyRoll"

# first, we import the necessary modules so we can 
# navitage to and open csv files in python
import os
import csv
from collections import defaultdict

# next, create variable to the path where the csv lives
csvpath = os.path.join("Resources","election_data.csv")

# read in the csv file, specify encoding as utf, and convert to a dictionary
# Note that the code reads in the first and third column of the csv file,
# as we are not particularly concerned with the second column ('county')
with open(csvpath,encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',', skipinitialspace=True)
    header = next(csvreader)
    electionDict = {rows[0]:rows[2] for rows in csvreader}

# Now invert the dictionary mapping so we get 1 candidate and then every unique
# ID that voted for him / her
invElectionDict = defaultdict(list)
for key, value in electionDict.items():
    invElectionDict[value].append(key)

# create another dictionary to print the length of values for each key (aka politician)
# by using a dictionary comprehension. This dictionary will contain everything
# we need to solve this challenge!
length_ElectionDict = {key: len(value) for key, value in invElectionDict.items()}

# Find the total votes
totalVotes = sum(length_ElectionDict.values())

# The votes by candidate is already stored as the value in our length_ElectionDict. So,
# let's find the percentage breakdown by candidate
CCSperc = round(length_ElectionDict['Charles Casper Stockham'] / totalVotes * 100,3)
DDperc = round(length_ElectionDict['Diana DeGette'] / totalVotes * 100,3)
RADperc = round(length_ElectionDict['Raymon Anthony Doane'] / totalVotes * 100,3)

# Find the winning politician by first finding the max value of the 
# length_ElectionDict dictionary 
winner = list(length_ElectionDict.keys())[list(length_ElectionDict.values()).index(max(length_ElectionDict.values()))]
print(winner)
