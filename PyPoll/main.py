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


    uniq_list=[]
    candidates=[]
    for row in csv_reader:
        candidates.append(str(row[2]))
        if row[2] not in uniq_list:
            uniq_list.append(row[2])
        else:
            continue

    print(uniq_list)

    candidate1 = candidates.count(uniq_list[0])
    candidate2 = candidates.count(uniq_list[1])
    candidate3 = candidates.count(uniq_list[2])
    candidate4 = candidates.count(uniq_list[3])

    can1_percent = int((candidate1/ rowcount) * 100)
    can2_percent = int((candidate2/ rowcount) * 100)
    can3_percent = int((candidate3/ rowcount) * 100)
    can4_percent = int((candidate4/ rowcount) * 100)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {rowcount}")
    print("-------------------------")
    print( uniq_list[0] +": " + str(can1_percent) + ".00% " +"("+str(candidate1)+")")
    print( uniq_list[1] +": " + str(can2_percent) + ".00% " +"("+str(candidate2)+")")
    print( uniq_list[2] +": " + str(can3_percent) + ".00% " +"("+str(candidate3)+")")
    print( uniq_list[3] +": " + str(can4_percent) + ".00% " +"("+str(candidate4)+")")
    print("-------------------------")













