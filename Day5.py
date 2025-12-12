#LEARN PYTHON : DAY 5
#Topics: Function [Defining, Arguments, Default Parameter value, Keyword Argument, Variable Scope, Global Keyword, Return Value, Pass Statement, *args and **kwargs]
#Resources: https://www.w3schools.com/python/default.asp
#Date: 12 December 2025

#A function is a block of code which only runs when it is called. A function can return data as a result. A function helps avoiding code repetition.
#Functions can send data back to the code that called them using the return statement. When a function reaches a return statement, it stops executing and sends the result back
#If a function doesn't have a return statement, it returns None by default.
#Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement
print("--------Defining Function in Python--------------")
def fav_birds_display():
    fav_birds = ["Dove", "Great tit", "Magpie"]
    print(f"My fav birds are: {fav_birds}")

fav_birds_display()


print("\n --------Function Arguments--------------------")
#By default, a function must be called with the correct number of arguments.If your function expects 2 arguments, you must call it with exactly 2 arguments

def fav_bird_display(birds): #parameter
    print(f"My fav birds are: {birds}")

fav_bird_display(["Dove","Magpie"]) #passing argument



print("\n --------Function Default Parameter value----------")

def fav_bird_display(birds = ["Dove", "Parrot"]): #parameter
    print(f"My fav birds are: {birds}")

fav_bird_display()



print("\n --------Function Keyword Argument----------")

def fav_bird_display(birds_name, number): #parameter
    print(f"My fav birds are: {birds_name} and I have {number} {birds_name}")

fav_bird_display(birds_name= "parrot", number = 3)

#The LEGB Rule
#Python follows the LEGB rule when looking up variable names, and searches for them in this order:
#Local - Inside the current function
#Enclosing - Inside enclosing functions (from inner to outer)
#Global - At the top level of the module
#Built-in - In Python's built-in namespace

print("\n --------Function Variable Scope----------")  
x = "global x"  #global variable
def myfunc():
    x = "local x"  #local variable
    print(x)
myfunc()
print(x)

print("\n --------Function Global Keyword----------")
x = "global x"  #global variable
def myfunc():
    global x
    x = "modified global x"  #modifying global variable
    print(x)
myfunc()
print(x)
print("\n --------Function Return Value----------")
def fav_bird_count(birds):
    return len(birds)

bird_list = ["Dove", "Parrot", "Magpie"]
count = fav_bird_count(bird_list)
print(f"I have {count} fav birds.")


print("\n --------Function Pass Statement----------")
def fav_bird_display(birds):
    pass
print("Function with pass statement executed successfully.")

#Python *args and **kwargs
print("\n --------Function *args and **kwargs----------")
def fav_bird_display(*birds): #using *args
    print("My fav birds are:")
    for bird in birds:
        print(bird) 

fav_bird_display("Dove", "Parrot", "Magpie")

print("\n --------Function **kwargs----------")
def fav_bird_display(**bird_info): #using **kwargs
    print("Bird Information:")
    for key, value in bird_info.items():
        print(f"{key}: {value}")

fav_bird_display(name="Dove", color="White", habitat="Urban Areas")


summary_of_learning_Day5 = """
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

"""
print("\n\n------------------End of Day 5 Summary-----------------:", summary_of_learning_Day5)