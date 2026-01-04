"""
Project Name: Personal Expense Tracker
=========================================================
Objectives:

Practice lists & dictionaries

Practice user input validation

Practice loops and conditionals

Understand data aggregation

---------------------------------------------------------
Requirements:-

User can:
-Add an expense (amount, category, description)
-View total expenses
-View total per category

Constraints:
-Store expenses in in files
-Amount must be a positive number 
-Category must be a non-empty string

=========================================================
"""
def view_category_expense(expense_list):
    expense_per_category ={}
    for expense in expense_list:
            category = expense["category"]
            amount = expense["amount"]
            if category in expense_per_category:
                expense_per_category.update({category:expense_per_category[category] + amount})
             
            else:
                expense_per_category.update({category:amount})                         
    return expense_per_category


def view_total(total_expense):
    total = 0
    for key in total_expense:
        total += total_expense[key]
    
    return total



def add_expense(item_number):   
    expenses =[]   
    for i in range(item_number):
        amount, category, description = input(f"For Item {i+1}, write your expense amount in dollar, category and description: ").split(", ")
        if amount.isdigit() and len(category) > 0 :
            amount = int(amount)
            category = category.lower()
            expenses.append({"amount": amount, "category": category, "description": description})
        else:
            print("Enter a positive integer number with Non empty category.")
            amount, category, description = input(f"For Item {i+1}, write your expense amount in dollar, category and description: ").split(", ")
    
    print(f"\nExpense Added Successfully!\n")    
    return expenses



def user_item():
    while True:
        expense_item = input("How many Items do you have: ")
        if expense_item.isdigit() :
            if int(expense_item) <= 0:
                print("Item number need to be larger than Zero")        
            else:
                break
            
        else:
            print("Please Enter a valid number:")
    
    all_expense = add_expense(int(expense_item))
    return all_expense




def main():
    temp_expense = {}
    
    while True:
        print(
        """\nChoose One from below list:
        1. Add expense
        2. View total expense
        3. View expense by category
        4. Exit
        """)

        user_operation = input("Type 1/2/3/4: ")
        if user_operation == "1":
            all_expense = user_item()
            expense_per_category = view_category_expense(all_expense)
            
            x = temp_expense.keys()
            if expense_per_category:
                for key in expense_per_category:
                    
                    if key in x:
                        temp_expense[key] = temp_expense[key] + expense_per_category[key]
                        
                    else:
                        temp_expense.update({key:expense_per_category[key]}) 
                        
        elif user_operation == "2":
            if len(temp_expense) == 0 :
                    print("No Expense Found!")
            else:
                total = view_total(temp_expense) 
                print(f"\nTotal Expense:{total}")

        elif user_operation == "3":
            if len(temp_expense) == 0 :
                  print("No Expense Found!")
            else:
                print(f"\nExpense by category-")
                for key in temp_expense:
                    print(f"{key}:{temp_expense[key]}")

        elif user_operation == "4":
            break        
        else:
            print("Please select a valid numerical option(1-4)")
               
    print("Program has been ended")                 

main()