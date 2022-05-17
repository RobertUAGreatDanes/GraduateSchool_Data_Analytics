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

stateinput = input('Enter the state data you want? e.g: New York or Alabama: ')

file = open(state_abb, 'r')
count = 0
for rows in csv.reader(file):
    #print(rows[count])
    if rows[count] == stateinput:
        count += 1
        print(count)



