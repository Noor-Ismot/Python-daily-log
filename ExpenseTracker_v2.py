"""
Expense Tracker Application version 2.0
----------------------------------------
A simple, command-line expense tracking program built in Python that helps users manage spending by category and view totals. The program uses a dictionary-based structure and saves data to a local file, ensuring your records are preserved even after closing the program.

Features
--------------------------
-Add Expenses: Quickly input expense amount, category, and description.
-View Total Expense: Get a cumulative sum of all expenses.  
-View Expenses by Category: See a breakdown of spending organized by category. 
-Persistent Storage: Automatically saves and loads data from a json file using the JSON format.
-Input Validation: Ensures only valid numbers and non-empty categories are accepted.  

Code Highlights
--------------------------
- JSON Integration: Uses the `json` module to serialize and deserialize data, allowing for permanent storage in `expense.json`.
- Modular Logic: Separate functions for loading, saving, and calculating totals make the code clean and maintainable.
- Error handling: Input validation ensures a smooth and error-free user experience.

Future Improvements
--------------------------
1. Visualizations: Add charts or graphs to represent spending visually.
2. GUI Interface: Create a user-friendly graphical interface using Tkinter or PyQt.
3. Budget alerts: Notify users when spending exceeds set limits.
4. Date Tracking: Include timestamps for each expense to allow for weekly or monthly reports.
"""

import json

def save_expense(expense_per_category):
    expense_per_category_json_str = json.dumps(expense_per_category, indent=4) 
    with open("expense.json","w") as expense_file:
        expense_file.write(expense_per_category_json_str)
    return expense_per_category_json_str


def expense_load_from_file():
    with open("expense.json", "r") as expense_file:
        expense_per_category = json.load(expense_file)
        return expense_per_category
        


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
    try:
        expense_per_category_from_file = expense_load_from_file()
        temp_expense.update(expense_per_category_from_file)
    except FileNotFoundError:
        with open("expense.json", "w") as file:
            file.write("{}")
    
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
            
            expense_category = temp_expense.keys()
            if expense_per_category:
                for key in expense_per_category:
                    if key in expense_category:
                        temp_expense[key] = temp_expense[key] + expense_per_category[key]
                          
                    else:
                        temp_expense.update({key:expense_per_category[key]}) 
            expense_per_category_from_file = save_expense(temp_expense)                      

        elif user_operation == "2":
            if len(temp_expense) == 0 :
                    print("No Expense Found!")
            else:
                total = view_total(temp_expense) 
                print(f"\nTotal Expense:{total}")


        elif user_operation == "3":
            if len(temp_expense) == 0:
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