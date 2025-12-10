#LEARN PYTHON : DAY 3
#Topics: Data Structures - Lists part 2 [List Looping, List Comprehension, List Copy, List Join, List Remove Item]
#Resources: https://www.w3schools.com/python/default.asp
#Date: 10 December 2025

print("------------------For Loop List Item with range function -----------------")
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
fav_bird = ["great tit", "Magpie", "dove", "duck"]
num_fav_bird = len(fav_bird)
print(num_fav_bird)
for i in range(num_fav_bird):
    print(fav_bird[i])



print("\n------------------For Loop List Item without range function/ indexing -----------------")
#For Looping Through a List
for i in fav_bird:
    print(i)



print("\n------------------While Loop List Item -----------------")
#While Looping Through a List
i= 0
while i < len(fav_bird):
    print(fav_bird[i])
    i = i+1



print("\n------------------Looping Using List Comprehension -----------------")
# Syntax: newlist = [expression for item in iterable if condition == True]
[print(i) for i in fav_bird]

print("\n------------------List copy -----------------")
#copy()
#list()
#slicing methods

new_bird_list = fav_bird.copy()
print(new_bird_list)

print("\n------------------List Join -----------------")
#+ operator
#extend()
#adding another list items with loop one by one

new_bird_list2 = fav_bird + new_bird_list
print(new_bird_list2)


print("\n------------------Remove List Item -----------------")
#The remove() method removes the specified item.If there are more than one item with the specified value, the remove() method removes the first occurrence.
#The pop() method removes the specified index. If you do not specify the index, the pop() method removes the last item.
#The del keyword also removes the specified index
#The del keyword can also delete the list completely.
#The clear() method empties the list.

print(new_bird_list2)
new_bird_list2.pop()
print(new_bird_list2)
new_bird_list2.pop(0)
print(new_bird_list2)
new_bird_list2.remove("dove")
print(new_bird_list2)
del new_bird_list2[1]
print(new_bird_list2)
new_bird_list2.clear()
print(new_bird_list2)

summary_of_learning_Day3 = """
1. Looping through a list using for loop with and without range function.
2. Looping through a list using while loop.
3. Looping through a list using list comprehension.
4. Copying a list using copy() method.
5. Joining two lists using + operator and extend() method.
6. Removing list items using remove(), pop(), del keyword, and clear() method.
"""
print("\n\n------------------End of Day 3 Summary-----------------:", summary_of_learning_Day3)