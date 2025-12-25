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
def view_category_expense(expense_list):
    expense_per_category ={}
    for expense in expense_list:
            category = expense["Category"]
            amount = expense["Amount"]
            if category in expense_per_category:
                expense_per_category.update({category:expense_per_category[category] + amount})
             
            else:
                expense_per_category.update({category:amount})                         
    return expense_per_category


def view_total_expense(expense_list):  
    total_expense = 0
    for expense in expense_list:
        amount = expense["Amount"]
        total_expense += amount   
    return total_expense

def add_expense(item_number):
    
    expenses =[]   
    for i in range(item_number):
        x, y, z = input(f"For Item {i+1}, write your expense amount in dollar, category and description: ").split(", ")
        x = int(x)
        y = y.lower()
        expenses.append({"Amount": x, "Category": y, "Des": z})
    return expenses



def user_item():
    while True:
        expense_item = input("How many Items do you have: ")
        if expense_item.isdigit() :
                    if int(expense_item) < 0:
                        print("Item number need to be larger than Zero")
                    elif int(expense_item) == 0:
                        ans = input("Do you want to view total expense?y/n :")
                        if ans.lower() == 'n':
                             print("Program has been ended")
                        else:
                             pass #Need to be updated
                             
                    else:
                        all_expense = add_expense(int(expense_item))
                        print(f"\nExpense Added Successfully!\n")
                        expense_per_category = view_category_expense(all_expense)
                        print(f"Expense Per category:\n{expense_per_category}")  
                        total = view_total_expense(all_expense)
                        print(f"Total Expense:\n{total}")   
        else:
            print("Enter a valid number.")



def main():
        expense_track = input("Do you want to add items? Please type Yes/No : ")
        if expense_track.lower() == 'yes':
            user_item()
        else:
            print("Program has been ended")
        

main()
