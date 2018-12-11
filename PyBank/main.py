#Import necessary libriaries
import os
import csv
import sys
#Define average function
def average(list):
    return int(sum(list) / len(list))

#Create a path for the file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open the csv file
with open(csvpath, newline='') as csvfile:
    # read the file
    csvreader = csv.reader(csvfile, delimiter = ',')

    #To avoid from the 1st row (header)
    csv_header = next(csvreader)

    #Convert the data to list
    сsv_reader = list(csvreader)

    #Calculate the total number of months included in the dataset
    rowcount = len(сsv_reader)


    #Empty list to place data of the differences of each row.
    change=[]

    #Calculate the total net amount of "Profit/Losses" over the entire period
    total = 0
    for row in сsv_reader:
       total = total + int(row[1])
       change.append(int(row[1]))


    #Calculate the average change in "Profit/Losses" between months over the entire period
    diff = [change[i]-change[i-1] for i in range(1,len(change))]

    ##Using Custom average function above
    totalaverage = average(diff)
    greatestInc= max(diff)
    greatestDec = min(diff)

    #Find
    max_index = diff.index(greatestInc)
    max_month = сsv_reader[max_index+1][0]

    min_index = diff.index(greatestDec)
    min_month = сsv_reader[min_index+1][0]

    #sys.stdout= open('output.txt', 'w')
    print(f"Total Months:  {rowcount}")
    print(f"Total:  ${total}")
    print(f"Average Change:  ${totalaverage}")
    print(f"Greatest Increase in Profits: {max_month} (${greatestInc})")
    print(f"Greatest Decrease in Profits: {min_month} (${greatestDec})")























