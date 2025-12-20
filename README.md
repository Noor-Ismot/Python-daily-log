# Python-daily-log
Daily Python practice covering fundamentals, problem-solving, automation, and mini-projects, tracked to build strong programming foundations.

# LEARN PYTHON - DAY 1 - Data Types, Conditions
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

# LEARN PYTHON : DAY 2 - List part 1
Topics: Data Structures - Lists [Part 1]
- Lists are ordered, mutable (changeable), and allow duplicate values.
- Lists are defined using square brackets [].
- You can access list items using their index, and you can also use slicing to access a range of items.
- You can add items to a list using append(), insert(), and extend() methods.
- You can change list items by specifying the index or a range of indices.
- You can sort and reverse lists using sort() and reverse() methods.
- You can check if an item exists in a list using the 'in' keyword.

# LEARN PYTHON : DAY 3 - List Part 2
Topics: Data Structures - Lists [Part 2]
- Looping through a list using for loop with and without range function.
- Looping through a list using while loop.
- Looping through a list using list comprehension.
- Copying a list using copy() method.
- Joining two lists using + operator and extend() method.
- Removing list items using remove(), pop(), del keyword, and clear() method.

# LEARN PYTHON : DAY 4 - Loops
Topics: Range function and Loops [For Loop, While Loop with break, continue, else, pass statements]
- The range() function generates a sequence of numbers, which can be customized using start, stop, and step parameters.
- For loops are used to iterate over sequences such as lists, strings, and more, without needing an indexing variable.
- The break statement can be used in loops to exit the loop prematurely when a certain condition is met.
- The continue statement allows skipping the current iteration of a loop and moving to the next iteration.
- The else clause in loops executes a block of code when the loop completes normally, but not if it is terminated by a break statement.
- While loops execute a block of code as long as a specified condition is true, and require careful management of loop counters to avoid infinite loops.
- The pass statement can be used as a placeholder in loops to avoid syntax errors when no action is needed.

# LEARN PYTHON : DAY 5 - Function
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

# LEARN PYTHON : DAY 6 - Tuple
- Tuples are ordered, unchangeable, and allow duplicate values.
- Tuples are defined with round brackets ().
- Access tuple items using indexing and slicing.
- Tuples are immutable; to update, convert to a list, modify, and convert back.
- Unpack tuples into variables, using * for excess items.
- Loop through tuples using for loops.
- Join tuples using the + operator and multiply using *.
- Tuple methods: count() and index().

# LEARN PYTHON : DAY 7 - Dictionary
- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
- Dictionaries are written with curly brackets, and have keys and values.
- Defining a dictionary using curly braces {}.
- Accessing dictionary values using key names or get() method.
- Adding new items or updating existing items in a dictionary.
- Checking if a key exists in a dictionary.
- Removing items from a dictionary using pop(), popitem(), del, and clear() methods.
- Copying a dictionary using copy() method and dict() function.
- Looping through a dictionary to access keys, values, and key-value pairs.

# LEARN PYTHON : DAY 8 - String
- Defined strings using single, double, and triple quotes.
- Accessed string characters using indexing and slicing.
- Modified strings using methods like upper(), replace().
- Explored various string methods: find(), count(), isalnum(), startswith(), endswith(), split(), strip(), join(), capitalize(), title(), swapcase(), isnumeric(), isalpha(), islower(), isupper(), index().
- String concatenation using + operator.
- String formatting using f-strings and format() method.
- Strings are immutable and ordered collections of characters.

# LEARN PYTHON : DAY 9 - Set
- Defining Set using curly braces {}
- Accessing Set items using loops and 'in' keyword
- Adding items using add() and update() methods
- Removing items using remove(), discard(), pop() methods
- Frozen Set as immutable set
- Joining Sets using union(), intersection(), difference(), symmetric_difference() methods and operators
- Set operations: union, intersection, difference, symmetric difference

# LEARN PYTHON : DAY 10 - File
- Learned how to handle files in Python using the open() function with different modes such as read, append, write, and create.
- Understood how to read from files using methods like read() and readlines(), and how to loop through file content.
- Practiced writing to files using append and write modes, and observed the differences in behavior between them.

# LEARN PYTHON : DAY 11 - Problem Solving [Part 1]
- Topics: Input, Output, Comments 

# LEARN PYTHON : DAY 12 - Problem Solving [Part 2]
- Topics: Loops, Conditions
- Learned how to use loops effectively to solve various problems, including counting, summing, generating multiplication tables, reversing numbers, checking for palindromes, and calculating factorials. I also learned how to handle negative numbers and leading zeros in string manipulations.

1. Goal: Print numbers from 1 to N. \
Input: integer N
Output: numbers from 1 to N (one per line)
Constraints: N ≥ 1

Test cases:
5 → 1 2 3 4 5
1 → 1
3 → 1 2 3

2. Goal: Print all even numbers between 1 and N.

Input: integer N
Output: even numbers ≤ N
Constraints:N ≥ 2

Test cases:
10 → 2 4 6 8 10
5 → 2 4
2 → 2

3. Goal: Calculate the sum of numbers from 1 to N.
Input: integer N
Output: integer sum
Constraints:N ≥ 1

Test cases:
5 → 15
1 → 1
10 → 55


4. Goal: Print multiplication table of a number up to 10.
Input: integer N
Output: N x i = result for i = 1..10
Constraints: N between 1 and 20

Test cases:
3 → 3 x 1 = 3 ... 3 x 10 = 30
5 → ...

5. Goal: Count digits in a number.
Input: integer
Output: number of digits
Constraints: Negative numbers allowed

Test cases:
123 → 3
0 → 1
-4567 → 4

Bias trap: Strings make this trivial — don’t use them.

6. Goal: Reverse a number.
Input: integer
Output: reversed integer
Constraints: No string conversion

Test cases:
123 → 321
100 → 1
-456 → -654

7. Goal: Check if a number is a palindrome.
Input: integer
Output: "Palindrome" or "Not Palindrome"
Constraints:No string usage

Test cases:
121 → Palindrome
123 → Not Palindrome
0 → Palindrome

8. Goal: Find factorial of a number.
Input: integer N
Output: factorial value
Constraints:N ≥ 0

Test cases:
5 → 120
0 → 1
3 → 6

9. Goal: Print Fibonacci sequence up to N terms.
Input: integer N
Output: first N Fibonacci numbers
Constraints:N ≥ 1

Test cases:
5 → 0 1 1 2 3
1 → 0
2 → 0 1

10. Goal: Find sum of digits of a number.
Input: integer
Output: sum of digits
Constraints:No string conversion

Test cases:
123 → 6
0 → 0
-456 → 15

