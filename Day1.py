#LEARN PYTHON : DAY 1
#Topics: Variables, Data Type, Type Casting, Output, Comments, Conditions, Logical Operators, Nested if, Pass statement
#Resources: https://www.w3schools.com/python/default.asp
#Date: 8 December 2025



print("------------------Variables in Python -----------------")
print("A variable is a container for storing data values, and you can create a variable by simply assigning a value to it using the equals sign (=). ")


my_name = "Noor"
my_age = 30
my_height = 5.1
is_student = False


print("-------------Print output examples:----------------------")
#Print output.By default, the print() function ends with a new line.
#If you want to print multiple words on the same line, you can use the end parameter of the print() function to specify what to print at the end.
print("My name is ", my_name, end=" ")
print(my_age)

print("\n \n -------------Python Data Types:----------------------")
print(
"""
Text Type:	str     
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range  
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""
)

#Assigning multiple values to multiple variables in one line
print("----------Assigning multiple values to multiple variables:-----------")
my_name, my_age, my_height, is_student = "Ismot", 32, 5.0, False


#printing multiple variables together
print("------Printing multiple variables:")
print("Name:", my_name, "Age:", my_age, "Height:", my_height, "Is Student:", is_student)


#type() function is used to know the data type of a variable.
#casting is done to specify a variable to a specific data type.
print("\n ----Data Types and Type Casting:")
print(type(my_age))
print(type(float(my_age)))


print("\n ------Concatenation: Joining multiple strings using the + operator----------")
print("Hello"+ " " + my_name + "! " + "Welcome to Python Programming.")


#Conditions: if, elif, else
print("\n ------------Checking conditions:----------")
if my_age >= 18:
    print(my_name + " is an adult.")
else:
    print(my_name + " is a minor.")

#when to use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.
print("\n -----------if, elif and else conditions------------")
if my_age < 13:
    print(my_name + " is a child.")     
elif my_age < 20:
    print(my_name + " is a teenager.")  
else:
    print(my_name + " is an adult.")

#short hand if...else
print("\n ------------Determining status with shorthand if...else:--------------")
status = "Adult" if my_age >= 18 else "Minor"
print(my_name, "is a", status)

#shorthand with multiple conditions
print("\n ----------Determining status with multiple conditions:-----------")
status = "Child" if my_age < 13 else "Teenager" if my_age < 20 else "Adult"
print(my_name, "is a", status)

#Logical operators: and, or, not
print("\n -------Checking multiple conditions:-------------")
if my_age >= 18 and not is_student:
    print(my_name + " is a Professional")        
elif my_age < 18 or is_student:   
    print(my_name + " is either a minor or a student.")

#Nested if statements
print("\n -------Checking nested conditions:-------")
if my_age >= 18:
    if is_student:
        print(my_name + " is not a Professional.")
    else:
        print(my_name + " is a student.")

#Pass statement: used as a placeholder for future code.
print("\n -------Using pass statement: -------")  
if my_age < 0:
    pass  # Future code to handle negative age will go here 
else:
    print(my_name + "'s age is valid.")     


summary_of_learning_Day1 = """
- Variables are used to store data values and can be created by assigning a value using the equals sign (=).
- Python has various data types, including text, numeric, sequence, mapping, set, boolean, and binary types.
- The print() function is used to display output, and you can customize its behavior using parameters like end.
- You can assign multiple values to multiple variables in one line and print multiple variables together.
- The type() function helps determine the data type of a variable, and type casting allows you to convert variables to specific data types.
- Conditional statements (if, elif, else) are used to execute code based on specific conditions, and shorthand if...else can be used for concise conditional assignments.
- Logical operators (and, or, not) allow you to combine multiple conditions in your statements.
- Nested if statements enable you to check conditions within other conditions.
- The pass statement serves as a placeholder for future code, allowing you to define empty blocks without causing syntax errors.
"""
print("\n\n------------------End of Day 1 Summary-----------------:", summary_of_learning_Day1)
