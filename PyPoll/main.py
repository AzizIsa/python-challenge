#Import necessary libriaries
import os
import csv

#Create a path for the file
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the csv file
with open(csvpath, newline='') as csvfile:
    # read the file
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)


