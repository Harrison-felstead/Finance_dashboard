
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

    def remove_catagory(self, catagory_removed, catagory_new_name = None) -> None:

        try: 
            for index in len(range(self.catagories)):
                #This finds the index where catagory_removed is within the catagory_list
                if self.all_catagories[i][0] == catagory_removed:
                    break
            ValueError
        except ValueError:
            #This runs if the catagory removed is not within the catagory list 
            return ValueError, "The index put into remove catagory isn't within the list"

        if catagory_new_name is not None: 
            #These lines will occur when there is passing an rename for the removed catagory.
            

    def all_catagories(self):
        temp_list = [] #This appends all the first entry values to this list
        for _ in range(len(self.catagories)): #This means it will iterate through all the possible entries of the list
            temp_list.append(self.catagories[_][0])
        return temp_list
        
    def all_subcatagories(self):
        temp_list = [] #This appends all the first entry values to this list
        for _ in range(len(self.catagories)): #This means it will iterate through all the possible entries of the list
            temp_list.append(self.catagories[_][1:]) #This will append all values in the row excluding the inital value 
        return temp_list

    def findCatagory(self, reference) -> str:
        '''
        This is called by the main program
        This outputs the catagory of the transaction location string inputed into the function
        '''

        for i in range(len(self.catagories)): #Goes through the whole list of catagories
            if self.catagories[i][0] == reference: #If the reference is found in the list of catagories 
                return self.catagories[i][1] #Returns the catagory reference
        #ONLY occurs when the reference is not found in the list of catagories, this will need to append the new catagory to the csv file
        value = self.new_catagory(reference) #This calls a function that allows the user to add a new catagory to the csv file

        return value

    def new_catagory(reference) -> None:
        '''
        This is used to add a new transaction location to the csv file
        '''

        os.system("cls") #This clears the screen
        #This is where the user can add a new catagory to the csv file
        for row in range(len(self.catagory_list)):
            print(self.catagory_list[row][0])
        print("To create a new main catagory, type {}: {}".format(len(self.catagory_list +1), i))

        while type(catagory_variable) != int and int <= (len(self.catagory_list)) +1): #Only accepts integers 
            catagory_variable = input("The transaction of {} is unknown, please select which catagory index from above it belongs to".format(reference))

        os.system("cls") #This clears the screen

        if catagory_variable == len(self.catagory_list +1):
            #This is where the user can add a new catagory to the csv file
            new_catagory = input("Please enter the new catagory")
            Sub_catagory = self.new_subcatagory(reference) #This calls a function that allows the user to add a new subcatagory to the csv file

            temp_value = self.catagory_list.append(new_catagory, Sub_catagory) #This appends the new catagory to the catagory list
            with open('Catagory_list.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(temp_value)
        
        else:
            for i in range(len(self.catagory_list[catagory_variable])):
                print(self.catagory_list[catagory_variable][i] : i) #This prints all the subcatagories within the catagory
            print("To create a new subcatagory, type {}".format(len(self.catagory_list[catagory_variable] +1))
                  
            while type(subcatagory_variable) != int and int <= (len(self.catagory_list[catagory_variable])) +1): #Only accepts integers 
                Subcatagory_variable = input("The transaction of {} is unknown, please select which subcatagory index from above it belongs to".format(reference))
            
            if Subcatagory_variable == len(self.catagory_list[catagory_variable] +1):
                Sub_catagory = self.new_subcatagory(reference)
            else:
                Sub_catagory = self.catagory_list[catagory_variable][Subcatagory_variable]

            temp_value_1 = self.catagories.append(reference, self.catagory_list[catagory_variable][0], Sub_catagory) 
            #This appends the new catagory to the catagory list
            with open('catagories.csv', 'a') as f: 
                #This appends the whole new transaction type to the csv file
                writer = csv.writer(f)
                writer.writerows(temp_value_1)

        
        
    def findSubcatagory(self, reference) -> str:
        '''
        This is only called by main program
        This outputs the subcatagory of the transaction location string inputed into the function
        '''
        reference_catagory = self.findCatagory(reference) #Finds the catagory reference of the transaction
        for i in range(len(self.catagories)): #Goes through the whole list of catagories
            if  self.catagories[i][0] == reference: #This finds the row which contains the reference
                return self.catagories[i][2] #Returns the subcatagory of reference transaction
        
        return TypeError("The transaction of {} is unknown, please select which subcatagory index from above it belongs to".format(reference))
    
    def new_subcatagory(self, reference) -> None:
        #This is only called by new_catagory

        os.system("cls") #This clears the screen 
        for row in range(len(self.catagory_list)):
            if self.catagory_list[row][0] == reference:
                for i in range(len(self.catagory_list[row])):
                    print(self.catagory_list[row][i]) #This prints all the subcatagories within the catagory
                break #This is to stop the loop from printing the whole list of subcatagories

        print("To create a new subcatagory, type {}".format(len(self.catagory_list +1))
              
        while type(subcatagory_variable) != int and int <= (len(self.catagory_list)) +1): #Only accepts integers 
            subcatagory_variable = input("The transaction of {} is unknown, please select which subcatagory index from above it belongs to".format(reference))

        if subcatagory_variable == len(self.catagory_list +1):
            #This is where the user can add a new subcatagory to the csv file
            new_subcatagory = input("Please enter the new subcatagory")
            self.catagory_list[row].append(new_subcatagory)  #This appends the new subcatagory to the catagory list

            with open('Catagory_list.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(new_subcatagory)
            
            with open('catagories.csv', 'a') as f: 
                #This appends the whole new transaction type to the csv file
                writer = csv.writer(f)
                writer.writerows(reference, self.catagory_list[row][0], new_subcatagory)
        
            
