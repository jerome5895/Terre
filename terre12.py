# Import module
import sys

# To try Errors
try:
    argument = sys.argv[1]
    hours, minutes = argument[:-2].split(":")
except ValueError:
    print("Invalid input. Please try again.")
    sys.exit()
except IndexError:
    print("Invalid input. Please try again.")
    sys.exit()

# To convert 12h format to 24h format
if argument[-2:] == "PM":
    if hours != "12":
        hours = str(int(hours) + 12)
    else:             
        hours = "12"
else:
    if hours == "12":
        hours = "00"

# Manage errors argument not full
if argument[-2:] != "AM" or argument[-2:] != "PM":
        print("Invalid input. Please try again.")
        sys.exit()

time_24h_format = f"{hours}:{minutes}"


print(time_24h_format)
