# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources', "election_data.csv")

# open the dataset, skipping the first row which contains headers
with open(csvpath, encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    csv_header = next(reader)

    # create the dictionary and set the count variables to 0
    vote_count = {}
    current_vote = 0
    tally = 0

    # loop through the rows in the file
    # the candidate totals and the try/except parts were from Terra's after office hours session
    for row in reader:

        # count total number of votes
        tally += 1

        # Store candidate name
        candidate = row[2]

        # Try accessing current row's candidate and adding to their vote count
        try:
            current_vote = vote_count[candidate] + 1
            vote_count[candidate] = current_vote
        
        # If unsuccessful, it's the candidate's first vote.
        except:
            vote_count[candidate] = 1

# define the function to get the percentage of votes per candidate, the parameter is a dictionary
def percent_of_votes(v):
    for key in v:
        vote_percent = (v[key]/tally) * 100
        print(f"{key}:  {round(vote_percent)}.000%  ({v[key]})")


# get the winner by looping through the vote_count dictionary to compare vote totals
# Got help from https://realpython.com/iterate-through-dictionary-python/#a-few-words-on-dictionaries
winner_votes = 0

for key, value in vote_count.items():
    if value > winner_votes:
        winner_votes = value
        winner = key

# Set variable for output file
output_file = os.path.join("analysis", "analysis.txt")

#  Open the output file and populate it with results
with open(output_file, "w") as datafile:
    datafile.write("Election Results \n")
    datafile.write("-----------------------------\n")
    datafile.write("Total Votes:  " + str(tally) + "\n")
    datafile.write("-----------------------------\n")
    for key, value in vote_count.items(): # got help from https://www.quora.com/How-do-I-write-a-dictionary-to-a-file-in-Python for the candidate stats portion
        percent_votes = (int(value)/tally) * 100
        percent_votes = round(percent_votes) # rounding didn't work on the line above so added separate line to do that
        datafile.write('%s:  %d.000%% (%s)\n' % (key, percent_votes, value))
    datafile.write("-----------------------------\n")
    datafile.write("Winner:  " + winner + "\n")
    datafile.write("-----------------------------\n")


# Display the results in the Terminal
print("Election Results")
print("-----------------------------")
print(f"Total Votes:  {tally}")
print("-----------------------------")
percent_of_votes(vote_count)
print("-----------------------------")
print(f"Winner:  {winner}")
print("-----------------------------")