# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:26:38 2021

@author: rmorn
"""

"Open csv files"
import csv

# csv file name
state_abb = "State_Abbreviations.csv"
# initializing the titles and rows list
fieldsstate = []
rowsstate = []

# csv file name
geocodes = "State-geocodes-v2018.csv"
# initializing the titles and rows list
fieldscodes = []
rowscodes = []

# csv file name
mask_use = "mask-use-by-county.csv"
# initializing the titles and rows list
fieldsuse = []
rowsuse = []

# csv file name
mask_use_edited = "mask-use-by-county-Edited.csv"
# initializing the titles and rows list
fieldsedit = []
rowsedit = []

#get the specific state from user input
stateinput = input('Enter the state name you which to print the data from? e.g: New York or Alabama: ')

#check if users input is in csv file
#reading csv file
with open(state_abb, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldsstate = next(csvreader)
    print(fieldsstate)
    for row in csvreader:
        rowsstate.append(row) 
        if row[1] == stateinput:
            print(stateinput)
            break
    else:
        print("The state is not found")
        #print("Total no. of rows: %d"%(csvreader.line_num))

with open(mask_use_edited, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldsedit = next(csvreader)
    for row in csvreader:
        rowsedit.append(row)
        #Print rows that mathces user input
        if row[8] == stateinput:
            print(row) 
            
        



