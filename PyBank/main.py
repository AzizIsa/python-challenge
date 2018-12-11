#Import necessary libriaries
import os
import csv

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
    print(rowcount)

    #Empty list to place data of the differences of each row.
    change=[]

    #Calculate the total net amount of "Profit/Losses" over the entire period
    total = 0
    for row in сsv_reader:
       total = total + int(row[1])
       change.append(int(row[1]))
    print(total)

    #Calculate the average change in "Profit/Losses" between months over the entire period
    diff = [change[i]-change[i-1] for i in range(1,len(change))]

    ##Using Custom average function above
    totalaverage = average(diff)
    print(totalaverage)
    greatestInc= max(diff)
    print(greatestInc)
    greatestDec = min(diff)
    print(greatestDec)























