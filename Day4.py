#LEARN PYTHON : DAY 4
#Topics: Range function and Loops [For Loop, While Loop with break, continue, else, pass statements]
#Resources: https://www.w3schools.com/python/default.asp
#Date: 11 December 2025


print("\n------------------Range function -----------------")
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#start	Optional. An integer number specifying at which position to start. Default is 0
#stop	Required. An integer number specifying at which position to stop (not included).
#step	Optional. An integer number specifying the incrementation. Default is 1
my_laptop_brands =["Dell", "HP", "Acer", "Samsung", "Lenovo"]
print([my_laptop_brands[i] for i in range(2)])
print([my_laptop_brands[i] for i in range(1, 3)])
print([my_laptop_brands[i] for i in range(0, 5, 2)])



print("------------------For Loop, Break, continue statement, else in for loop, pass in for loop -----------------")
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#The for loop does not require an indexing variable to set beforehand.
#Python does not support inline break or continue statements.
#Looping Through a String
print("For Loop with break statement")
my_laptop_brand = "DELA"
for i in my_laptop_brand:
    if i == "L": break #With the break statement we can stop the loop before it has looped through all the items
    print(i) 
    

print("For Loop with continue statement")
my_laptop_brand = "HLP"
for i in my_laptop_brand:
    if i == "L": continue #With the continue statement we can stop the current iteration of the loop, and continue with the next
    print(i) 

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished
#The else block will NOT be executed if the loop is stopped by a break statement.
print("For Loop with range function")
for x in range(6):
  print(x)
else:
  print("Finally finished!")


print("For Loop with pass statement")
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass # having an empty for loop like this, would raise an error without the pass statement



print("\n------------------While Loop, break, continue, else statement -----------------")
#With the while loop we can execute a set of statements as long as a condition is true.
#remember to increment i, or else the loop will continue forever.
#With the break statement we can stop the loop even if the while condition is true
#With the continue statement we can stop the current iteration, and continue with the next
my_laptop_brand = "DELL"
i = 0
while i< len(my_laptop_brand):
   print(my_laptop_brand[i])
   i = i+1



print("While Loop with break statement")
i = 0
while i< len(my_laptop_brand):
   if my_laptop_brand[i] == "E" :
      break
   print(my_laptop_brand[i])
   i = i+1



print("While Loop with continue statement")
i = 0
while i< len(my_laptop_brand):
   if my_laptop_brand[i] == "E" :
      i = i+1 #Always increment your loop counter before using continue in a while loop to avoid an infinite loop.
      continue
   print(my_laptop_brand[i])
   i = i+1

summary_of_learning_Day4 = """
1. The range() function generates a sequence of numbers, which can be customized using start, stop, and step parameters.
2. For loops are used to iterate over sequences such as lists, strings, and more, without needing an indexing variable.
3. The break statement can be used in loops to exit the loop prematurely when a certain condition is met.
4. The continue statement allows skipping the current iteration of a loop and moving to the next iteration.
5. The else clause in loops executes a block of code when the loop completes normally, but not if it is terminated by a break statement.
6. While loops execute a block of code as long as a specified condition is true, and require careful management of loop counters to avoid infinite loops.
7. The pass statement can be used as a placeholder in loops to avoid syntax errors when no action is needed.
"""
print("\n\n------------------End of Day 4 Summary-----------------:", summary_of_learning_Day4)