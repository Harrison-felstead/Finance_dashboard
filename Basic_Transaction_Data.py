
__author__ = 'Harrison Felstead'
__version__ = '0.1.0'

class Basic_Transaction_Data:
    '''
    This is the initalisation of all the basic data that is stored within an transaction
    that has already been passed through the CSV file converter to this programs
    standardised format.
    '''
    def __init__(self, date, transaction_type, amount, details, catagory, subcatagory) -> None:
        #Dont pass any data into this as a tuple

        self.date = date 
        self.transaction_type = transaction_type
        self.amount = amount
        self.details = details
        self.catagory = catagory
        self.subcatagory = subcatagory
        self.description = str("There is no description for this transaction")
        self.tax_reduction = float(0.0)

    def set_description(self):
        '''
        This function is used to set the description of the transaction
        ''' 
        print("The current description is: " + self.description + "\n")
        input = input("Would you like to write over this or just append to this current description? (Yes or No):)")
        continue_loop = True
        while continue_loop == True:
            if input == "No":
                self.description = str(input("Please enter a description for this transaction: "))
                continue_loop = False
            elif input == "Yes":
                self.description = str(self.description + " " + input("Please enter a description for this transaction:"))
                continue_loop = False
            else:
                print("Please enter a valid input")

    def retrieve_description(self) -> str:
        '''
        This function is used to retrieve the description of the transaction
        '''
        return self.description
    
    def set_tax_reduction(self):
        '''
        This function is used to set the tax reduction of the transaction
        '''
        print("The current tax reduction is: " + str(self.tax_reduction) + "\n")
        while type(self.tax_reduction) != float:
            self.tax_reduction = float(input("Please enter a tax reduction for this transaction (float format): "))

    def retrieve_tax_reduction(self) -> float:
        '''
        This function is used to retrieve the tax reduction of the transaction
        '''
        return self.tax_reduction