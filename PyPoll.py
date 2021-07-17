#Add our dependencies
import csv
import os

# Assign a variable to load the file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save= os.path.join("analysis", "election_analysis.txt")

#Initialize Total vote counter
total_votes=0

#Initialize Candidate Options List and candidate votes
candidate_options=[]
candidate_votes={}

#Winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

#Open the election results and read file
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)

    #Read the header row
    headers=next(file_reader)

    #Read each row in the CSV File
    for row in file_reader:
        #Add to the total vote count
        total_votes+= 1

        #Print the candidate name from each row
        candidate_name= row[2]


        #Add the candidate name to the candidate list if not already in list
        if candidate_name not in candidate_options:
           #Add to the list of candidates
           candidate_options.append(candidate_name)

           #Begin to track candidate vote count
           candidate_votes[candidate_name]=0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

    #Save the results to our text file    
    with open(file_to_save, "w") as txt_file:
        election_results= (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")

        # Save the final vote count to the text file.
        txt_file.write(election_results) 

        #determine the percentage of each vote for each candidate
        #Iterate through candidate list
        for candidate_name in candidate_votes:
            #Retrieve vote count of a candidate
            votes=candidate_votes[candidate_name]
            #Calculate the percentage of votes
            vote_percentage=float(votes)/float(total_votes) * 100

            #Print out each candidates name, vote count, and percentage of votes to the terminal
            Candidate_results= (f'{candidate_name} : {vote_percentage:.1f}% ({votes:,})\n')
            #Print each candidate, their vote count and percent to terminal
            print(Candidate_results)
            #Save the candidate result to text file
            txt_file.write(Candidate_results)

            #Determine winning vote count and candidate
            #Determine if the votes is greater than the winning count
            if (votes>winning_count) and (vote_percentage > winning_percentage):
                #If true then set winning_count=votes and winning_percentage=vote_percentage
                winning_count=votes
                winning_percentage=vote_percentage
                #Set winning candidate equal to the candidate name
                winning_candidate=candidate_name
        #Print out winning candidate, vote count and percentage to terminal
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        print(winning_candidate_summary)
        
        #Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)
    

#Print candidate names
#print(candidate_votes)



#Count the total number of votes received
#List each candidate who received at least one vote
#Count votes per candidate
#Calculate percentage per candidate
#Figure candidate with highest percentage



#with open (file_to_save, "w") as txt_file:

    #Write some data to the file
    #txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")


