""" Module for the first challenge about strings"""

from .between_break_lines import between_break_lines

print("Python on Alura Programming School \n")

# Using loop
between_break_lines("ALURA")

# Using Sep
print("A", "L", "U", "R", "A", sep="\n")

PI = 3.14159

# Using Round
print(f"{round(PI, 2)}")
# Using o método f-string
print(f"{PI:.2f}")
# Using f-string
print(f"{PI:.2f}")

NAME = "Henrique de Paula Rodrigues"
AGE = 23
