#Add our dependencies
import csv
import os

# Assign a variable to load the file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save= os.path.join("analysis", "election_analysis.txt")

#Open the election results and read file
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader= csv.reader(election_data)

    #Print the header row
    headers=next(file_reader)
    print(headers)



#Count the total number of votes received
#List each candidate who received at least one vote
#Count votes per candidate
#Calculate percentage per candidate
#Figure candidate with highest percentage



#with open (file_to_save, "w") as txt_file:

    #Write some data to the file
    #txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")


