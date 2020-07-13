# python-challenge

## Tasks

There are two different challenges. Each has its own script, source file and results file.

### Challenge 1 - PyBank

This challenge entailed analyzing financial data to calculate the total number of months included in the dataset, the net total amount of profits/losses over the entire period, the average of the changes in profits/losses over that period, the greatest increase in profits over that period, and the greatest decrease in losses over the period. The results will be displayed in the terminal window as well as in a text file called analysis.txt.  

#### Files

* [PyBank Script](PyBank/main.py) - running this file will produce results in the terminal window and in a text file
* [Financial Data](PyBank/Resources/budget_data.csv) - this is the data file to be analyzed
* [Analysis Results](PyBank/analysis/analysis.txt) - this file holds the results from runinng the script - this file is created automatically or is overwritten if the file already exists


### Challenge 2 - PyPoll

This challenge dealt with analyzing poll data to calculate the total number of votes cast, the complete iist of all candidates and each of their percentage of votes won along with the total number of votes they received. The winner was also determined based on popular vote. The results will be displayed in the terminal window as well as in a text file called analysis.txt.  

#### Files

* [PyPoll Script](PyPoll/main.py) - running this file will produce results in the terminal window and in a text file
* [Financial Data](PyPoll/Resources/election_data.csv) - this is the data file to be analyzed
* [Analysis Results](PyPoll/analysis/analysis.txt) - this file holds the results from runinng the script - this file is created automatically or is overwritten if the file already exists

## Notes

The analysis.txt file (results file) created for each challenge is included here for thoroughness but it should be generated on its own each time the script is run. This file can be found in the analysis folder. The data source files are located in the Resources folder. The script files are located in their PyBank or PyPoll folder, respectively, not in their Resources folder.

