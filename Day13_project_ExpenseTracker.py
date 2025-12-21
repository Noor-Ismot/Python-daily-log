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
-Add an expense (amount, category, description)
-View all expenses
-View total expenses
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
total_expense_amount = 0

expense_item = int(input("How many Items do you have: "))

for i in range(expense_item):
    x, y, z = input(f"For Item {i+1}, write your expense amount, category and description: ").split(", ")
    expense_amount.append(x)
    expense_category.append(y)
    expense_description.append(z)
    total_expense_amount += int(x)

print(f"Expense Added Successfully!\n")
print(f"Your total expense: {total_expense_amount}")



#need to modify---------------------------

"""
expense_detail = {
"amount" : expense_amount,
"category" : expense_category,
"description" : expense_description
}


print("Expenses Category wise:")
for i in expense_category:
    for j in expense_amount:
        print(f"{i}: {j}")
"""

