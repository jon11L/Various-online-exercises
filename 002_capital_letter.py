def capitals(str):
    new_string = []
    for letter in str:
        if letter.isupper() == True:
            new_string += letter
    return new_string

x = "The CAT is Flying Above Clouds."

print(capitals(x))