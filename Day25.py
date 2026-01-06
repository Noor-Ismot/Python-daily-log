#LEARN PYTHON : DAY 25
#Topics: List Comprehension
#Resources: 
# https://www.w3schools.com/python/python_lists_comprehension.asp
# https://www.geeksforgeeks.org/python/python-list-comprehension/

#List Comprehension: List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list or range) and optionally filtering items based on a condition.

"""
Why Use List Comprehension?
Cleaner code: Combines looping, filtering and transformation in one line.
More readable: Avoids verbose loops and temporary variables.
Faster execution: Often faster than equivalent for-loops.
"""

#Syntax: newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)