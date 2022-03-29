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
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Store the header row as a variable
    csv_header = next(csvfile)
    
    data_dict = {rows[0]:int(rows[1]) for rows in csvreader}
    
    totalMonths = len(data_dict)
    total = sum(data_dict.values())
    # averageChange = 
    greatestInc = max(data_dict, key=data_dict.get)

print(f"""Financial Analysis
------------------------------
Total Months: {totalMonths}
Total: ${total}
Average Change: 
Greatest Increase in Profits: {greatestInc}
Greatest Decrease in Profits: 
""")
