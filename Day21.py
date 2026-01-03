"""
#LEARN PYTHON : DAY 21
#Topics: Error Handling
#Resources: https://www.w3schools.com/python/python_try_except.asp
#Date: January 3, 2026

#Error handling in Python
#Error handling is a way to respond to runtime errors in your code, allowing the program to continue its execution instead of crashing.
#In Python, error handling is done through the use of try and except blocks.


print("-----------Error Handling in Python---------------")
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
try:
    print(x)
except:
    print("An exception occurred")



print("\n-----------Handling Specific Exceptions---------------")
#Handling Specific Exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


print("\n-----------Using else Keyword---------------")
#Using else Keyword
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


print("\n-----------Using finally Keyword---------------")
#Using finally Keyword
try:
    print("Hello")
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


print("\n-----------Raise an Exception---------------")
#Raise an Exception
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")


print("\n-----------Custom Exception---------------")
#Custom Exception
class ValueTooHighError(Exception):
    pass
class ValueTooLowError(Exception):
    pass
def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooLowError("Value is too low")
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e)

"""

print("\n-----------Final Example---------------")
#Final Example
def add_expense(num_items):
    expenses = {}
    for i in range(num_items):
        while True:
            item_name = input(f"Enter name for item {i+1}: ")
            item_cost = input(f"Enter cost for item {i+1}: ")
            try:
                item_cost = float(item_cost)
                if item_cost < 0:
                    raise ValueError("Cost cannot be negative.")
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please enter a valid number for cost.")
        
        expenses[item_name] = item_cost
    return expenses

x = int(input("How many expense items do you want to add? "))
all_expenses = add_expense(x)
print("Expenses added successfully:")
for item, cost in all_expenses.items():
    print(f"{item}: ${cost:.2f}")