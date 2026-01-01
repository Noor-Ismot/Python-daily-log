"""
Project Name: Personal Expense Tracker
========================================================================
Date: 21 - 25 December, 2025

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
        if x.isdigit():
            x = int(x)
            y = y.lower()
            expenses.append({"Amount": x, "Category": y, "Des": z})
        else:
            print("Enter a positive integer number with Non empty category.")
            x, y, z = input(f"For Item {i+1}, write your expense amount in dollar, category and description: ").split(", ")
    
    print(f"\nExpense Added Successfully!\n")    
    return expenses



def user_item():
    while True:
        expense_item = input("How many Items do you have: ")
        if expense_item.isdigit() :
                    if int(expense_item) <= 0:
                        print("Item number need to be larger than Zero")        
                    else:
                        all_expense = add_expense(int(expense_item))
                                              
        else:
            break
  
    return all_expense


def main():
    temp_expense = []
    while True:
        print("Choose One from below list:")
        print("""
        1. Add expense
        2. View total expense
        3. View expense by category
        4. Exit"
        """)

        user_operation = input("Type 1/2/3/4: ")
        if user_operation == "1":
            temp_expense += user_item() 
            expense_per_category = view_category_expense(temp_expense)
            print(f"Expense Per category:\n{expense_per_category}")  
            total = view_total_expense(temp_expense)
            print(f"Total Expense:\n{total}")   
        elif user_operation == "2":
             if len(temp_expense) == 0 :
                  print("No Expense Found!")
        elif user_operation == "3":
                if len(temp_expense) == 0 :
                  print("No Expense Found!")
        else:
            break

    temp_expense += user_item()    
    print("Program has been ended")         
 
                   

main()
