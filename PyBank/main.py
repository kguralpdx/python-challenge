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
with open(csvpath) as csvfile:
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

months
net_total
last_profit_loss = int_net_total
avg_changes = (last_profit_loss - first_profit_loss)/(months - 1)

print("Financial Analysis")
print("--------------------------")
print(f"Total Months:  {months}")
print(f"Total:  ${net_total}")
print("Average Change:  $" + "{:.2f}".format(avg_changes)) # Got formatting help from https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-30.php
print(f"Greatest Increase in Profits:  {greatest_profit_loss_list[0]} (${greatest_profit_loss_list[1]})")
print(f"Greatest Decrease in Profits:  {greatest_profit_loss_list[2]} (${greatest_profit_loss_list[3]})")