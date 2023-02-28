import sys

# Test line code in the variable "Integers", to manage Errors
try:
    integers = [int(integer) for integer in sys.argv[1:]]   
except ValueError:
    print("Please enter a list of integers.")
    sys.exit()

# To sort "Integers" to "sorted" or "not sorted"
sorted = True
for i in range(len(integers) - 1):
    if integers[i] > integers[i+1]:
        sorted = False
        break

# Two possible output 
if sorted:
    print("Your list is sorted!")
else:
    print("Your list is not sorted!")