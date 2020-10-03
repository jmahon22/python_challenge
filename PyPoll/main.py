import os
import csv
electiondata_csv = os.path.join("Resources", "election_data.csv")

TotalVotes=0


#open and read csv
with open(electiondata_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#read the header row first
    csv_header = next(csv_reader)

    for row in csv_reader:  
#total number of votes cast
        electiondata_csv = {'voter id':}
#list of candidates who received votes

#percentage of votes each candidate won

#total number of votes each candidate won

#Winner of the election based on popular vote