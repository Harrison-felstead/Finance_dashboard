
__author__ = 'Harrison Felstead'
__version__ = '0.1.0'

"""
This is the module that finds the corrosponding catagory reference for a given transaction
"""
import csv

'''
Example format of catagories.csv
Transaction reference (Who the transaction is to/from), Catagory reference (What catagory the transaction is in), 
subcatagory reference (What subcatagory the transaction is in) ==None if no subcatagory
^That would be one line in the csv file
'''


class catagorise: 
    def __init__(self):
        with open('catagories.csv', 'r') as f:
            reader = csv.reader(f)
            self.catagories = list(reader) #This is an array of arrays, each subarray is a line in the csv file
            self.catagory_list = self.catagories[1] #Cause the whole second row is just the different catagories
            self.catagories.pop(:1) #Removes the first and second lines of the csv file as it is just the headers
    
    def findCatagory(self, reference):
        for i in range(len(self.catagories)):
            if self.catagories[i][0] == reference:
                return self.catagories[i][1]
        self.new_catagory(reference)

    def new_catagory(reference):
        #This is where the user can add a new catagory to the csv file
        input("The transaction place " + reference + " is unknown, please select which catagory number",)
        
            
