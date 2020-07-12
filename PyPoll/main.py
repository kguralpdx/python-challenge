# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources', "election_data.csv")

# open the dataset, skipping the first row which contains headers
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    csv_header = next(reader)

    vote_count = {}
    current_vote = 0
    tally = 0
    winner_votes = 0

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

    # get the winner by looping through the vote_count dictionary to compare vote totals and tben top vote getter into a new dictionary
    # Got help from https://realpython.com/iterate-through-dictionary-python/#a-few-words-on-dictionaries
    top_vote_getter = {}
    for key, value in vote_count.items():
        if value > winner_votes:
            winner_votes = value
            winner = key

#winner = max(vote_count, key=vote_count.get)  

print("Election Results")
print("-----------------------------")
print(f"Total Votes:  {tally}")
print("-----------------------------")
for key, value in vote_count.items(): # got help with this from https://realpython.com/iterate-through-dictionary-python/#a-few-words-on-dictionaries
    print(f"{key}:  ({value})")
print("-----------------------------")
print(f"Winner:  {winner}")
#print(winner)
# need to get
# total number of votes
# complete list of candidates who received votes
# percentage of votes each candidate received
# total number of votes each candidate received
# winner of the election based on popular vote
# 
  