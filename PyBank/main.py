#PyBank Homework

# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set variables here:
line_count = 0
total = 0
greatest_increase = 0
greatest_decrease = 0

# Lists to store Profit/Losses data
Profit_Losses = []
# may require another list for 3rd column (% change)

# Calculate average - needs to be recalculated for new list set as % change
def getAverage(Profit_Losses):
    return sum(Profit_Losses) / len(Profit_Losses)


# Open and read the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # To successfully store header row
    csv_header = next(csvfile)

    # To print header row as a check
    print(f"Header: {csv_header}")

    # Start any for loops here:
    for row in csvreader:
        if line_count == 0:
           line_count += 1

        #append only numbers from "Profit/Losses" column
        if line_count > 0:
            Profit_Losses.append(row["Profit/Losses"])

        line_count +=1

        



    # Calculate the total # of months invluded in the dataset - determine len of column 1
    # ex output: Total Months: 86
    # total_months = len(Profit_Losses)

    # Calculate the net total amount of profit/losses over the entire period - sum column 2
    # ex output: Total: $38382578
    # total = sum(Profit_Losses)

    # Calculate the changes in profit/losses over the entire period, then find the average of those changes - loop thru and create column 3, then avg column 3 output
    # ex output: Average  Change: $-2315.12
    # average_change = getAverage(change_list)

    # Locate the greatest increase in profits (date and amount) over the entire period - max from column 3
    # ex output: Greatest Increase in Profits: Feb-2012 ($1926159)
    # greatest_increase = max(change_list)
    
    # Locate the greatest decrease in losses (date and amount) over the entire period - min from column 3
    # ex output: Greatest Decrease in Profits: Sep-2013 ($-2196167)
    # greatest_decrease = min(change_list)





    # Final script should print the analysis to the terminal and export a text file with the results


    # Specify the file to write to
    #output_path = os.path.join("Analysis", "PyBank_Analysis.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    #with open(output_path, 'w', newline='') as csvfile:

        # Initialize csv.writer
        #csvwriter = csv.writer(csvfile, delimiter=',')

        # Write outputs to file
        #csvwriter.writerow(['Total Months', 86])
        #csvwriter.writerow(['Total', '$38382578'])
        #csvwriter.writerow(['Average Change', '$-2315.12'])
        #csvwriter.writerow(['Greatest Increase in Profits', 'Feb-2012', '($1926159)'])
        #csvwriter.writerow(['Greatest Decrease in Profits', 'Sep-2013', '($-2196167)'])



    



    # Loop through looking for the video
    #for row in csvreader:
        #if row[0] == video:
            #print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            # BONUS: Set variable to confirm we have found the video
            #found = True

            # BONUS: Stop at first results to avoid duplicates
            #break

    # If the video is never found, alert the user
    #if found is False:
        #print("Sorry about this, we don't seem to have what you are looking for!")
