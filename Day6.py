#LEARN PYTHON : DAY 6
#Topics: Tuple [Defining, Accessing, Updating, Unpacking, Looping, Joining, Methods]
#Resources: https://www.w3schools.com/python/default.asp
#Date: 13 December 2025

#Tuples are used to store multiple items[in different types] in a single variable.
#A tuple is a collection which is ordered and unchangeable and allow duplicate values.
#Tuples are written with round brackets.


print("-----------Defining Tuples, type, len, print tuples---------------")
my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
my_fav_birds = ("parrot",) #To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

print(type(my_fav_fruits))
print(f"My fav fruits are: {my_fav_fruits}")
print(type(my_fav_birds))
print(f"My fav birds are: {my_fav_birds}")
print(f"Length of the bird tuple is: {len(my_fav_birds)}")


print("\n-----------Access Tuples with slicing---------------")
print(f"My fav fruits are: {my_fav_fruits}")
print(my_fav_fruits[1:])
print(my_fav_fruits[1:3])
print(my_fav_fruits[:-3]) #first item not included

print("\n-----------Check tuple item if exists---------------")
fruit = input("Your fav fruits? ")
#my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
print("We have similar choice!") if fruit in my_fav_fruits else print("Nice one, I will try!")


print("\n-----------Update Tuple---------------")
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
fruit_list = list(my_fav_fruits)
fruit_list[0] = "Mango"
print(tuple(fruit_list))

print("\n-----------Add new item to the Tuple---------------")
#Add Items: Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple

my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
fruit_list = list(my_fav_fruits)
fruit_list.append("Lime")
print(tuple(fruit_list))

#Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple
my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
other_fruits = ("Lichi",)
my_fav_fruits += other_fruits
print(my_fav_fruits)

print("\n-----------Remove item from the Tuple---------------")
my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
fruit_list = list(my_fav_fruits)
fruit_list.remove("Kiwi")
my_fav_fruits = tuple(fruit_list)
print(my_fav_fruits)

#Or you can delete the tuple completely
my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
del my_fav_fruits
print(my_fav_fruits) #this will raise an error because the tuple no longer exists


print("\n-----------Unpack the Tuple---------------")
my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
(Green, Yellow, Red, Orange,brown) = my_fav_fruits
print(Green)
print(Red)
print(Orange)
print(brown)

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:


my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
print("\n --------With asterick:---------")
(Green, Yellow, *Red) = my_fav_fruits
print(Green)
print(Yellow)
print(Red)


print("\n --------With another asterick way:---------")
my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
(Green, *Yellow, Red) = my_fav_fruits
print(Green)
print(Yellow)
print(Red)

print("\n --------Looping:---------")
my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
for i in range(len(my_fav_fruits)):
    print(my_fav_fruits[i])

print("\n --------Join Tuples:---------")
my_fav_fruits = ("Kiwi", "Banana", "Apple", "Orange","Pineapple")
another_list_fr = ("Lichi", "Green Apple")
total_fruit_list = my_fav_fruits + another_list_fr
print(total_fruit_list)

print("\n --------Multiply Tuples:---------")

total_fruit_list = total_fruit_list*2
print(total_fruit_list)

print("\n --------Tuple Methods:---------")
print(total_fruit_list.count("Kiwi")) #how many times the items can be found
print(total_fruit_list.index("Kiwi")) #display the first index

#Note: There are only two built-in methods that you can use on tuples: count() and index().

summary_of_learning_Day6 = """
- Tuples are ordered, unchangeable, and allow duplicate values.
- Tuples are defined with round brackets ().
- Access tuple items using indexing and slicing.
- Tuples are immutable; to update, convert to a list, modify, and convert back.
- Unpack tuples into variables, using * for excess items.
- Loop through tuples using for loops.
- Join tuples using the + operator and multiply using *.
- Tuple methods: count() and index().
"""
print("\n\n------------------End of Day 6 Summary-----------------:", summary_of_learning_Day6)