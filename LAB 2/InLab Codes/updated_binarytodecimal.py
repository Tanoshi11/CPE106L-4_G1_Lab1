"""
File: binarytodecimal.py
Converts a string of bits to a decimal integer.
"""

# UPDATED #

# Validate the input to allow only binary numbers
while True:
    bstring = input("Enter a string of bits (only 0s and 1s): ")
    if all(char == '0' or char == '1' for char in bstring):  # Check if every character is 0 or 1
        break  # Exit the loop if the input is valid
    print("Invalid input! Please enter only 0s and 1s.")

# Main code starts here
decimal = 0
exponent = len(bstring) - 1
for digit in bstring:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)
