"""Module focused on python course of Alura"""

from challenges.between_break_lines import between_break_lines

print("Sabor Express\n")
options = [
    "1. Register restaurant",
    "2. List restaurant",
    "3. Activate restaurant",
    "4. exit",
]
between_break_lines(options)
selected_option = input("select one option:")
print(f"You select: {selected_option}\n")
# Actually we have a better way to do that
if selected_option == "1":
    print(options[0])
elif selected_option == "2":
    print(options[1])
elif selected_option == "3":
    print(options[2])
else:
    print(options[3])
