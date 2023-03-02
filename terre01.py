# Function that returns the title of the script
def print_title_of_script():
    import sys
    script_title = sys.argv[0]
    print(script_title)

# Print title
print_title_of_script()