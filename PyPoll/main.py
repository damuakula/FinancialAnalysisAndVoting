import os
import csv
import collections

# Set the csv path and file name        
csvpath = os.path.join('.','election_data.csv')

# Read in the CSV file
with open(csvpath, newline = '') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the first header row
    next(csvreader)

    totalVotes = 0
    totalCandidates = 0
    totalPerCandidate = 0
    percentPerCandidate = 0
    winningCandidate = ""

    candidateList = []
    candidatesGroup = {}
    
    candidatesGroup = collections.defaultdict(list)
    # Loop through the csv file to get the total votes, candidate list
    for row in csvreader:
        totalVotes = totalVotes + 1
        candidateList.append(row[2])
        candidateGroup = row[2]
        value = row[0]
        candidatesGroup[candidateGroup].append(value)
    
    # Select the unique candidate list
    uniqueCandidates = set(candidateList)

    # Print the output with numbers to the terminal
    print("Election Results")
    print("----------------------------")
    print("The list of candidates:")
    print("----------------------------")
    
    for i in uniqueCandidates:
       print(str(i))

    print("----------------------------")
    print("Total Votes Cast: " + str(totalVotes))
    print("----------------------------")

    j=0
    for key, values in candidatesGroup.items():
       #print(key,values)
       i=0
       for votes in values:
          i = i + 1
       print(key + ":" + str(round((i/totalVotes)*100,2)) + "% (" + str(i) + ")")
       if (i > j):
           winner = key
           j=i
       else:
           j=i
          
    print("----------------------------")
    print("Winner: " + winner)

    # Set the output text file path and file name
    output_path = os.path.join('.','.','election_data_out.txt')
    # Print the output with numbers to the text file
    with open(output_path,'w',newline='\n') as txtfile:
       txtfile.write("Election Results")
       txtfile.write('\n')
       txtfile.write("----------------------------")
       txtfile.write('\n')
       txtfile.write("The list of candidates:")
       txtfile.write('\n')
       txtfile.write("----------------------------")
       txtfile.write('\n')
       for i in uniqueCandidates:
           txtfile.write(str(i))
           txtfile.write('\n') 
       txtfile.write("----------------------------")
       txtfile.write('\n')
       txtfile.write("Total Votes: " + str(totalVotes))
       txtfile.write('\n')
       txtfile.write("----------------------------")
       txtfile.write('\n')
       for key, values in candidatesGroup.items():
         i=0
         for votes in values:
            i = i + 1
         txtfile.write(key + ":" + str(round((i/totalVotes)*100,2)) + "% (" + str(i) + ")")
         txtfile.write('\n')
       txtfile.write("----------------------------")
       txtfile.write('\n')
       txtfile.write("Winner: " + winner)
     
    # Close the text file
    txtfile.close()
    # Close the csv file
    csvfile.close()