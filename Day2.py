#LEARN PYTHON : DAY 2
#Topics: Data Structures - Lists part 1 [Definition, Accessing, Modifying, Adding, Sorting, Checking]
#Resources: https://www.w3schools.com/python/default.asp
#Date: 9 December 2025

#Data Structures is about how data can be stored in different structures.
#In Python, we have several built-in data structures such as lists, tuples, sets, and dictionaries.
#List: An ordered, allow duplicate values, mutable (changeable), collection of items. Lists are defined using square brackets [].

print("List in Python:")
person_fav_items = ["Netflix Series", "10", "Traveling"]

#print list items
print(person_fav_items)

#print first item of the list
print(person_fav_items[0])

print("\n------------------Sort List Item -----------------")
#sort the list and print the updated list
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
person_fav_items.sort(reverse= True)
print(person_fav_items)
person_fav_items.sort() 
print(person_fav_items)
#The reverse() method reverses the current sorting order of the elements.
person_fav_items.reverse() 
print(person_fav_items)
#case-insensitive sort function, use str.lower as a key function
fav_bird = ["great tit", "Magpie", "dove"]
fav_bird.sort(key= str.lower)
print(fav_bird)


print("\n ---------list length and type----------") 
print(len(person_fav_items))
print(type(person_fav_items))

print("\n\n------------------ADD LIST ITEMS -----------------")

#Add item at the end of the list
person_fav_items.sort()
person_fav_items.append("Nature")
print(person_fav_items)

#Add item at the specific index of the list
person_fav_items.insert(1, "Birds")
print(person_fav_items)

#Append another list at the end of the list
fav_makeup_items = ["Lipstick", "Eyeliner"]
person_fav_items.extend(fav_makeup_items)
print(person_fav_items)

#add any iterable object (tuples, sets, dictionaries etc.) at the end of the list
fav_fruits =("Kiwi", "Apple")
person_fav_items.extend(fav_fruits)
print(person_fav_items)

print("\n\n------------------Change List Item -----------------")
#Change specific one Item
person_fav_items[0] = "7"
print(person_fav_items)

#Change a range of list items
fav_fruits_secondlist = ["Orange", "Banana"]
person_fav_items[7:9] = fav_fruits_secondlist
print(person_fav_items)

# The length of the list will change when the number of items inserted does not match the number of items replaced.
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly


print("\n\n------------------Access List Items -----------------")
print(person_fav_items) ##will print 7, 'Birds', 'Netflix Series', 'Traveling', 'Nature', 'Lipstick', 'Eyeliner', 'Orange', 'Banana'
print(person_fav_items[1:3]) #will print Birds, Netflix series
print(person_fav_items[:3]) #will print 7, Birds, Netflix series
print(person_fav_items[1:]) #will print 'Birds', 'Netflix Series', 'Traveling', 'Nature', 'Lipstick', 'Eyeliner', 'Orange', 'Banana'
print(person_fav_items[-1]) #will print Banana
print(person_fav_items[-4:-1]) #will print 'Lipstick', 'Eyeliner', 'Orange'

print("\n\n------------------Check from List Item with conditions-----------------")
#Check if item exist in the list
fruit = input("What's your fav fruit?")
if fruit in fav_fruits:
    print("YAAY! we have a common fav fruit!")
else:
    print("Nice!")
    print("My fav are:", fav_fruits)

summary_of_learning_Day2 = """
- Lists are ordered, mutable (changeable), and allow duplicate values.
- Lists are defined using square brackets [].
- You can access list items using their index, and you can also use slicing to access a range of items.
- You can add items to a list using append(), insert(), and extend() methods.
- You can change list items by specifying the index or a range of indices.
- You can sort and reverse lists using sort() and reverse() methods.
- You can check if an item exists in a list using the 'in' keyword.
"""
print("\n\n------------------End of Day 2 Summary-----------------:", summary_of_learning_Day2)