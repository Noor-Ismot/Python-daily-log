"""
Expense Tracker Application version 1.0
A simple, interactive expense tracking project built in Python that helps users manage daily spending by category and view totals. The program stores expenses in a dictionary, allowing for efficient categorization and retrieval. Users can continuously add expenses and view summaries until they choose to exit.
Features

1. Add Expenses: Quickly input expense amount, category, and description.  
2. View Total Expense: Get a cumulative sum of all expenses.  
3. View Expenses by Category: See how your spending breaks down.  
4.Persistent Session Tracking: Add multiple expenses in the same runtime session.  
5. Input Validation:Only accepts valid numeric amounts and non-empty categories.

Code Highlights

-Dictionary-based storage: Organizes expenses by category for fast lookup and aggregation.
- Reusable functions: Functions like `view_category_expense`, `view_total_expense`, and `add_expense` make the code modular and easy to extend.
- Error handling: Input validation ensures a smooth and error-free user experience.

Future Improvements
1. Data persistence: Save expenses to a file (CSV/JSON) or database.
2. Visualizations: Add charts or graphs to represent spending visually.
3. GUI Interface: Create a user-friendly graphical interface using Tkinter or PyQt.
4. Budget alerts: Notify users when spending exceeds set limits.

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



def add_expense(item_number): 
    expenses =[] 
    for i in range(item_number): 
        x, y, z = input(f"For Item {i+1}, write your expense amount in dollar, category and description: ").split(", ") 
        if x.isdigit() and len(y)>0 : 
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
                break
        else: 
            print("Please Enter a valid number:") 
            all_expense = add_expense(int(expense_item)) 
        
    return all_expense 


def view_total(total_expense): 
    total = 0 
    for key in total_expense: 
        total += total_expense[key] 
    
    return total 
    
    
def main(): 
    temp_expense = {} 
    while True: 
        print( """Choose One from below list: 
              1. Add expense 
              2. View total expense 
              3. View expense by category 
              4. Exit """) 
    
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