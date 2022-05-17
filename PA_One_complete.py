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


"Program menu"      
def print_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Whole US Data")
    print ("2. Data for a specified US State")
    print ("3. Exit")
    print (67 * "-")
"Displays program menu"
print_menu()



def option1():
    #reading csv file
    with open(mask_use_edited, 'r') as csvfile:
    #creating a csv reader object
        csvreader = csv.reader(csvfile)
    # extracting field names through first row
        fieldsedit = next(csvreader)
    # extracting each data row one by one
        for row in csvreader:
            rowsedit.append(row)
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
    print(rowsedit)
#Ask the user to choose again
choice = input("Enter your choice new [1-3]: ")
"Convert string to int type"
choice = int(choice)

def option2():
    #get the specific state from user input
    stateinput = input('Enter the state name you which to print the data from? e.g: NY or AL: ')
    #check if users input is in csv file
    #reading csv file
    with open(state_abb, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fieldsstate = next(csvreader)
        print(fieldsstate)
        for row in csvreader:
            rowsstate.append(row)
            if (row[1] == stateinput):
                print(stateinput)
                break #break the for loop when the correct valu is found

    #check if users input is in csv file
    #reading csv file        
    with open(mask_use_edited, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fieldsedit = next(csvreader)
        for row in csvreader:
            rowsedit.append(row)
            #Print rows that mathces user input
            if row[8] == stateinput: #check that use enterec abbreviations
                   print(row)
                
        #Ask the user to choose again
        choice = input("Enter your choice new [1-3]: ")
        "Convert string to int type"
        choice = int(choice)
   


"while loop for program"
while(True):
    if choice == 1:
         print ("Menu 1 has been selected")
         option1()# output the entire file with edited data
        
    elif choice == 2:
        option2() #output the file according the specific data needed
                
        #Ask the user to choose again
        choice = input("Enter your choice new [1-3]: ")
        "Convert string to int type"
        choice = int(choice)

    elif choice == 3:
        print("Menu 3 has been selected")
        i = False
        "function to exit program"
        print("Thanks for using this program")
        exit()
        
    elif choice > 3:
        print("Invalid number. Try again...")
        #Ask the user to choose again
        choice = input("Enter your choice new [1-3]: ")
        "Convert string to int type"
        choice = int(choice)
