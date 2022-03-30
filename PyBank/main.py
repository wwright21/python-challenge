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

    # # Store the header row as a variable
    # csv_header = next(csvfile)
    
    monthList = []
    profitList = []

    for col in csvreader:
        monthList.append(col['Date'])
        profitList.append(int(col['Profit/Losses']))

# This will find the total number of months (bullet point #1)
totalMonths = len(monthList)
print(totalMonths)

# This will find the total profit/loss over the entire period (bullet point #2)
totalProfit = sum(profitList)
print(totalProfit)

# This will find the month-over-month changes and then the
# average of those changes (bullet point #3)
deltaList = []
for x, y in zip(profitList[0::], profitList[1::]):
    deltaList.append(y-x)
avgChange = sum(deltaList)/len(deltaList)
print(avgChange)

# Using the max() function, this code will find the greatest increase in month-over-
# month profit and return the corresponding month when this occurred (bullet point #4)
maxIncrease = max(deltaList)
monthmaxIncrease = monthList[deltaList.index(maxIncrease)+1]
print(maxIncrease)
print(monthmaxIncrease)

# Using the min() function, this code will find the greatest decrease in month-over-
# month profit and return the corresponding month when this occurred (bullet point #5)
maxDecrease = min(deltaList)
monthmaxDecrease = monthList[deltaList.index(maxDecrease)+1]
print(maxDecrease)
print(monthmaxDecrease)



# print(f"""Financial Analysis
# ------------------------------
# Total Months: {totalMonths}
# Total: ${total}
# Average Change: 
# Greatest Increase in Profits: {greatestInc}
# Greatest Decrease in Profits: 
# """)

