# Write a Python script that takes two numbers as input from the user and performs addition, subtraction, multiplication and division.
# Print the result of each operation.

def calculate(n1, n2):
    '''takes two numbers as argument and perform addition, subtraction, multiplication and division of these 2 numbers.'''
    add = n1 + n2
    print(f"addition: {n1} + {n2} = {add} ")
    subtract = n1 - n2
    print(f"subtraction: {n1} - {n2} = {subtract} ")
    multiply = n1 * n2
    print(f"multiplication: {n1} * {n2} = {multiply} ")

    try:
        divide = n1 / n2
        print(f"division: {n1} / {n2} = {divide}")
    except ZeroDivisionError:
        print("Error, you cannot divide by zero(0)")


first = int(input("please type a number: "))
second = int(input("please type a second number: "))

print("\n", "*"*50, "\n")
calculate(first, second)
print("\n", "*"*50, "\n")