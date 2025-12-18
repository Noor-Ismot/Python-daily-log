#LEARN PYTHON : DAY 9
#Topics: Set [Defining, Accessing, Adding, Removing, Joining, Set operations]
#Resources: https://www.w3schools.com/python/default.asp
#Date: 16 December 2025

#A set is a collection which is unordered, unchangeable*[remove items and add new items can be possible], and unindexed, Duplicates are not allowed. In Python sets are written with curly brackets.

print("-----------Defining Set, type, len---------------")
my_fav_flowers = {"Sunflower", "Tulip", 0, True, False}
print(my_fav_flowers)
print(type(my_fav_flowers))
print(len(my_fav_flowers))
#True and 1 is considered the same value. False and 0 are considered as same value

print("\n-----------Access Set Item and check item---------------")
for i in my_fav_flowers:
    print(i)

if "Tulip" in my_fav_flowers: print("Wow! You love tulips!")

print("\n-----------Add new item or Update Set---------------")
#To add one item to a set use the add() method.
my_fav_flowers.add("Lily")
print(my_fav_flowers)


#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.). The update() changes the original set, and does not return a new set.
flowers = ["Rose", "Marigold"]
my_fav_flowers.update(flowers)
print(f"Updated flower set:{my_fav_flowers}")

print("\n-----------Remove item from Set---------------")
print(f"Mlower set:{my_fav_flowers}")

##If the item to remove does not exist,remove() will NOT raise an error.
my_fav_flowers.remove("Tulip")
print(f"Updated flower set after removing:{my_fav_flowers}")

#If the item to remove does not exist, discard() will NOT raise an error.
my_fav_flowers.discard("Rose")
print(f"Updated flower set after removing:{my_fav_flowers}")

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.The return value of the pop() method is the removed item.
print(f"Mlower set:{my_fav_flowers}")
my_fav_flowers.pop()
print(f"Updated flower set after removing:{my_fav_flowers}")

#The del keyword will delete the set completely.Printing This set after deleting will raise an error because the set no longer exists

print("\n-----------Frozen Set---------------")
#frozenset is an immutable version of a set.
#Like sets, it contains unique, unordered, unchangeable elements.
#Unlike sets, elements cannot be added or removed from a frozenset.
#Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.
my_fav_colors = frozenset({"Purple", "Yellow", "Gray"})
print(my_fav_colors)
print(type(my_fav_colors)) 

print("\n-----------Join Sets---------------")

# union() method returns a new set with all items from both sets. We can also use | to join sets
prog_lang = {"Python", "C","C++"}
database_lang = {"SQL","MYSQL"}

total_lang = prog_lang.union(database_lang)
#total_lang = prog_lang | database_lang
print(f"Union set: {total_lang}")

#Join multiple sets: union() or | operator
set_1 = {"A", "B", "C"}
set_2 = {"A","D", "E"}
set_3 = {"F", "G"}
total_alpha = set_1 | set_2 | set_3
print(f"Joined set with multiple set: {total_alpha}")

#Intersection:Keep ONLY the duplicates
#The intersection() method will return a new set, that only contains the items that are present in both sets. 
#You can use the & operator instead of the intersection() method, and you will get the same result. 
# The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set_1 = {"A", "B", "C"}
set_2 = {"A","D", "E"}
#set_3 = set_1.intersection(set_2)
set_3 = set_1 & set_2
print(f"Intersection between set 1 and 2: {set_3}")

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
#You can use the - operator instead of the difference() method, and you will get the same result.
#The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
#The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set_1 = {"A", "B", "C"}
set_2 = {"A","D", "E"}
set_3 = set_1.difference(set_2)
print(f"Difference between set 1 and 2: {set_3}")

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
#The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set_1 = {"A", "B", "C"}
set_2 = {"A","D", "E"}
set_3 = set_1.symmetric_difference(set_2)
print(f"Difference between set 1 and 2: {set_3}")

summary_of_learning_Day9 = """
- Defining Set using curly braces {}
- Accessing Set items using loops and 'in' keyword
- Adding items using add() and update() methods
- Removing items using remove(), discard(), pop() methods
- Frozen Set as immutable set
- Joining Sets using union(), intersection(), difference(), symmetric_difference() methods and operators
- Set operations: union, intersection, difference, symmetric difference
"""
print("\n\n------------------End of Day 9 Summary-----------------:", summary_of_learning_Day9)