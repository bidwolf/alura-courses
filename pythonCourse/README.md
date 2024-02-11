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