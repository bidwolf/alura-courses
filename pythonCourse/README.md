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
formatted = f"{variable} formatted" # -> "test formated"
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

### Dicionaries

Dicionaries are the a variable type that have properties that can be
accessed with `variable["property"]` or `variable.property` very much like objects, but with some differences

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