#LEARN PYTHON : DAY 26
#Topics: JSON File handling
#Resources: 
# https://www.w3schools.com/python/python_json.asp

#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.Python has a built-in package called json, which can be used to work with JSON data.

import json


#Convert a python dictionary to json
person = {
    "Name" : "Alice",
    "Age" : 65,
    "Height" : 155.6,
    "Blood group" : "B+",
    "Retired" : True
}

y = json.dumps(person, indent=4, sort_keys=True)
print(y)

#Convert a json string to Python code

j_str_text =  '{ "name":"John", "age":30, "city":"New York"}'
z = json.loads(j_str_text)
print(type(z))
print(z)