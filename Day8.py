#LEARN PYTHON : DAY 8
#Topics: String [Defining, Accessing, Slicing, Modifying, Methods, concatenation, formatting]
#Resources: https://www.w3schools.com/python/default.asp
#Date: 15 December 2025

#A string is a collection of one or more characters put in a single quote, double-quote or triple quote. Strings are immutable i.e. they cannot be changed after they are created. Strings are ordered i.e. we can access the characters using indexing.

print("-----------Defining String, type, len---------------")
my_string = "Hello, welcome to Learn Python"
print(my_string)
print(type(my_string))
print(len(my_string))
print("\n-----------Accessing String---------------")
print(my_string[0]) #First character
print(my_string[-1]) #Last character
print(my_string[7:14]) #Slicing from index 7 to 13
print(my_string[:5]) #Slicing from start to index 4
print(my_string[18:]) #Slicing from index 18 to end

print("\n-----------Modifying String---------------")
my_string_upper = my_string.upper()
print(f"Original String: {my_string}")
print(f"Uppercase String: {my_string_upper}")
my_string_replace = my_string.replace("Learn Python", "Master Python")
print(f"Replaced String: {my_string_replace}")

print("\n-----------String Methods---------------")
print(f"Find 'welcome' in string at index: {my_string.find('welcome')}")
print(f"Count of 'o' in string: {my_string.count('o')}")
print(f"Is the string alphanumeric? {my_string.isalnum()}")
print(f"Does the string start with 'Hello'? {my_string.startswith('Hello')}")
print(f"Does the string end with 'Python'? {my_string.endswith('Python')}")
print(f"Split the string by spaces: {my_string.split(' ')}")
print(f"Strip whitespace from string: {'   Hello World   '.strip()}")
print(f"Join characters with '-': {'-'.join(['L', 'e', 'a', 'r', 'n'])}")
print(f"Capitalize the string: {my_string.capitalize()}")
print(f"Title case the string: {my_string.title()}")
print(f"Swap case of the string: {my_string.swapcase()}")
print(f"Check if string is numeric: {'12345'.isnumeric()}")
print(f"Check if string is alphabetic: {'HelloWorld'.isalpha()}")
print(f"Check if string is lowercase: {my_string.islower()}")
print(f"Check if string is uppercase: {my_string.isupper()}")
print(f"Count of 'e' in string: {my_string.count('e')}")
print(f"Find index of 'Python' in string: {my_string.index('Python')}")
print(f"Replace 'welcome' with 'greetings': {my_string.replace('welcome', 'greetings')}")
print(f"Center the string with '*': {my_string.center(40, '*')}")

print("\n-----------String Concatenation and Formatting---------------")
str1 = "Learn"
str2 = "Python"
concatenated_str = str1 + " " + str2
print(f"Concatenated String: {concatenated_str}")
formatted_str = f"{str1} - {str2} is fun!"
print(f"Formatted String: {formatted_str}")
print("Using format method: {} - {} is fun!".format(str1, str2))


summary_of_learning_Day8 = """
- Defined strings using single, double, and triple quotes.
- Accessed string characters using indexing and slicing.
- Modified strings using methods like upper(), replace().
- Explored various string methods: find(), count(), isalnum(), startswith(), endswith(), split(), strip(), join(), capitalize(), title(), swapcase(), isnumeric(), isalpha(), islower(), isupper(), index().
- String concatenation using + operator.
- String formatting using f-strings and format() method.
- Strings are immutable and ordered collections of characters.

"""
print("\n\n------------------End of Day 8 Summary-----------------:", summary_of_learning_Day8)