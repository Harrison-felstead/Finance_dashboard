
__author__ = 'Harrison Felstead'
__version__ = '0.1.0'

"""
This is the module that finds the corrosponding catagory reference for a given transaction
"""
import csv
import os

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
            self.catagories.pop(0) #Removes the first and second lines of the csv file as it is just the headers

        with open('Catagory_list.csv', 'r') as file:
            reader = csv.reader(file)
            self.catagory_list = list(reader) 
            self.catagory_list.pop(0) 

            #Removes the first and second lines of the csv file as it is just the headers
            #This is an array of arrays, the first value in the subarray being the catagory 
            #reference and the following elements being sub catagories within the catagory

    def findCatagory(self, reference) -> str:
        '''
        This outputs the catagory of the transaction location string inputed into the function
        '''

        for i in range(len(self.catagories)): #Goes through the whole list of catagories
            if self.catagories[i][0] == reference: #If the reference is found in the list of catagories 
                return self.catagories[i][1] #Returns the catagory reference
        value = self.new_catagory(reference) #This calls a function that allows the user to add a new catagory to the csv file
        return value

    def new_catagory(reference) -> None:
        os.system("cls") #This clears the screen
        #This is where the user can add a new catagory to the csv file
        for row in range(len(self.catagory_list)):
            print(self.catagory_list[row][0])
        print("To create a new main catagory, type {}".format(len(self.catagory_list +1)))

        while type(catagory_variable) != int and int <= (len(self.catagory_list)) +1): #Only accepts integers 
            catagory_variable = input("The transaction of {} is unknown, please select which catagory index from above it belongs to".format(reference))

        os.system("cls") #This clears the screen

        if catagory_variable == len(self.catagory_list +1):
            #This is where the user can add a new catagory to the csv file
            new_catagory = input("Please enter the new catagory")
            self.catagory_list.append(new_catagory)
            self.catagories.append(reference, new_catagory, None)
        
    def findSubcatagory(self, reference) -> str:
        '''
        This outputs the subcatagory of the transaction location string inputed into the function
        '''

        for i in range(len(self.catagories)): #Goes through the whole list of catagories
            if self.catagories[i][0] == reference:
                return self.catagories[i][2] #Returns the subcatagory reference
        value = self.new_subcatagory(reference) #This calls a function that allows the user to add a new subcatagory to the csv file
        return value
    
    def new_subcatagory(self, reference) -> None:
        os.system("cls") #This clears the screen 
        reference_catagory = self.findCatagory(reference) #Finds the catagory reference of the transaction
        for row in range(len(self.catagory_list)):
            if self.catagory_list[row][0] == reference_catagory:
                for i in range(len(self.catagory_list[row])):
                    print(self.catagory_list[row][i]) #This prints all the subcatagories within the catagory
                break #This is to stop the loop from printing the whole list of subcatagories

        print("To create a new subcatagory, type {}".format(len(self.catagory_list +1))
              
        while type(subcatagory_variable) != int and int <= (len(self.catagory_list)) +1): #Only accepts integers 
            `subcatagory_variable = input("The transaction of {} is unknown, please select which subcatagory index from above it belongs to".format(reference))

        if subcatagory_variable == len(self.catagory_list +1):
            #This is where the user can add a new subcatagory to the csv file
            new_subcatagory = input("Please enter the new subcatagory")
            self.catagory_list[catagory_variable].append(new_subcatagory)
            self.catagories[reference].append(new_subcatagory) #This adds the new subcatagory to the catagory reference
        else:
            self.catagories[reference].append(self.catagory_list[row][subcatagory_variable])
            #This adds the pre-existing subcatagory to the catagory[reference], since the for loop breaks, 
            #the row variable is still the same as it was when the loop broke 


    ####Unsure what I would need to do to be able to push any updates to the csv file####
        
            
