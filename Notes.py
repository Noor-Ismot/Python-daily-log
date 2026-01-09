"""
# Python-daily-log
Daily Python practice covering fundamentals, problem-solving, automation, and mini-projects, tracked to build strong programming foundations.

# DAY 1 - Data Types, Conditions
Topics: Variables, Data Type, Type Casting, Output, Comments, Conditions, Logical Operators, Nested if, Pass statement
Summary:
- Variables are used to store data values and can be created by assigning a value using the equals sign (=).
- Python has various data types, including text, numeric, sequence, mapping, set, boolean, and binary types.
- The print() function is used to display output, and you can customize its behavior using parameters like end.
- You can assign multiple values to multiple variables in one line and print multiple variables together.
- The type() function helps determine the data type of a variable, and type casting allows you to convert variables to specific data types.
- Conditional statements (if, elif, else) are used to execute code based on specific conditions, and shorthand if...else can be used for concise conditional assignments.
- Logical operators (and, or, not) allow you to combine multiple conditions in your statements.
- Nested if statements enable you to check conditions within other conditions.
- The pass statement serves as a placeholder for future code, allowing you to define empty blocks without causing syntax errors.

# DAY 2 - List part 1
Topics: Data Structures - Lists [Part 1]
- Lists are ordered, mutable (changeable), and allow duplicate values.
- Lists are defined using square brackets [].
- You can access list items using their index, and you can also use slicing to access a range of items.
- You can add items to a list using append(), insert(), and extend() methods.
- You can change list items by specifying the index or a range of indices.
- You can sort and reverse lists using sort() and reverse() methods.
- You can check if an item exists in a list using the 'in' keyword.

# DAY 3 - List Part 2
Topics: Data Structures - Lists [Part 2]
- Looping through a list using for loop with and without range function.
- Looping through a list using while loop.
- Looping through a list using list comprehension.
- Copying a list using copy() method.
- Joining two lists using + operator and extend() method.
- Removing list items using remove(), pop(), del keyword, and clear() method.

# DAY 4 - Loops
Topics: Range function and Loops [For Loop, While Loop with break, continue, else, pass statements]
- The range() function generates a sequence of numbers, which can be customized using start, stop, and step parameters.
- For loops are used to iterate over sequences such as lists, strings, and more, without needing an indexing variable.
- The break statement can be used in loops to exit the loop prematurely when a certain condition is met.
- The continue statement allows skipping the current iteration of a loop and moving to the next iteration.
- The else clause in loops executes a block of code when the loop completes normally, but not if it is terminated by a break statement.
- While loops execute a block of code as long as a specified condition is true, and require careful management of loop counters to avoid infinite loops.
- The pass statement can be used as a placeholder in loops to avoid syntax errors when no action is needed.

# DAY 5 - Function
- Functions are blocks of code that run when called and can return data.
- Functions help avoid code repetition.
- Functions can return data using the return statement.
- If a function lacks a return statement, it returns None by default.
- The pass statement allows creating function placeholders without code.    
- Functions can accept arguments to customize their behavior.
- Default parameter values allow functions to have optional arguments.
- Keyword arguments enable passing arguments by name for clarity.
- Python follows the LEGB rule for variable name lookup: Local, Enclosing, Global, Built-in.
- Variable scope determines where variables can be accessed within functions.
- The global keyword allows modifying global variables within functions.
- Functions can return values to the calling code.
- The pass statement can be used in functions to create empty function bodies.
- *args allows passing a variable number of positional arguments to functions.
- **kwargs allows passing a variable number of keyword arguments to functions.

# DAY 6 - Tuple
- Tuples are ordered, unchangeable, and allow duplicate values.
- Tuples are defined with round brackets ().
- Access tuple items using indexing and slicing.
- Tuples are immutable; to update, convert to a list, modify, and convert back.
- Unpack tuples into variables, using * for excess items.
- Loop through tuples using for loops.
- Join tuples using the + operator and multiply using *.
- Tuple methods: count() and index().

# DAY 7 - Dictionary
- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
- Dictionaries are written with curly brackets, and have keys and values.
- Defining a dictionary using curly braces {}.
- Accessing dictionary values using key names or get() method.
- Adding new items or updating existing items in a dictionary.
- Checking if a key exists in a dictionary.
- Removing items from a dictionary using pop(), popitem(), del, and clear() methods.
- Copying a dictionary using copy() method and dict() function.
- Looping through a dictionary to access keys, values, and key-value pairs.

# DAY 8 - String
- Defined strings using single, double, and triple quotes.
- Accessed string characters using indexing and slicing.
- Modified strings using methods like upper(), replace().
- Explored various string methods: find(), count(), isalnum(), startswith(), endswith(), split(), strip(), join(), capitalize(), title(), swapcase(), isnumeric(), isalpha(), islower(), isupper(), index().
- String concatenation using + operator.
- String formatting using f-strings and format() method.
- Strings are immutable and ordered collections of characters.

# DAY 9 - Set
- Defining Set using curly braces {}
- Accessing Set items using loops and 'in' keyword
- Adding items using add() and update() methods
- Removing items using remove(), discard(), pop() methods
- Frozen Set as immutable set
- Joining Sets using union(), intersection(), difference(), symmetric_difference() methods and operators
- Set operations: union, intersection, difference, symmetric difference

# DAY 10 - File
- Learned how to handle files in Python using the open() function with different modes such as read, append, write, and create.
- Understood how to read from files using methods like read() and readlines(), and how to loop through file content.
- Practiced writing to files using append and write modes, and observed the differences in behavior between them.

# DAY 11 - Problem Solving [Part 1]
- Topics: Input, Output, Comments
- Focused on how to take multiple input in one line.
- Format output using sep and end parameters in print() function.
- Used comments effectively to explain code logic.
- Multiple line string using triple quotes.

# DAY 12 - Problem Solving [Part 2]
- Topics: Loops, Conditions
- Focused on how to use loops effectively to solve various problems, including counting, summing, generating multiplication tables, reversing numbers, checking for palindromes, and calculating factorials. I also learned how to handle negative numbers and leading zeros in string manipulations.


# DAY 13 - Project: Personal Expense Tracker
- A personal expense tracker application that allows users to add expenses with details such as amount, category, and description. The application calculates and displays the total expenses incurred and further enhanced to provide category-wise expense summaries.

# DAY 14 and Day 15 - Project: Slot Machine Game
- A slot machine game implemented in Python using functions, loops, and conditional statements. The game allows users to deposit money, place bets on lines, spin the reels, and win based on matching symbols.
Learning Objectives:
- Practice functions and modular code
- Practice loops and conditionals
- Understand randomization
- Understand basic game mechanics

# DAY 16- 20 : Updates on Project Personal Expense Tracker


# DAY 18 - 19 Problem Solving [Part 3]
- Topics: Lists
- Summary of the  problem solving challenges:  My hands-on practice with Python list operations through progressively challenging problems.
-Focusing points included:
 Iterating over lists using for and while loops.
 Manual implementations of common operations (sum, max, reverse, duplicate, removal) without relying on built-in shortcuts
 Handling edge cases such as empty lists, single-element lists, duplicate values, and negative numbers
 Writing clear, readable logic and improving code structure by separating input parsing from core algorithms
 The goal of these exercises was not just to get correct output, but to understand how list traversal and state tracking work internally.

 # DAY 21 : Error and Exception Handling
- Topics: Errors and Exception Handling
- Focused on different types of errors in Python, including syntax errors and exceptions.
- Explored how to handle exceptions using try, except, else, and finally blocks.
- Practiced raising exceptions using the raise statement.

# DAY 22 : Object-Oriented Programming (OOP) Basics
- Topics: Classes and Objects
- Learned the fundamentals of Object-Oriented Programming (OOP) in Python.
- Created classes to define blueprints for objects, encapsulating attributes and behaviors.
- Instantiated objects from classes and accessed their attributes and methods.
- Concepts of encapsulation, inheritance, and polymorphism in OOP.


# DAY 23 : Modules and Packages
- Topics: Modules and Packages
- Learned how to organize Python code using modules and packages.
- Created custom modules and imported them into other scripts.
- Explored built-in modules and third-party packages to extend Python's functionality.

# DAY 24 : Lambda Functions
- Topics: Lambda Functions
- Lambda functions are small anonymous functions defined using the lambda keyword.
- They can take any number of arguments but can only have one expression.
- Lambda functions are often used for short, throwaway functions that are not reused elsewhere in the code.
- They are commonly used with built-in functions like map(), filter(), and reduce() to perform operations on lists or other iterables.
- While lambda functions are useful for simple operations, for more complex functions, it's better to use the def keyword to define a standard function.


# DAY 25 : List Comprehensions
- Topics: List Comprehensions
- List comprehensions provide a concise way to create lists in Python.
- They consist of brackets containing an expression followed by a for clause, and can include optional if clauses for filtering.
- List comprehensions can replace traditional for loops for creating lists, making the code more readable and efficient.
- They can also be nested to create more complex lists.
"""

