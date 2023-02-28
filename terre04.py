# import module
import sys

# verify if input
if len(sys.argv) < 2:
    print("There is not input.")
    sys.exit()

# verify if number
try:
    number = int(sys.argv[1])
except ValueError:
    print("Invalid input. Please enter an Integer.")
    sys.exit()

# verify if even, odd or negative
if number % 2 == 0:
    print("even")
else:
    print("odd")

if number < 0:
    print("negative")




