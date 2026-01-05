#LEARN PYTHON : DAY 23
#Topics: Modules and Packages
#Resources: 
# https://www.w3schools.com/python/python_modules.asp
# https://www.geeksforgeeks.org/python/python-packages/


#Modules: A module is a file containing Python code that can define functions, classes, and variables. It allows you to organize your code into manageable sections.
#You can create your own modules or use built-in and third-party modules.


print("-----------Creating and Using Modules in Python---------------")
#Creating a Module:
#To create a module, simply save the code you want in a file with a .py extension.
#For example, create a file named mymodule.py with the following content:
# mymodule.py

#Using a Module:
#To use a module, you need to import it into your script using the import statement.
import mymodule
result = mymodule.greet("Alice")
print(result)

"""
#You can also import specific functions or classes from a module using the from keyword.
from mymodule import greet
result = greet("Bob")
print(result)


#Packages: A package is a way of organizing related modules into a directory hierarchy. A package is simply a directory that contains a special file named __init__.py, which indicates to Python that the directory should be treated as a package.
#You can create sub-packages and modules within a package to further organize your code.
print("\n-----------Creating and Using Packages in Python---------------")
#Creating a Package:
#To create a package, create a directory and add an __init__.py file to it. You can then add modules to the package by creating additional .py files in the directory.
#For example, create a directory named mypackage with the following structure:
# mypackage/
#     __init__.py
#     module1.py
#     module2.py
#Using a Package:
#To use a package, you need to import it into your script using the import statement.
from mypackage import module1, module2
result1 = module1.function1()
result2 = module2.function2()
print(result1)
print(result2)
"""