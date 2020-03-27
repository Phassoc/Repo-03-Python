# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

from collections import OrderedDict
from operator import itemgetter

input_file  = os.path.join('..', 'Resources', 'election_data.csv')
output_file = os.path.join('..', 'Resources', 'election_analysis.txt')

votes = 0
winner_votes = 0
greatest_votes = ["", 0]
candidate_list = []
candidate_vote_dict = {}

with open(input_file) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

        votes = votes + 1     

        if row["Candidate"] not in candidate_list:
            
            candidate_list.append(row["Candidate"])

            candidate_vote_dict[row["Candidate"]] = 1
            
        else:
            candidate_vote_dict[row["Candidate"]] = candidate_vote_dict[row["Candidate"]] + 1
    
    # print(candidate_vote_dict)
    # print(candidate_list)
    
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")

# open and write initial output file records..

with open(output_file, "w") as out_file:
    out_file.write("Election Results")
    out_file.write("\n")
    out_file.write("-------------------------")
    out_file.write("\n")
    out_file.write("Total Votes " + str(votes))
    out_file.write("\n")
    out_file.write("-------------------------") 
    out_file.write("\n")

# print the summary results to the terminal and output file...

    for candidate in candidate_vote_dict:

        print(candidate + " " + str(round(((candidate_vote_dict[candidate]/votes)*100))) 
        + "%" + " (" + str(candidate_vote_dict[candidate]) + ")") 

        out_file.write(candidate + " " + str(round(((candidate_vote_dict[candidate]/votes)*100))) 
        + "%" + " (" + str(candidate_vote_dict[candidate]) + ")") 
        out_file.write("\n")

        candidate_results = (candidate + " " + str(round(((candidate_vote_dict[candidate]/votes)*100))) 
        + "%" + " (" + str(candidate_vote_dict[candidate]) + ")") 
    
    winner = sorted(candidate_vote_dict.items(), key=itemgetter(1), reverse=True)[0]

    # print (winner)
    # print more results...
    print("-------------------------")
    print("Winner: " + str(winner[0]))
    print("-------------------------")

# write winner string info to the output file..

    out_file.write("-------------------------") 
    out_file.write("\n")
    out_file.write("Winner: " + str(winner[0])) 
    out_file.write("\n")
    out_file.write("-------------------------")

