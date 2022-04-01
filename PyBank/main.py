# This is the python file for the first challenge, "PyBank"

# first, we import the necessary modules so we can 
# navitage to and open csv files in python
import os
import csv

# next, create variable to the path where the csv lives
# if this were pandas, we'd read it into a dataframe
csvpath = os.path.join("Resources","budget_data.csv")

# read in the csv file, specify encoding as utf
with open(csvpath,encoding='utf') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ',')
   
    monthList = []
    profitList = []

    for col in csvreader:
        monthList.append(col['Date'])
        profitList.append(int(col['Profit/Losses']))

# This will find the total number of months (bullet point #1)
totalMonths = len(monthList)

# This will find the total profit/loss over the entire period (bullet point #2)
totalProfit = sum(profitList)

# This will find the month-over-month changes and then the
# average of those changes (bullet point #3)
deltaList = []
for x, y in zip(profitList[0::], profitList[1::]):
    deltaList.append(y-x)
avgChange = round(sum(deltaList)/len(deltaList),2)

# Using the max() function, this code will find the greatest increase in month-over-
# month profit and return the corresponding month when this occurred (bullet point #4)
maxIncrease = max(deltaList)
monthmaxIncrease = monthList[deltaList.index(maxIncrease)+1]

# Using the min() function, this code will find the greatest decrease in month-over-
# month profit and return the corresponding month when this occurred (bullet point #5)
maxDecrease = min(deltaList)
monthmaxDecrease = monthList[deltaList.index(maxDecrease)+1]

# Here is a list of text lines we'll loop through to write the results
# Note that we format any numbers with commas as thousands separators
textLines = ["Financial Analysis","------------------------------------",
            f"Total Months: {totalMonths}",f"Total: ${totalProfit:,}",
            f"Average Change: ${avgChange:,}",
            f"Greatest Increase in Profits: {monthmaxIncrease} (${maxIncrease:,})",
            f"Greatest Decrease in Profits: {monthmaxDecrease} (${maxDecrease:,})"

]

# Now that we have all the variables & lines we'll need in our print statement,
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

