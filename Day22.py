#LEARN PYTHON : DAY 22
#Topics: OOP
#Resources: https://www.w3schools.com/python/default.asp

#OOP stands for Object-Oriented Programming.
#Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
#Advantages:
#Provides a clear structure to programs
#Makes code easier to maintain, reuse, and debug
#Helps keep your code DRY (Don't Repeat Yourself)
#Allows you to build reusable applications with less code
#Tip: The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.
#Class & Object: Classes and objects are the two core concepts in object-oriented programming.
#A class defines what an object should look like, and an object is created based on that class.

print("-----------Creating class and Object in Python---------------")
#create class
class fruits:
    shape = "round"

#create objects
apple = fruits()
peach = fruits()
#Each object is independent and has its own copy of the class properties.

print(apple.shape)
print(peach.shape)

print("\n-----------_int_ method in Python class---------------")
# _int_ method in Python
#The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
#With __init__(), you can set initial values when creating the object
#default value can also be set

class fruits:
    price = 40 #class property

    #Methods are functions that belong to a class. They define the behavior of objects created from the class.
    #All methods must have self as the first parameter.
    def __init__(self, name, color, taste, size ="small"):
        self.name = name #Instance Property
        self.color = color
        self.taste = taste
        self.size = size
    
    def total_price(self, frweight, frprice):
        return frweight * frprice
    
    #Methods modifying properties
    def certificate_size(self):
        self.size = "Big" 
        print("Certificate size modified to:", self.size)
    


fruit_1 = fruits("Apple","Red","Normal")
fruit_2 = fruits("Mango","Green","Sour","Medium")

print(fruit_1.name, fruit_1.color, fruit_1.taste, fruit_1.size)
print(fruit_2.name, fruit_2.color, fruit_2.taste,fruit_1.size)

print("\n--------------Modifying Property Value-------------")
#modify property value
print("Original color:",fruit_1.color)
fruit_1.color = "redish"
print("Modified color:", fruit_1.color)

#Delete Property
del fruit_1.size
#print(fruit_1.size) -> will throw error

print("\n--------------Accessing & Modifying class property value-------------")
#accessing class property
print(fruit_1.price)
print(fruit_2.price)

#Modifying class property -> will affect all objects
fruits.price = 60

print(fruit_1.price)
print(fruit_2.price)

print("\n--------------Adding new property to an existing object-------------")

fruit_1.weight = .5   #it will only effect to specific object, not all object
print(fruit_1.weight) 

print("\n--------------Methods with parameters-------------")
print(fruit_1.total_price(4, 30))


print("\n--------------Methods modifying properties-------------")
fruit_3 = fruits("Guava","Sweet","small")
fruit_3.certificate_size()

"""
Other Information:
1. A class can have multiple methods that work together
2. The __str__() method is a special method that controls what is returned when the object is printed
"""


print("\n------------------Python Inheritance-------------------------------------")
"""
- Inheritance allows us to define a class that inherits all the methods and properties from another class.
- Parent class is the class being inherited from, also called base class.
- Child class is the class that inherits from another class, also called derived class.
- We want to add the __init__() function to the child class (instead of the pass keyword)
- To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
- Python also has a super() function that will make the child class inherit all the methods and properties from its parent
"""

class fruit_basket(fruits):
    def __init__(self, name, color, taste, size="small"):
        super().__init__(name, color, taste, size)
        self.shape = "round" #adding a new property to the inherited class

basket_a = fruit_basket("Parron", "Green", "Sweet","Medium")
print(basket_a.name)
print(basket_a.shape)


print("\n------------------Python Polymorphism-------------------------------------")
"""
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
"""
class cat:
    def sound(self):
        return "Meow"
class dog:
    def sound(self):
        return "Bark"
def animal_sound(animal):
    print(animal.sound())

cat1 = cat()
dog1 = dog()
animal_sound(cat1)
animal_sound(dog1)


print("\n------------------Python Encapsulation-------------------------------------")

"""
Encapsulation is one of the fundamental concepts in OOP. It describes the idea of bundling data and methods that work on that data within one unit.
In Python, we denote private properties and methods by prefixing their names with an underscore (_). This indicates that they should not be accessed directly from outside the class.
"""

class computer:
    def __init__(self, cpu, ram):
        self._cpu = cpu  #private property
        self._ram = ram  #private property

    def _config(self):   #private method
        print("Configuration:", self._cpu, self._ram)
comp1 = computer("i7", "16GB")
#Accessing private method from outside the class will throw error
#comp1._config()
#Accessing private property from outside the class will throw error
#print(comp1._cpu)
#However, in Python, this is just a convention and does not prevent access from outside the class. It is a way to indicate that these members are intended for internal use only.
#If you really want to access them, you can do so, but it's generally discouraged.
comp1._config()
print("CPU:", comp1._cpu)
print("RAM:", comp1._ram)



