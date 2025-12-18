#LEARN PYTHON : DAY 10
#Topics: File Handling
#Resources: https://www.w3schools.com/python/default.asp
#Date: 17 December 2025

print("-----------File---------------")

#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
#There are four different methods (modes) for opening a file:
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists


#The open() function returns a file object, which has a read() method for reading the content of the file:
"""
f = open("testpythonFile.txt")
print(f.read())
f.close()

#Another way to open and read and close a file
with open("testpythonFile.txt") as f:
    print("First Two Characters:")
    print(f.read(2)) #to read characters

#Another way to open and read lines in a file
with open("testpythonFile.txt") as f:
    print("Whole Text:")
    print(f.readlines()) #to read characters

with open("testpythonFile.txt") as f:
    print("Looping through the file:")
    for x in f:
        print(x)


with open("testpythonFile.txt", "a") as f:
    f.write("New Line has been added")

with open("testpythonFile.txt") as f:
    print(f.readlines())


#"w" - Write - will overwrite any existing content

#with open("testpythonFile.txt", "w") as f:
    #f.write("New Line has been added")

"""

summary_of_learning_Day10 = """
- Learned how to handle files in Python using the open() function with different modes such as read, append, write, and create.
- Understood how to read from files using methods like read() and readlines(), and how to loop through file content.
- Practiced writing to files using append and write modes, and observed the differences in behavior between them. 
"""
print("\n\n------------------End of Day 10 Summary-----------------:", summary_of_learning_Day10)