import os
import csv
budget_csv = os.path.join("..", "Resources", "election_data.csv")
#print result to a file
outputfile = os.path.join("PyPoll Analysis.txt")
# Open and read csv
with open(budget_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
#grab header
    csvheader = next(csv_file)
    totalVotes=0
    candidates=[]
    candidateVotes={}
    winningCount=0
    winningCandidate=""
    print(f'Header: {csvheader}')
    for row in csvreader:
        totalVotes+=1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidateVotes[row[2]]=1
        else:
            candidateVotes[row[2]]+=1
    vote_output=""
    for candidate in candidateVotes:
        votes= candidateVotes.get(candidate)
        votePer=(float(votes)/float(totalVotes))*100.00
        votePer=round(votePer,3)
        vote_output+= f"{candidate}:{votePer}%\n"
        if votes>winningCount:
            winningCount=votes
            winningCandidate=candidate

winnerOutput=f"Winner: {winningCandidate}"
#output
output = f'Total Votes: = {totalVotes}\n------------------\n{vote_output}------------------\n{winnerOutput}'
print(output)
with open(outputfile,"w") as textFile:
    textFile.write(f"Election Results: \n------------------\n{output}")

 


