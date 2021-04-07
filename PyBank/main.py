#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Modules
import os
import csv
from collections import OrderedDict
from statistics import mean


# In[2]:


# Designate File Path
path = "./"
csv_path = os.path.join(path, "Resources", "budget_data.csv")


# In[3]:


# Initialize dictionary object
dictBudget = OrderedDict()


# In[4]:


# Read and write CSV into dictionary
with open(csv_path) as csvfile:
    Budget = csv.reader(csvfile,delimiter=",")
    next(Budget)   #skips the header row of csv file
    for row in Budget:
        date = str(row[0])
        profit = int(row[1])
        dictBudget[date] = profit


# In[10]:


# Total number of months in data set
monthCount = len(dictBudget.keys())
outputMonths = f"Total Months: {monthCount}"
print(outputMonths)


# In[11]:


# Calculate the total profit of data set
totalProfit = 0
for month in dictBudget.keys():
    totalProfit += dictBudget.get(month)


outputProfit = f"Total: ${totalProfit:,}"   
print(outputProfit)


# In[12]:


# Calculate the changes in Profits for the entire period, 
# then the average of those changes
changeProfit = [] #list of changes to profits from month to month
monthData = {} #maps change in profits to months
monthlyProfits = list(dictBudget.items()) #list of dictionary tuples from Budget

for month in range(monthCount - 1):
    difference = monthlyProfits[month + 1][1] - monthlyProfits[month][1]
    changeProfit.append(difference)
    monthData[difference] = monthlyProfits[month + 1][0]
    
averageChange = round(mean(changeProfit),2)
outputChange = f"Average Change: ${averageChange:}"
print(outputChange)


# In[13]:


# The greatest increase in profits (date and amount) over the entire period
outputInc = f"Greatest increase in profits: {monthData[max(changeProfit)]} ${max(changeProfit):,}"
print(outputInc)


# In[14]:


# The greatest decrease in losses (date and amount) over the entire period
outputDec = f"Greatest Decrease in profits: {monthData[min(changeProfit)]} ${min(changeProfit):,}"
print(outputDec)


# In[24]:


# Output data analysis to text file in Analysis Folder
output_path = os.path.join(".", "Analysis", "Analysis.txt")

with open(output_path, 'w') as a_writer:
    a_writer.write(outputMonths)
    a_writer.write("\n"+outputProfit)
    a_writer.write("\n"+outputChange)
    a_writer.write("\n"+outputInc)
    a_writer.write("\n"+outputDec)


# In[ ]:




