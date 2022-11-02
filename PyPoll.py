# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Load csv file

import csv
import os

#Assign a variable for the file to load and the path 
file_to_load = os.path.join("Desktop","Bootcamp","Module 3 - Python - PyPoll","Election-Analysis","Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Desktop","Bootcamp","Module 3 - Python - PyPoll","Election-Analysis","Analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Initialize a candidate list
candidate_options = []

# Initialzie candidate vote count as dictionary
candidate_votes = {}

# Initialize winning variables 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        
        # add to vote counter
        total_votes += 1 

        # Find candidate name from each row
        candidate_name = row[2]

        # If candidate hasn't been seen yet
        if candidate_name not in candidate_options:
            
            # Add candidate's name to candidate list
            candidate_options.append(candidate_name)

            # Begin counting candidate votes
            candidate_votes[candidate_name] = 0
        
        # Add a vote for given candidate
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percent = (votes/total_votes) * 100
    
    # Determine if vote count is larger than winning_count
    if votes > winning_count:
        
        # set winning_count to the higher value
        winning_count = votes

        # set winning_candidate to current candidate
        winning_candidate = candidate_name

        # set winning_percentage to this candidate's percentage
        winning_percentage = vote_percent

    print(f'{candidate_name}: {vote_percent:.1f}% ({votes:,})\n')
    
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n"
)
print(winning_candidate_summary)