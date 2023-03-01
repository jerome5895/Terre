# Import module
import sys

# Verify if number
try:
    number = int(sys.argv[1])
except ValueError:
    print("Invalid input. Please enter an Integer.")
    sys.exit()
except IndexError:
    print("There is no input.")
    sys.exit()

# Verify if even, odd or negative
if number % 2 == 0:
    print("even")
else:
    print("odd")

if number < 0:
    print("negative")







