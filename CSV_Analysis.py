import csv

__author__ = 'Harrison Felstead'
__version__ = '0.1.0'


class Parent_Class:
    def __init__(self, CSV_file):
        self.CSV_file = CSV_file
        #Need to init the  master.csv file here
        

    #The following methods where copied from FIT1008 Week 4 Lecture Notes#

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """ 
            Magic method. Insert the item at a given position, if possible (!). 
            When the sortedness condition is checked (and satisfied), check if 
            the list if full, in which case resize it.
            Don't forget to shift the following elements to the right.
        """
        if self.is_empty() or \
                (index == 0 and value <= self[index]) or \
                (index == len(self) and self[index - 1] <= value) or \
                (index > 0 and self[index - 1] <= value <= self[index]):

            if self.is_full():
                self._resize()

            self._shuffle_right(index)
            self.array[index] = value
        else:
            # the list isn't empty and the item's position is wrong wrt. its neighbourghs
            raise IndexError('Element should be inserted in sorted order')

    def __contains__(self, item):
        """ Checks if item is in the list. """
        try:
            _ = self.index(item)
            return True
        except ValueError:
            return False

    def _shuffle_right(self, index: int) -> None:
        """ Shuffle items to the right up to a given position. """
        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

    def _shuffle_left(self, index: int) -> None:
        """ Shuffle items starting at a given position to the left. """
        for i in range(index, len(self)):
            self.array[i] = self.array[i + 1]
        
    #End of copied methods#

    def analysed_CSV_data(self):
        pass

class ANZ(Parent_Class):
    def analysed_CSV_data(self):
        with open(self.CSV_file, "r", newline='') as csvfile: 
            #This is the file that is being read
            self.reader = csv.reader(csvfile)
            with open(Master.csv, "r", newline='') as Master_csvfile: 
                #This is the file that is being writen too
                self.writer = csv.writer(csvfile)

                #This will iterate through each row in the CSV file (That is being read)
                for row in self.reader:

                    #The first column in the row is the date
                    self.date = row[0]
                    #The second column in the row is the amount being transacted
                    if row[1] >= 0:
                        self.transaction_type = "Debit"
                    else:
                        self.transaction_type = "Credit"
                    
                    #This is the amount being transacted
                    self.amount = abs(row[1])

                    #This is the details of the vendor,
                    #The csv has ,,,, at the end of an row so this is used to split
                    #the details from the rest of the row
                    self.details, _ = row[2].split(",,,,") 

                    #This is the catagory of the transaction
                    self.catagory = self.details.get_catagory()
                    #This is the subcatagory of the transaction
                    self.subcatagory = self.details.get_subcatagory()

                    if Master_csvfile.__contains__(self.date, self.transaction_type, self.amount, self.details, self.catagory, self.subcatagory) == True:
                        