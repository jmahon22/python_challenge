import os
import csv
electiondata_csv = os.path.join("Resources", "election_data.csv")

TotalVotes=0
VoteWinner=0
Winner=0

#open and read csv
with open(electiondata_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#read the header row first
    csv_header = next(csv_reader)
#create dictionary
    CandidatesDictionary={}

    for Candidate in csv_reader:  
#total number of votes cast
        TotalVotes+=1
        Candidate=(Candidate[2])
#list of candidates who received votes
        if Candidate in CandidatesDictionary:
            CandidatesDictionary[Candidate]+=1
        else:
            CandidatesDictionary[Candidate]=1

#percentage and total votes for each candidate. Output election winner

#print to terminal, export results
output_path = os.path.join("Analysis", "PyPollResults.txt")
with open(output_path, 'w') as txtfile:

    print("Election Results", file=txtfile)
    print("Election Results")
    print("----------------------", file=txtfile)
    print("----------------------")
    print(f"Total Votes: {TotalVotes}", file=txtfile)
    print(f"Total Votes: {TotalVotes}")
    print("----------------------", file=txtfile)
    print("----------------------")
    
    for Candidate, CandidateVotes in CandidatesDictionary.items():
        VotePercentage=(round(CandidateVotes/TotalVotes*100,3))
        print(Candidate+":  " + str(VotePercentage) + "%" + " ("+str(CandidateVotes)+")", file=txtfile)
        print(Candidate+":  " + str(VotePercentage) + "%" + " ("+str(CandidateVotes)+")")

        if CandidateVotes > VoteWinner:
            VoteWinner = CandidateVotes
            Winner = Candidate
    
    print("----------------------", file=txtfile)
    print("----------------------")
    print(f"Winner: {Winner}", file=txtfile)
    print(f"Winner: {Winner}")   
    print("---------------------", file=txtfile)
    print("---------------------")
