"""
Project Name: Personal Expense Tracker
========================================================================
Date: 21 December, 2025

Objectives:

Practice lists & dictionaries

Practice user input validation

Practice loops and conditionals

Understand data aggregation

---------------------------------------------------------
Requirements:-

User can:
-Add an expense (amount, category, description) : DONE
-View all expenses : DONE
-View total expenses : DONE
-View total per category

Constraints:
-Store expenses in memory only (no files)
-Amount must be a positive number 
-Category must be a non-empty string

=======================================================================
"""
expenses =[
]
expense_per_category ={}

def add_expense(item_number):
    
    for i in range(item_number):
        x, y, z = input(f"For Item {i+1}, write your expense amount in dollar, category and description: ").split(", ")
        expenses.append({"Amount": x, "Category": y, "Des": z})
    print(f"\nExpense Added Successfully!\n")
    print(expenses)
 
            


def user_item():
    while True:
        expense_item = input("How many Items do you have: ")
        if expense_item.isdigit() :
                    if int(expense_item) <= 0:
                        print("Item number need to be larger than Zero")
                    else:
                        all_expense = add_expense(int(expense_item))                       
        else:
            print("Enter a valid number.")


def main():
        expense_track = input("Do you want to add items? Please type Yes/No : ")
        if expense_track.lower() == 'yes':
            user_item()
        else:
            print("Program has been ended")
        

main()
