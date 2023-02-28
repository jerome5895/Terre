# Import module
import sys


# Verify Errors
try:
    argument = sys.argv[1]
except IndexError:
    print("There is not any input.")
    sys.exit()

# Verify if only numbers
if argument.isdigit():
    print("Invalid input")
    sys.exit()

# Invalid if more than one argument
if len(sys.argv) > 2:
    print("Invalid input")
    sys.exit()

# Print out the lenght of the first argument
lenght = 0
for calcul in argument:
    lenght = lenght + 1

print(lenght)