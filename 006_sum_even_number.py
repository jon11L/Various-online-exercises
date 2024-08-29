#  Write a function that takes a list of numbers as input and returns the sum of all the even numbers.

def sum_even_num():
    ''' allow the user to input as many numbers as they want and return the sum of the even numbers'''
    num_list = []
    print("type as many numbers as you like. When you are done type 'exit' or any other character than numbers to stop.")
    while True:
        # give a loop to let the user add as many numbers
        try:
            number = int(input("type a number: "))
            num_list.append(number)
        except ValueError:
        # when typing anything else than a number it stops and moves on
            print("numbers have now been stored. ")
            break
    print(num_list)
    sum_even = 0
    for num in num_list:
        # look through the list and increment to a new variable if number is even.
        if num % 2 == 0:
            sum_even += num

    return sum_even


sum_even = sum_even_num()
print(f"the sum of all the even numbers is: {sum_even}")
