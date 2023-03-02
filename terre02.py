# Function that displays the arguments of the prompt, line by line
def displays_argument():
    import sys
    argument = sys.argv[1:]
    for arg in argument:
        print(arg)

# Call function 'display_argument'
displays_argument()