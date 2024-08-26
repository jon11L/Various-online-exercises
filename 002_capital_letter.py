# create a script that that takes a string and return a list of string of all the capital letters

def capitals(str):
    new_string = []
    for letter in str:
        if letter.isupper() == True:
            new_string += letter
    return new_string

x = "The CAT is Flying Above Clouds."

print(capitals(x))
