# Import module
import sys

# Verify Errors
try:
    number = int(sys.argv[1])
except ValueError:
    print("Please enter an integer.")
    sys.exit()
except IndexError:
    print("Invalid input. No provided number.")
    sys.exit()

# Manage more arguments
if len(sys.argv) > 2:
    print("Invalid input. Please provide only one integer.")
    sys.exit()

# Program that displays if it is prime number
if number > 1:
    for i in range(2, int(number/2)+1):
        if (number % i) == 0:
            print("It is not a prime number.")
            break
    else:
        print("It is a prime number.")
else:
    print("It is not a prime number.")