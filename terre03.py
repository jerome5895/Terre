# Import module
import sys

# Convert variable to a number
letter_from = ord(sys.argv[1])

# Establishment the rest of the alphabet
alphabet = range((letter_from), (123))
 
# Programm that displays the alphabet from the letter given as an argument in lowercase letters followed by a newline
for letter in alphabet:
    print(chr(letter), end="")

print()