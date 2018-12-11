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
    csv_reader = list(csvreader)
    rowcount = int(len(csv_reader))
    print(rowcount)

    uniq_list=[]
    for row in csv_reader:
        if row[2] not in uniq_list:
            uniq_list.append(row[2])
        else:
            continue
    print(uniq_list)













