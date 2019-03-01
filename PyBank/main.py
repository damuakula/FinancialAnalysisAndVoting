import os
import csv

# Set the csv path and file name        
csvpath = os.path.join('.','budget_data.csv')

# Read in the CSV file
with open(csvpath, newline = '') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the first header row
    next(csvreader)

    totalMonths = 0
    netProfitLossTotal = 0.00
    avgProfitLossChanges = 0.00
    avgProfitLossTotal = 0.00
    greatestIncrease = 0.00
    greatestDecrease = 0.00
    itemList = []
    dateList = []
    
    # Loop through the csv file to get the months list, dates list, total months, and total profit & loss numbers
    for row in csvreader:
        totalMonths = totalMonths + 1
        netProfitLossTotal = netProfitLossTotal + float(row[1])
        itemList.append(float(row[1]))
        dateList.append(row[0])
    
    # Loop through to calculate the net change of profit/loss numbers to get the average net change
    # The change in price will be next month's price minus the current price. Add up all these changes
    # and take the average of these changes.
    itemNbr = 0
    for item in itemList:
        if itemNbr < totalMonths-1:
          avgProfitLossChange = itemList[itemNbr+1] - itemList[itemNbr]
          itemNbr = itemNbr + 1
          avgProfitLossTotal = avgProfitLossTotal + avgProfitLossChange
    
        # Calculate the average change in profits/losses
    avgProfitLossChanges = avgProfitLossTotal/(totalMonths-1)

    # Calculate the greatest increase in profits
    greatestIncrease = max(itemList)

    # Calculate the greatest derease in profits
    greatestDecrease = min(itemList)

    i = itemList.index(greatestIncrease)
    j = itemList.index(greatestDecrease)

    # Print the output with numbers to the terminal
    print("Total Months: " + str(totalMonths))
    print("Net Profit Loss Total: " + str(netProfitLossTotal))
    print("Average Change: " + str(round(avgProfitLossChanges,2)))
    print("Greatest increase in profits: " + dateList[i] + " ($" + str(greatestIncrease) + ")")
    print("Greatest decrease in profits: " + dateList[j] + " ($" + str(greatestDecrease) + ")")

    # Set the output text file path and file name
    output_path = os.path.join('.','.','budget_data_out.txt')
    # Print the output with numbers to the text file
    with open(output_path,'w',newline='\n') as txtfile:
       txtfile.write("Total Months: " + str(totalMonths))
       txtfile.write('\n')
       txtfile.write("Net Profit Loss Total: " + str(netProfitLossTotal))
       txtfile.write('\n')
       txtfile.write("Average Change: " + str(round(avgProfitLossChanges,2)))
       txtfile.write('\n')
       txtfile.write("Greatest increase in profits: " + dateList[i] + " ($" + str(greatestIncrease) + ")")
       txtfile.write('\n')
       txtfile.write("Greatest decrease in profits: " + dateList[j] + " ($" + str(greatestDecrease) + ")")
       txtfile.write('\n')

    # Close the text file
    txtfile.close()
    # Close the csv file
    csvfile.close()