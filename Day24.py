#LEARN PYTHON : DAY 24
#Topics: Lambda Functions
#Resources: 
# https://www.w3schools.com/python/python_lambda.asp
# https://www.geeksforgeeks.org/python/python-lambda-anonymous-functions-filter-map-reduce/


#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Lambda functions are commonly used with built-in functions like map(), filter(), and sorted()
#In Python, both lambda and def can be used to define functions, but they serve slightly different purposes. While def is used for creating standard reusable functions, lambda is mainly used for short, anonymous functions that are needed only temporarily.

def add(x):
    return lambda a : a + x

user_val = int(input("Enter the integer:"))
result = add(user_val)
print(result(100))

#Use Cases of Lambda Functions

#Condition checking-------------------------------------------
value_check = lambda a : "Even number" if a%2 == 0 else "Odd number"
print(value_check(user_val))

#Using with List Comprehension----------------------------------------
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())


#Using for Returning Multiple Results------------------------------------
#Lambda functions do not allow multiple statements, however, we can create two lambda functions and then call the other lambda function as a parameter to the first function.
#The lambda function performs both addition and multiplication and returns a tuple with both results.
#This is useful for scenarios where multiple calculations need to be performed and returned together.
num_cal = lambda x,y : (x+y, x-y)
final_result = num_cal(20, 30)
print(final_result)

#Using with filter()----------------------------------
#filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence "sequence", for which the function returns True.
num_list = [90, 3, 55, 85, 980]
even_num = filter(lambda x : x % 2 == 0, num_list)
print(list(even_num))

#Using with map()------------------------------------
#map() function in Python takes in a function and a list as an argument. The function is called with a lambda function and a new list is returned which contains all the lambda-modified items returned by that function for each item.
num_list2 = [90, 3, 55, 85, 980]
updated_num = map(lambda x : x * 100, num_list2)
print(list(updated_num))


#Using with reduce()----------------------------------
from functools import reduce
num_list2 = [90, 3]
result = reduce(lambda x ,y : x * y, num_list2)
print(result)

