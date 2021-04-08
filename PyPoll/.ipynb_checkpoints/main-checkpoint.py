#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Import Modules
import os
import csv
from collections import OrderedDict
from collections import Counter


# In[2]:


# Designate File Path
path = "./"
csv_path = os.path.join(path, "Resources", "election_data.csv")


# In[3]:


#initialize dictionaries
dictVotes = OrderedDict()


# In[4]:


# Read and write CSV into dictionary
with open(csv_path) as csvfile:
    election = csv.reader(csvfile,delimiter=",")
    next(election)   #skips the header row of csv file
    for row in election:
        ID = str(row[0])
        County = str(row[1])
        Candidate = str(row[2])
        dictVotes[ID] = [County,Candidate]


# In[68]:


# Count the number of votes cast
outputVotes = len(dictVotes.keys())
print("Election Results")
print(f'Total Votes: {outputVotes}')


# In[65]:


# List of candidates who received votes
candidateList = []
candidateAggregate = []
candidateVotesList = list(dictVotes.items())

for rows in range(outputVotes):
    candidateName = candidateVotesList[rows][1][1]
    candidateAggregate.append(candidateName)
    if candidateName not in candidateList:
        candidateList.append(candidateName)        


# In[64]:


# The percentage of votes each candidate won
candidateCount = Counter(candidateAggregate)
candidatePercentDict = {}
for names in candidateList:
    candidatePercent = candidateCount[names] / outputVotes
    candidatePercentDict[names] = candidatePercent
    print(f'{names}: {round(candidatePercent*100,1)}% ({candidateCount[names]}) ')


# In[54]:


# The winner of the election based on popular vote
winnerName = "none"
winnerPercent = 0
for name in candidateList:
    if candidatePercentDict[name] > winnerPercent:
        winnerName = name
        winnerPercent = candidatePercentDict[name]
        
print(f'Winner: {winnerName}')


# In[75]:


# Output data analysis to text file in Analysis Folder
output_path = os.path.join(".", "Analysis", "Analysis.txt")

with open(output_path, 'w') as a_writer:
    a_writer.write("Election Results"+"\n")
    a_writer.write("-------------------------"+"\n")
    a_writer.write(f'Total Votes: {outputVotes}'+"\n")
    a_writer.write("-------------------------"+"\n")
    for name in candidateList:
        a_writer.write(f'{name}: {round(candidatePercentDict[name]*100,2)}% ({candidateCount[name]})'+"\n")
    a_writer.write("-------------------------"+"\n")
    a_writer.write(f'Winner: {winnerName}'+"\n")
    a_writer.write("-------------------------"+"\n")


# In[ ]:




