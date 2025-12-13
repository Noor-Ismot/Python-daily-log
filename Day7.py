#LEARN PYTHON : DAY 7
#Topics: Dictionary [Defining, Accessing, Adding, Updating, Checking, Removing, Copying, Looping]
#Resources: https://www.w3schools.com/python/default.asp
#Date: 14 December 2025

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates[Duplicate values will overwrite existing values]. Dictionaries are written with curly brackets, and have keys and values

print("-----------Defining Dictionary, type, len---------------")
person_detail = {
    "name": "Johanson",
    "age" : 32,
    "height": 5.08,
    "fav_fruits" : ["Kiwi", "apple", "mango"]
}
print(person_detail)
print(type(person_detail))
print(len(person_detail))


print("\n-----------Access Dictionary---------------")
print(person_detail["fav_fruits"])
print(person_detail.get("fav_fruits"))
print(person_detail.keys())
print(person_detail.items())

print("\n-----------Add new Items or Update items to Dictionary---------------")
print(f"Main dictionary: {person_detail}")
person_detail["weight"] = 45 #add new key-value
print(f"Updated dictionary: {person_detail}")
person_detail["weight"] = 56.67 #updated value of weight key
print(f"Updated dictionary: {person_detail}")

#The update() method will update the dictionary with the items from the given argument.The argument must be a dictionary, or an iterable object with key:value pairs.
person_detail.update({"height": 6.01})
print(f"Updated dictionary with method function: {person_detail}")

person_detail.update({"color": "brown"})
print(f"Updated dictionary with method function: {person_detail}")

print("\n-----------Check item in Dictionary---------------")
if "height" in person_detail: print(f"Height has been found: {person_detail['height']}") 

print("\n-----------Remove Items from Dictionary---------------")
person_detail.update({"face_shape":"round"})
print(person_detail)

person_detail.pop("face_shape")
print(person_detail)

person_detail.popitem()
print(person_detail)

del person_detail["weight"]
print(person_detail)
#The del keyword can also delete the dictionary completely

person_detail.clear()
print(person_detail)


print("\n-----------Copy a Dictionary---------------")
person_detail = {
    "name": "Johanson",
    "age" : 32,
    "height": 5.08,
    "fav_fruits" : ["Kiwi", "apple", "mango"]
}

#one way is to use the built-in Dictionary method copy()
new_person_detail = person_detail.copy()
print(new_person_detail)

#Another way to make a copy is to use the built-in function dict()
classmate_detail = dict(new_person_detail)
print(classmate_detail)


print("\n-----------Looping through Dictionary---------------")
print(classmate_detail)

#Print all values in the dictionary, one by one
for i in classmate_detail:
    print(f"Values: {classmate_detail[i]}") #printing all values

print("----------------")
for i in classmate_detail.values():
    print(f"Value: {i}") #printing values one by one

print("----------------")
#Print all keys in the dictionary, one by one
for i in classmate_detail:
    print(f"key:{i}") #printing keys

print("----------------")
#Print all keys and values in the dictionary one by one
for i in classmate_detail.keys():
    print(f"key:{i}") #printing keys one by one

print("----------------")
#Print all keys and values in the dictionary one by one
for i in classmate_detail.items():
    print(f"key, value:{i}") #printing key-value one by one



summary_of_learning_Day7 = """
- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
- Dictionaries are written with curly brackets, and have keys and values
- Defining a dictionary using curly braces {}
- Accessing dictionary values using key names or get() method
- Adding new items or updating existing items in a dictionary
- Checking if a key exists in a dictionary
- Removing items from a dictionary using pop(), popitem(), del, and clear() methods
- Copying a dictionary using copy() method and dict() function
- Looping through a dictionary to access keys, values, and key-value pairs

"""
print("\n\n------------------End of Day 7 Summary-----------------:", summary_of_learning_Day7)