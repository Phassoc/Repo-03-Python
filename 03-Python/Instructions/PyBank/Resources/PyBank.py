# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Establish dataframe(s) csvinput and csvout..
csvinput = os.path.join('..', 'Resources', 'budget_data.csv')
csvout  = os.path.join('..', 'Resources', 'budget_analysis.txt')

Total_Months = 0
Total_PL = 0
Prev_PL = 0
Curr_PL = 0
PandLChange = 0
zero_val = 0

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

PandLChanges = []

# read the input..

with open(csvinput, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    first_row = next(csvreader)
    Total_Months = Total_Months + 1
    Total_PL = Total_PL + int(first_row[1])
    Prev_PL = int(first_row[1])

    # Read each row of data after the header
    for row in csvreader:

        Total_Months = Total_Months + 1
        Total_PL = Total_PL + int(row[1])
        PandLChange = int(row[1]) - Prev_PL
        Prev_PL = int(row[1])
        
        # Determine the greatest increase and decrease in profits...
        if (PandLChange > greatest_increase[1]):
            greatest_increase[1] = PandLChange 
            greatest_increase[0] = row[0]

        if (PandLChange < greatest_decrease[1]):
            greatest_decrease[1] = PandLChange
            greatest_decrease[0] = row[0]

        #PandLChanges.append(int(row[1]))
        PandLChanges.append(PandLChange)
    
    print (sum(PandLChanges))
    print (len(PandLChanges))

    PandLAvgChg = (round(PandLChange) / len(PandLChanges))
    PandLAvg = sum(PandLChanges) / len(PandLChanges)

# Print to the terminal..
    print ("  ")
    print ("Financial Analysis")
    print ("----------------------------")
    print ("Total Months: " + str(Total_Months))
    print ("Total P & L : " + "$"+ str(Total_PL))
    print ("Average Change: " + "$" + str(round(sum(PandLChanges) / len(PandLChanges),2)))
    print ("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print ("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")") 
    

# Write the output file..
with open(csvout, "w") as out_file:
    out_file.write("Total Months: " + str(Total_Months))
    out_file.write("\n")
    out_file.write("Total P & L: " + "$" + str(Total_PL))
    out_file.write("\n")
    out_file.write("Average Change: " + "$" + str(round(sum(PandLChanges) / len(PandLChanges),2)))
    out_file.write("\n")
    out_file.write("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    out_file.write("\n")
    out_file.write("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

    
