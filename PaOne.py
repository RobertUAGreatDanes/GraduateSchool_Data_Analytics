# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:26:38 2021

@author: rmorn
"""

"Open csv files"
import csv

"Open  state abbreviations csv file"
with open('C:/Users/rmorn/OneDrive/Desktop/INF505/PA1/State_Abbreviations.csv', 'r') as file:
    reader1 = csv.reader(file)
    "for row in reader:"
    "print(row)"
        
"Open  state geocodes csv file"
with open('C:/Users/rmorn/OneDrive/Desktop/INF505/PA1/State-geocodes-v2018.csv', 'r') as file:
    reader2 = csv.reader(file)
    for row in reader2:
        "print(row)"

"Open  mask use by county csv file"
with open('C:/Users/rmorn/OneDrive/Desktop/INF505/PA1/mask-use-by-county.csv', 'r') as file:
    reader3 = csv.reader(file)
    "for row in reader:"
    "print(row)"

"Open  mask use by county edited csv file"
with open('C:/Users/rmorn/OneDrive/Desktop/INF505/PA1/mask-use-by-county-Edited.csv', 'r') as file:
    reader4 = csv.reader(file)
    "for row in reader4:"
    "print(row)"

"Program menu"      
def print_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Whole US Data")
    print ("2. Data for a specified US State")
    print ("3. Exit")
    print (67 * "-")
"Displays program menu"
print_menu()

i = 0
"print(i)"
choice = input("Enter your choice [1-3]: ")
"Convert string to int type"
choice = int(choice)

"while loop for program"
while i <= 3:
    if choice == 1:     
        print ("Menu 1 has been selected")
        "Open  mask use by county edited csv file"
        with open('C:/Users/rmorn/OneDrive/Desktop/INF505/PA1/mask-use-by-county-Edited.csv', 'r') as file:
            reader4 = csv.reader(file)
            for row in reader4:
                print(row)
                break;


    elif choice == 2:
        print("Menu 2 has been selected")
        "add your code or functions here"
        state = input("Enter a specified US state (e.g: New York or California): ")
        print("User entered: " + state)
        "Open  state geocodes csv file"
        with open('C:/Users/rmorn/OneDrive/Desktop/INF505/PA1/State-geocodes-v2018.csv', 'r') as file:
            reader2 = csv.reader(file)
            for row in reader2:
                for field in row:
                    "print(row)"
                    if field == state:
                        print("State is Valid")                       
                
    elif choice == 3:
        print("Menu 3 has been selected")
        "function to exit program"
        print(exit)
        exit()
        
    elif choice > 3:
        print("Invalid number. Try again...")
        choice = input("Enter your choice [1-3]: ")
        "Convert string to int type"
        choice = int(choice)
