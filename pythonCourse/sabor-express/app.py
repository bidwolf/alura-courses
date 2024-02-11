"""Module focused on python course of Alura"""


def between_break_lines(word: str) -> None:
    """Print each letter of the word between break lines"""
    for letter in word:
        print(f"{letter}\n")


print("Sabor Express\n")
options = [
    "1. Cadastrar restaurante",
    "2. Listar restaurante",
    "3. Ativar restaurante",
    "4. Sair",
]
between_break_lines(options)
selected_option = input("select one option:")
print(f"You select: {selected_option}\n")

print("Python on Alura Programming School \n")

# Usando loop
between_break_lines("ALURA")

# Usando Sep
print("A", "L", "U", "R", "A", sep="\n")

PI = 3.14159

# Usando Round
print(f"{round(PI, 2)}")
# Usando o método f-string
print(f"{PI:.2f}")
# Usando f-string
print(f"{PI:.2f}")

NAME = "Henrique de Paula Rodrigues"
AGE = 23
