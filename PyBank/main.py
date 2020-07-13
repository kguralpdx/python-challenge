# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources', "budget_data.csv")

# set final variables to start at 0
months = 0
net_total = 0
previous_row_profit = 0
current_profit_inc = 0
current_profit_dec = 0

# Open the CSV file
with open(csvpath, encoding='utf-8') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     csv_header = next(csvreader)

     for row in csvreader:
         months += 1 #counting the number of months
         int_net_total = int(row[1]) # current row's profit/loss
         net_total += int_net_total # running total of profit/loss
         if previous_row_profit == 0:
             first_profit_loss = int(row[1])
         # Get the greatest increase/decrease in profits/losses
         if int(row[1]) - previous_row_profit > current_profit_inc:
             current_profit_inc = int(row[1]) - previous_row_profit
             current_profit_inc_month = row[0]
         if int(row[1]) - previous_row_profit < current_profit_dec:
             current_profit_dec = int(row[1]) - previous_row_profit
             current_profit_dec_month = row[0]
         previous_row_profit = int(row[1])

# populate list for greatest increase in profits and greatest decrease in losses
greatest_profit_loss_list = [current_profit_inc_month, current_profit_inc, current_profit_dec_month, current_profit_dec]

# get the final profit/loss and calculate the average change
last_profit_loss = int_net_total
avg_changes = (last_profit_loss - first_profit_loss)/(months - 1)

# Set variable for the output file
output_file = os.path.join("analysis", "analysis.txt")

#  Open the output file and populate it with results
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis \n")
    datafile.write("-----------------------------\n")
    datafile.write("Total Months:  " + str(months) + "\n")
    datafile.write("Total:  $" + str(net_total) + "\n")
    datafile.write("Average Change:  $" + str(round(avg_changes, 2)) + "\n")
    datafile.write(f"Greatest Increase in Profits:  {greatest_profit_loss_list[0]} (${greatest_profit_loss_list[1]}) \n")
    datafile.write(f"Greatest Decrease in Profits:  {greatest_profit_loss_list[2]} (${greatest_profit_loss_list[3]}) \n")


# Display the results in the Terminal
print("Financial Analysis")
print("--------------------------")
print(f"Total Months:  {months}")
print(f"Total:  ${net_total}")
print("Average Change:  $" + str(round(avg_changes, 2)))
print(f"Greatest Increase in Profits:  {greatest_profit_loss_list[0]} (${greatest_profit_loss_list[1]})")
print(f"Greatest Decrease in Profits:  {greatest_profit_loss_list[2]} (${greatest_profit_loss_list[3]})")