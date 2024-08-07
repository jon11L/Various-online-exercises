def reduce_string(str):
    '''takes a string as parameter and return half(50%) of that string.'''
    return str[0:len(str)//2]

given_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore."
print(reduce_string(given_string))


