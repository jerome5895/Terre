# Import module
import sys

# Test argument to manage Errors
try:
    string = sys.argv[1]
except IndexError:
    print("Invalid input. Please provide at least two characters.")
    sys.exit()

reversed_string = ""

# Get the argument upside down
for substring in string:
    reversed_string = substring + reversed_string

# Program that displays the argument upside down
print(reversed_string)

