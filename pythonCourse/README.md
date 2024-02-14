# Python Course

This is a repository dedicated to learn about python syntax deeply.

## Configuration

To configure your project you can need to follow these steps:

1. init a virtual environment:
    ```shell
    python3 -m venv .venv
    ```

2. (OPTIONAL) if you use vscode you can press `COMMAND + SHIFT + P` then type `select interpreter` select that option and select the interpreter on `.venv` directory 
to allow the terminal to use the python created in your virtual environment.

3. read the `/requirements.txt` to install the requirements.

## Chapters

Is where we can understand each knowledge separated in different topics in python.

### Strings

In python you can declare a string with single quote, or double quote.
The type of string in python is `str`.

You can concatenate strings with + as any based on `c` language can.
Also, you can use formatted string using:
```py
variable = "test"
formatted = f"{variable} formatted" # -> "test formatted"
```
Also you can prompt to the user asking him to input some value, this can be done using the `input(message_input)` function

### If/else

In python the if/else statement is due like this:
```py
if condition:
   # do something
  elif another_condition:
    # do another thing
  else:
    # Another thing too, and the last in this if/else statement
```

### Types

Python is a strongly typed language, and because of this, you cannot compare, two different types.
See the example below :
```py
my_number = 1
my_input = input('type a number:') # this is a str anyway
print(isinstance(my_input,str)) # -> True
if my_input == '1':
  print(my_input ==my_number) # -> False

```

To see the type of a variable you can use `type(variable)`

To convert types you can use something like this `int(variable)` or `str(variable)`.
> This is valid for any type in python

### Functions and imports

To declare a function you can follow the syntax `def function_name(param1,param2)`

To import some functions from a build in library in python you can use
`import library_name`

To declare the main function (Others files cannot import anything from this file), you can follow the example in below:

```py
if __name__ == '__main__':
    # run the main functionality
```
### Conditionals

Other conditional used in python is the syntax match/case

```py
 match variable:
    case condition_1:
      # do something
    case condition_2:
      # do another thing
    case _:
      # default (no match any case above)
```

### Try/except

The block `try/except` syntax is:

```py
try:
  #do something
except:
  # Something go wrong

# you can also catch the exception by doing something like this:
try:
  # Do another thing
except Exception as exception:
  # do something with the exception info
```
>[!NOTE]
> Another thing that you may want to use is the `assert` instruction, that allows you to assert a condition, and case the instruction returns False, the **assertion** will **raise** a error. Let's see a example:
> 
> ```python
> number = int(input("type a number"))
> assert 0<= number <=10,"The number must be in the interval between 0 and 10."
> ```
### Lists

To declare a list is pretty common. just declare the variable with a `[]`

To loop in a list you can use the `for`loop:

```py
my_list = ["example_1","example_2"]
for item in my_list:
  print(item) # -> Prints the current item (example_1 or example_2)
```

You can also use the enumerate(list) to get the index in your list
```py
my_list = ["example_1","example_2"]
for index,item in enumerate(my_list):
  print(item,index) # -> Prints the current item with the current index (example_1 0 or example_2 1)
```

Some examples on this chapter may require to make a summation of a list of numbers.
Actually python has this already made, the function name is sum, and you can pass to it a list of numbers,
making more easy doing that kind of stuff.

>[!TIP]
> ### Filters
> The filter syntax in python currently is more comprehensible than others languages, see the example below:
> ```py
> films = [{"name":"teste1","year":2000},{"name":"teste2","year":2009},{"name":"teste1","year":2020}]
> old_films = [film for film in films if film["year"]<=2010] # returns a list with test1 and test2 inside
> ```
### Dicionaries

Dicionaries are the a variable type that have properties that can be
accessed with `variable["property"]` or `variable.get('property')` very much like objects, but with some differences

To declare a dictionary you can follow the example below:

```py
variable = { 'key':'value'}
print(variable['key']) # -> 'value'
for value in variable:
    print (value) # -> 'value'
variable.update({'key':'another_value'})  
print(variable.get('key')) # -> 'another_value'
```
>[!NOTE]
> - update method allow us to update existent keys in our dictionary 
> - get method allow us to get a value from a key in our dictionary
> - You cannot update a value from dictionary by doing something like this `dictionary.key = value`


### Docstring

Docstring provides documentation for your modules, functions and classes. Highly recommended for methods that you'll reuse after a while.

- Need to be in the first line of the module, function or class
- is implemented between """ and can be multiline in that way.

## Object orientation Paradigm (OOP)
This is a powerful paradigm of programming that is used in the whole world, and you will take some contact with that in this course.
### Classes

Classes are the fundamental building blocks of object-oriented programming in Python.
They allow you to define a blueprint for creating objects with their own properties and behaviors.
By using classes, you can organize your code into reusable and modular components.

To create a class in python, it's simple:

```py
class YourClassName :
    property_1:''
    property_2:2
    property_3:False

```
#### Instances

To create a instance you can use ` instance_obj = YourClassName()
But that is not all, you can access properties, and update those properties:

```py
class YourClassName :
    property_1='test'
    property_2=2
    property_3=False

instance = YourClassName()
print(instance.property_1) # -> throws a error
instance.property_1 = 'new atribute'
print(instance.property_1) # -> 'new atribute'

```
>[!NOTE]
> You can see all atributes of a class using `dir(instance)` that return a dictionary 
> including default ones (all classes have those, something like `__shared_property__`).
>
> You can also see all atributes uniques of a class using `vars(instance)` that return a dictionary only with attributes of the instance of that class.

### Constructors

Constructors turn classes into instances, basically is the function that will be called when the instance is created.
Let's see an example of how to customize the constructor of a class:

```py
class YourClassName :
    property_1=''
    property_2=int
    property_3=False
    def __init__(self,property_1,property_2): # The constructor of that class
        self.property_1 = property_1 
        self.property_2 = property_2
instance = YourClassName(property_1='first',property_2='second')
print(instance.property_1) # -> 'first'
print(instance.property_3) # -> False (default attribution )

```
>[!NOTE]
> The self means the scope of the class, where self is a reference to the current instance.
> You always must pass self in the first parameter in a instance method.

### Methods
Methods are functions that a Class can use to provide to the instance the rules applied to them
You can think that is what your instance can do.

#### Special Methods

In classes we have some special methods that we can use for different purposes, one example is the
`__init__` method that is responsible to create the class instance.
In the `special methods section` we have contact with the following methods:

- `__str__`: responsible to the result when the instance is converted to string (like in `print(instance)`)
    ```py
    #... class YourClassName
    __str__(self):
        print(f"\{p1:{self.property_1},p2:{self.property_2},p3:{self.property_3}\}")
  instance = YourClassName(instance = YourClassName(property_1='first',property_2='second')
  print(instance) # -> {p1:'first',p2:'second',p3:False}
    ```
#### Method definition

Methods can be private to the Class, meaning that only instances of that class can use them.
An example can be the method `__str__`, that only instances of a class have access.
Methods can also be public, meaning that anyone can call that method.

Also, methods can be created to attend your needs, see the following example:

```py
import math
class Point:
  __init__(self,x:Float,y:Float):
      self.x = x
      self.y = y
  __str__(self):
      print(f"({self.x},{self.y})")
  module(self):
      point_module = math.sqrt(self.x**2+self.y**2)
      return point_module
point = Point(x=2.0,y=2.0)
print(point) # -> (2,2)
print(point.module()) # -> 2
```
#### Private methods

Private methods is visible only for the class, and cannot be accessed by instances or inherited classes.
To create a private method you need to add `__` before the method name.

>[!TIP]
>example : 
> ```py
> # test.class.py
> class Test:
>   def __init(self):
>     self.property_1 = self.__do_something_internally()  
>   def __do_something_internally(self):
>       # do something ...
>
> # main.py  
> test = Test()
> test.__do_something_internally() # raises an error
> ``` 

#### @property
This is a decorator for manage a property in the class.
you can easily add that expression in the code and your class will can handle the property accordingly your need.

```py
class NewClassWithDecoratorProperty:
    a = 1
    _b = False
    c = ''
    def __init__(self, a,c):
      self.a=a
      self._b=False
      self.c = c
    def __str__(self):
      return (self.a,self._b,self.c)
    @property
    def b(self):
      return "ok" if self._b is True else "not ok"
test = NewClassWithDecoratorProperty(a=2,c="test")
print(test) # -> 2 ok test
```

>[!TIP]
> That decorator is useful for situations where your code need to send a different information based in others parameters. Or you need to access a protected information in your class in your class instance

#### @classmethod and @staticmethod

Both are **decorators** in python, but each one has a unique reason to exist.

- The **@classmethod** is responsible to provide to the method created with him access only for the class itself or the object that represents the class.
Which means that a method created with that decorator cannot change atributes from the instance of that class. But it can change atributes from the class.

- The **@staticmethod** cannot access any information about the class were it was defined, by doing this, static methods decorator turn the method just a namespace in that class.

Example:
```py
class Test:
  property_1='Class property'
  def __init__(self,instance_property):
    self.instance_property = instance_property
  @classmethod
  def class_method(cls): # cls is the object that represents the class
    print(cls.property_1) # -> 'Class property'
    # print(self.instance_property) -> raises an error
    # because that method cannot have access to the instance property. 
    cls.property_1='abc'
  
  @staticmethod
  def static_method(prop_1): # cannot access any information about the class
    # can be accessed outside a class instance
    print(prop_1) # the property passed to that static method
    # print(self) -> raises a error, self not exists in that scope
    # print(property_1) -> raises a error, this variable not exists in that scope
test = Test(instance_property='instance')
# -> prints 'test outside' in the console
Test.static_method('test outside') # (not a class instance)
# -> prints 'test.property_1' in the console
Test.class_method() # (not a class instance)
test.static_method('test inside') # -> prints 'test inside' in the console
test.class_method() # -> prints the test.property_1 value
``` 

>[!TIP]
>we have a section about decorators [here](#decorators).
### Decorators
<!-- TODO : Provide a understandable documentation about decorators in Python -->

