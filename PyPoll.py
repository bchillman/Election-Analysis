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

#Open results and read file
with open(file_to_load, 'r') as election_data:

    #To-do: perform analysis
    print(election_data)

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Desktop","Bootcamp","Module 3 - Python - PyPoll","Election-Analysis","Analysis","election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Araphoe\nDenver\nJefferson")

# To do: Read and analyze the data here.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        
       
        print(row)

