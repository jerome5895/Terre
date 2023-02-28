# Import module
import sys

# Manage Errors
try:
    number_1 = int(sys.argv[1])
    number_2 = int(sys.argv[2])
    number_3 = int(sys.argv[3])
except ValueError:
    print("Invalid input. Please provide three integers.")
    sys.exit()
except IndexError:
    print("Invalid input. One integer at least is missing.")
    sys.exit()

# Find the integer in the middle
if number_1 < number_2 and number_1 > number_3:
    print(number_1)
if number_1 > number_2 and number_1 < number_3:
    print(number_1)

if number_2 < number_1 and number_2 > number_3:
    print(number_2)
if number_2 > number_1 and number_2 < number_3:
    print(number_2)

if number_3 < number_1 and number_3 > number_2:
    print(number_3)
if number_3 > number_1 and number_3 < number_2:
    print(number_3)

# Error if all equal
if number_1 == number_2 and number_1 == number_3:
    print("The three integers are equal.")