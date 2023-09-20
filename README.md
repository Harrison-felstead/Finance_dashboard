# Finance_dashboard
This is a project that is used to create everything i need for Finance stuff

___________________________Todo List______________________________________ 
1. be able to pull data off a CSV off bank statements (Use ANZ as a benchmark)
2. be able to sort through that data and catagorise it depending on debit or credit
3. Sort through that list and associate those companies with the type of expendature (Grosseries, fuel)
4. Analyse the data and interperate it in useful manner
5. create a dashboard, of graphs and methods of removing certian sets of data. 
6. be able to analyse the data to determine the approximate amount of tax 
6.1 be able to modify certian items so they have able to get tax rebates back. 
7. be able to create a budget and compare it to the actual data.
9. look at how catagories have changed over time. 

__________________________Mission Statement__________________________
The purpose of this project is to create a dashboard that will allow me to analyse my finances and be able to make better decisions about my finances.
To reduce the reliance of people to have to go to financial advisors to get advice on how to manage their finances and manage their taxes
To have the capability to understand where your money travels and how it is spent.
The ability to track your household average income and expenses and be able to predict future expenses and income.


__________________________Project Scope__________________________
    1. The ability to pull data from a CSV file and be able to sort it into a dataframe
    2. The ability to sort through the data and catagorise it into debit and credit
    3. The ability to catagorise the data into certian catagories
    4. The ability to analyse the data and interperate it in a useful manner
    5. The ability to create a dashboard of graphs and methods of removing certian sets of data
    6. The ability to analyse the data to determine the approximate amount of tax
    7. The ability to modify certian items so they have able to get tax rebates back
    8. The ability to create a budget and compare it to the actual data
    9. The ability to look at how catagories have changed over time (Either month by month or year by year)

__________________________Project goals_______________________________

1. Refining "Details" aspect of the data:                                         DONE 
// This is all the types of transactions and will need to be sorted and cleaned prior to entry within the uniform dataset //

1.1: Visa Debit, Remove the first 30 char within the string                       DONE 
1.2: Payment, Remove the 13 char within the string                                DONE
1.3: Transfer, Remove the 14 char within the string                               Done 
1.4: BPay, Remove the first 26 char within the string & last 20 char              Done 
1.5: ANZ Banking Payment: Remove the first 39 char within the string              Done 
1.6: EFTPOS, Remove the first 15 char within the string                           Done
1.7: Account Funds transfer, Remove the first 34 Char within the string           Done 


2. Assigning the catagory for each data entry:
// This will be an automated process that will assign a catagory and possbily subcatagory to each data entry //
// By defult the catagory will need to be assigned, and the subcatagory will be "None" //

2.1: Make a def that will iterate through an array (Containing all the catagories) and check if the string contains any of the catagories. If not there call 2.2 def                                                                  DONE
2.2: Def that will append the string to a list that will be used to manually assign the catagory and possible subcatagory to the data entry    DONE
2.3: Make an array that will contain the tuple with (account, catagory, subcatagory) and append it to the array.           Done (changed data type)
2.3: Make a def that will retrieved the catagory and subcatagory from the array and assign it to the data entry, using the def 2.1.  DONE
2.4: It will make an def to be able to change the catagory and subcatagory of the data entry.
2.5.1: Make a def that will be able to add a new catagory to the array
2.5.2: Make a def that will be able to add a new subcatagory to the array
1.5.3: Make a list that will contains all the catagories
1.5.4: Make a list that will contain all the subcatagories
2.6: Make a def that will be able to remove a catagory from the array
2.7: Make a def that will be able to remove a subcatagory from the array 