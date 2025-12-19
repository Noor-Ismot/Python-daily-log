#Problem Solving: Input, Output, Comments (10 Problems)
#Date: 18 December 2025
#New learnings:
#How to take multiple input in one line with split() function
#NoneType data type where None is the only instance of NoneType object. None is a special constant in Python that represents the absence of a value.

#My Solution: Problem 1 ------------------------------------------

name = input("What's your name? ")
print(f"Hello, {name}!")


#My Solution: Problem 2 ------------------------------------------
number_1, number_2 = input("Enter the numbers: ").split()
print(int(number_1) + int(number_2))


#My Solution: Problem 3 ------------------------------------------
input("Write None as user input:") #Taking no input or None as input
print("Learning Python") #display a string 



#My Solution: Problem 4 ------------------------------------------
name, age = input().split()
print(f"My name is {name} and I am {age} years old.")


#My Solution: Problem 5 ------------------------------------------

num_1, num_2, num_3 = input().split()
print(f"{num_1},{num_2},{num_3}")


#My Solution: Problem 6 ------------------------------------------

num = int(input("Enter the number for a multiplication table (1–5): "))
for i in range(1,6):
    print(f"{num} * {i} = {num * i}")


#My Solution: Problem 7 ------------------------------------------
text = input("Enter your text: ")
print(text.upper())


#My Solution: Problem 8 ------------------------------------------
num_1, num_2, num_3 = input().split()
print(num_1)
print(num_2)
print(num_3)


#My Solution: Problem 9 : Not completed------------------------------------------
value_01, value_02 = input("Enter the values to print their type: ").split()
print(type(value_01), type(value_02))


#My Solution: Problem 10 ------------------------------------------
print("Bangladesh, to the east of India on the Bay of Bengal, is a South Asian country marked by lush greenery and many waterways.\nIts Padma (Ganges), Meghna and Jamuna rivers create fertile plains, and travel by boat is common. \nOn the southern coast, the Sundarbans, an enormous mangrove forest shared with Eastern India, is home to the royal Bengal tiger.")
