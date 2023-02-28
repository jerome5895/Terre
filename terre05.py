# import module
import sys

# verify Errors
try:
    number_1 = int(sys.argv[1])
    number_2 = int(sys.argv[2])
    result = (number_1 // number_2)
except ZeroDivisionError:
    print("Invalid input. One of your numbers is zero.")
    sys.exit()
except ValueError:
    print("Invalid input. Please enter two integers.")
    sys.exit()
except IndexError:
    print("One integer at least is missing")
    sys.exit()

# functions for result and remainder
def result(a, b):
    return a // b
def remainder(a, b):
    return a % b

# verify divider size
if number_2 > number_1:
    print("Your divider is bigger than your dividend.")

# print out the result and the remainder
print("The result is:", result(number_1, number_2))    
print("The remainder is:", remainder(number_1, number_2))

