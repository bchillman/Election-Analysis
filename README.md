# Election-Analysis

## Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate received.
5. Determine the winner of the election based on popular vote.
6. Caluclate the total number of votes in each county.
7. Determine the the county with the largest number of votes.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.7, Visual Studio Code 1.72.2

## Election-Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote (85,213 votes)
  - Diana DeGette received 73.8% of the vote (272,892 votes)
  - Raymon Anthony Doane received 3.1% of the vote(11,606 votes)
 - The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote (272,892 votes)
-The County results were
  - Jefferson County: 10.5% of the voters (38,855 voters)
  - Denver County: 82.8% of the voters (306,055 voters)
  - Arapahoe County 6.7% of the voters (24,801 voters
 - The county with the most voters was:
  - Denver County, which had 82.8% of the voters (306,055 voters)
  
## Election-Audit Summary
### General Use
This script can be used for any election. It takes votes from a csv file, and reads the number of votes for each candidate as well as the number of votes from each county. This script can be used for any election, as it reads the candidates and counties from the file and doesn't need any prior information about the election. This is done with the following section of code:
![code-1](https://github.com/bchillman/Election-Analysis/blob/main/Resources/code-1.png)

Here, if the candidate is not already in the list of candidates, they are added to the list, which allows us to not input any prior information. Similar code is used for the counties. Thus, by just making sure that the file is pathed to correctly, the script will read the number of votes for each candidate and county. This allows it to be used for any election. 
### Modifications
There may need to be some modifications to be used for other elections. First, currently the numbers of votes for a candidate and the number of votes in a county are seperate. These could be combined for useful information about how many votes there are for each candidate in each county. This can be done by combining, or nesting, the *if* functions that are used to count votes for candidates or counties, respectively. Second, as mentioned above, the pathing to and reading of the results file may need to be changed. If the file is a csv file, then it needs to be made sure that the following line of code correctly paths to the file:
![code-2](https://github.com/bchillman/Election-Analysis/blob/main/Resources/code-2.PNG)

If the file is not a csv file, then it needs to be correctly read. The script currently uses the *csv.reader* function to read the file, and a different function will likely need to be used.
