# Import module
import sys

# Verify Errors
try:
    number_1 = int(sys.argv[1])
    number_2 = int(sys.argv[2])
    result = number_1 ** number_2
except IndexError:
    print("Invalid input. One integer at lest is missing.")
    sys.exit()
except ValueError:
    print("Invalid input. Please provide only integers.")
    sys.exit()

# Function power
def power(a, b):
    return a ** b

# Condition negative number
if number_2 < 0:
    print("Invalid input. Negative number.")
    sys.exit()

# Print out the result of power
print("The result is:", power(number_1, number_2))

