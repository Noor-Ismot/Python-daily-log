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
expense_amount = []
expense_category = []
expense_description = []
expense_per_category ={
     
}

def add_expense(item_number):
    total_expense_amount = 0
    for i in range(item_number):
        x, y, z = input(f"For Item {i+1}, write your expense amount in dollar, category and description: ").split(", ")
        expense_amount.append(x)
        expense_category.append(y)
        expense_description.append(z)
        expense_per_category[y] = x
        total_expense_amount += int(x)
          

    print(f"\nExpense Added Successfully!\n")
    print(expense_per_category)
    return total_expense_amount
    

def view_all_expense(item_number):   
    for i in range(int(item_number)):
        print(f"Catgory: {expense_category[i]}, Amount: ${expense_amount[i]}, Description: {expense_description[i]}")


def user_item():
    while True:
        expense_item = input("How many Items do you have: ")
        if expense_item.isdigit() :
                    if int(expense_item) <= 0:
                        print("Item number need to be larger than Zero")
                    else:
                        total_cost = add_expense(int(expense_item))
                        print(f"Your total expense: {total_cost}")
                        print("Your Expense List:")
                        view_all_expense(expense_item)
                        
        else:
            print("Enter a valid number.")


def main():
        expense_track = input("Do you want to add items? Please type Yes/No : ")
        if expense_track.lower() == 'yes':
            user_item()
        else:
            print("Program has been ended")
        

main()

