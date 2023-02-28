# import module to extract argument
import sys

# convert variable to a number
letter_from = ord(sys.argv[1])

# establishment the rest of the alphabet
alphabet = range((letter_from), (123))
 
# a programm that displays the alphabet from the letter given as an argument in lowercase letters followed by a newline
for letter in alphabet:
    print(chr(letter), end="")