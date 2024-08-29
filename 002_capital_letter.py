# create a script that takes a string and return all the capital letters in a list of string.

def capitals(str):
    new_string = []
    for letter in str:
        if letter.isupper() == True:
            new_string += letter
    return new_string

x = "The CAT is Flying Above Clouds."

print(capitals(x))
