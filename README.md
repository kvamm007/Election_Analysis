# Election_Analysis

## Overview
The Colorado Board of Elections was looking to complete an audit of a recent local election for congress. The following steps were used to complete the audit:
1. Calculate the total number of votes cast in the election.
2. Get a list containing the name of each candidate who received at least one vote.
3. Get a list containing the name of each county in which at least one vote was cast.
4. Calculate the total number of votes that each candidate (step 2.) received in the election.
5. Calculate the total number of votes that each county (step 3.) cast in the election 
6. Calculate the percentage that each candidate (step 2.) received of the total votes cast.
7. Calculate the percentage that each county (step 3.) cast of the total votes cast.
8. Determine the county with the highest voter turnout (based on step 5.)
9. Determine the winner based on the highest percentage and highest count of popular vote received (based on step 4. and step 6.) 

## Resources
Data source = election_results.csv provided by Colorado Board of Elections

Software: Python version 3.7.6 and Visual Studio Code 1.58.2

Starter code: PyPoll_Challenge_Starter_Code provided by class module

## Summary of results
The analysis of our election results shows that there were 369,711 total votes cast in the election

### County Information
The counties in which at least one vote was cast were:
 - Jefferson County
 - Denver County
 - Arapahoe County
 
The votes cast by county were:
 - Jefferson County cast 38,855 votes or 10.5% of the total votes
 - Denver County cast 306,055 votes or 82.8% of the total votes
 - Arapahoe County cast 24,801 votes or 6.7% of the total votes

The county with the most votes cast was Denver County, with 82.8% (306,055) of the votes cast

![County Votes](https://user-images.githubusercontent.com/85597801/126078894-205cbd45-0297-4da8-8347-567f80988d0e.png)

### Candidate Information
The candidates who received at least 1 vote were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

The results by candidate were:
  - Charles Casper Stockham received 85,213 votes, or 23.0% of the total votes cast
  - Diana DeGette received 272,892 votes, or 73.8% of the total votes cast
  - Raymon Anothy Doane received 11,606 votes, or 3.1% of the total votes cast

The winner of the election was:
  - Diana DeGette with 272,892 votes, or 73.1% of the total votes

![Candidate Votes](https://user-images.githubusercontent.com/85597801/126078898-19ba2add-5225-4e9c-a4f2-be9bcf49d604.png)


## Potential Modification to Script
Personally I prefer more spacing and to make it visually easier to scan the results in the text file or terminal output. Here are the tweaks I would make:
```
  election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
```
I would add an additional line separator to mark out the section showing “County Results” as follows:
```
  election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
        f"*************************\n")
```
I would add the same * border over the candidate results. I would also extend the length of some of the dividers so that they extend beyond the end of the text. 


Original: ![Original Results](https://user-images.githubusercontent.com/85597801/126078914-bdb915d2-f003-4a1d-8fab-e4d8b35a3ba9.png)

Reformatted:![Reformatted Results](https://user-images.githubusercontent.com/85597801/126078919-a04c4c06-94e2-4f6e-9f1d-fcf263e880d3.png)


I have saved the reformatted script, if that is preferred to the original format, as “reformatted.py”, also available in the repository. 

## How to use script for additional elections
In general, this script is very flexible, in that we did not hard code any of the candidate names or county names, everything is set to pull out of the CSV file. 
1. This formatting will all work correctly to read any elections results as long as the following are true:
   - The results contain 3 columns, with the 2nd column being “County” and the 3rd column being “candidate”. The 1st column is not referenced.
   - The file is saved in a folder that also contains subfolders:
     -  “Resources”, which contains the election results CSV file
     -  “Analysis” folder which will be populated with the final text file. 
2.	If the candidate name is in a different column simply alter the following script:
```
  candidate_name = row[2]
```
Change the [2] to whichever column the candidate name is in, with A being 0- for example, if the candidate name is in column “E” change to 

```
  candidate_name = row[4]
```
3.	Similarly, if the county name is in a different column, simply alter the following script:
```
  county_name=row[1]
```
Change the [1] to whichever column the county name is in, with A being 0- for example, if the county name is in column “H” change to
```
  county_name=row[7]
```
