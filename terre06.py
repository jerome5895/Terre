import sys

string = sys.argv[1]

reversed_string = ""

# Get the argument upside down
for substring in string:
    reversed_string = substring + reversed_string

print(reversed_string)


