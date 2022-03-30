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

# Now invert the dictionary mapping so we get 1 candidate and then a slew of 
# unique IDs corresponding to everyone that voted for him / her
invElectionDict = defaultdict(list)
for key, value in electionDict.items():
    invElectionDict[value].append(key)

# create another dictionary to print the length of values for each key (aka politician)
# by using a dictionary comprehension
length_ElectionDict = {key: len(value) for key, value in invElectionDict.items()}
print(length_ElectionDict)