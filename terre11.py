# Import module
import sys

# Manage if Errors
try:
    argument = sys.argv[1]
    hours, minutes = argument.split(':')
    hours = int(hours)
    minutes = int(minutes)
except ValueError:
    print("Please enter a valid time.")
    sys.exit()
except IndexError:
    print("Please enter a valid time.")
    sys.exit()

# Manage message if invalid input
if hours > 24 or minutes > 59:
    print("Please enter a valid time.")
    sys.exit()

# Converse format 24h to 12h    
if hours > 12 and hours < 24:
    print(int(hours-12), ":", minutes, "PM")
if hours < 12:
    print(hours, ":", minutes, "AM")
if hours == 12:
    print(hours, ":", minutes, "PM")
if hours == 24:
    print(int(hours-12), ":", minutes, "AM")
