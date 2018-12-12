#Import necessary libriaries
import os
import csv
import sys
#Create a path for the file
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the csv file
with open(csvpath, newline='') as csvfile:
    # read the file
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)
    csv_reader = list(csvreader)
    rowcount = int(len(csv_reader))

    #List of candidates who received votes
    uniq_list=[]
    candidates=[]
    for row in csv_reader:
        candidates.append(str(row[2]))
        if row[2] not in uniq_list:
            uniq_list.append(row[2])
        else:
            continue

    # Calculate Total number of votes for each candidate
    candidate1 = candidates.count(uniq_list[0])
    candidate2 = candidates.count(uniq_list[1])
    candidate3 = candidates.count(uniq_list[2])
    candidate4 = candidates.count(uniq_list[3])

    # Listing total values of each candidate to find max canidate index
    max_vote = [candidate1, candidate2, candidate3, candidate4]
    winner_index = max_vote.index(max(max_vote))

    # Calculate % share of each candidate from total number of votes.
    can1_percent = float(candidate1/ rowcount)
    can2_percent = float(candidate2/ rowcount)
    can3_percent = float(candidate3/ rowcount)
    can4_percent = float(candidate4/ rowcount)

    #Printing out the results
    #sys.stdout= open('output.txt', 'w')
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {rowcount}")
    print("-------------------------")
    print( uniq_list[0] +": " + "{:.2%}".format(can1_percent) +" ("+str(candidate1)+")")
    print( uniq_list[1] +": " + "{:.2%}".format(can2_percent)  +" ("+str(candidate2)+")")
    print( uniq_list[2] +": " + "{:.2%}".format(can3_percent) +" ("+str(candidate3)+")")
    print( uniq_list[3] +": " + "{:.2%}".format(can4_percent)  +" ("+str(candidate4)+")")
    print("-------------------------")
    print("Winner: " + uniq_list[winner_index])
    print("-------------------------")











