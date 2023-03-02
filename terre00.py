# Function that displays the alphabet in lowercase letters
def alphabet():
    for lettre in range(97,123,1):
        print(chr(lettre), end="")
    print(("\n"), end="")

# Print out function alphabet
alphabet()