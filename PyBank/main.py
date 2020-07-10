# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data
months = []
total = []
avg_changes = []
greatest_profit_inc_date = []
greatest_profit_inc_amt = []
greatest_profit_dec_date = []
greatest_profit_dec_amt = []

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csv_header)

#     # Loop through looking for the video
#     for row in csvreader:
#         if row[0] == video:
#             print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

#             # BONUS: Set variable to confirm we have found the video
#             found = True

#             # BONUS: Stop at first results to avoid duplicates
#             break




# # Set variable for output file
# output_file = os.path.join("financial_analysis.txt")

# #  Open the output file
# with open(output_file, "w") as datafile:
#     writer = csv.writer(datafile)

#     # Write the header row
#     # writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
#     #                 "Percent of Reviews", "Length of Course"])

#     # Write in zipped rows
#     writer.writerows(cleaned_csv)