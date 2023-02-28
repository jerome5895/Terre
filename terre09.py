# Import module
import sys

# Verify Errors
try:
    number = int(sys.argv[1])
    result = number ** 0.5
except ValueError:
    print("Invalid input. Please provide only integer.")
    sys.exit()
except IndexError:
    print("Invalid input. No number provided.")
    sys.exit()

# Function square root
def square_root(a):
    return a ** 0.5

# Condition negative argument
if number < 0:
    print("Invalid input. Negative number.")
    sys.exit()

# Condition for more arguments
if len(sys.argv) > 2:
    print("Invalid input, please provide only one integer.")
    sys.exit()

# Print out square root
print("The square root is:", square_root(number))
