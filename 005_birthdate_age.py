# Write a python program that asks the user for their birthdate then calculates and print their current age.
# include error handling for invalid input.

from datetime import datetime

def calculate_age():
    '''Takes the input of a user as their birth date and calculate their age.'''
    today = datetime.today().date()

    while True:
        try:
            birthdate = (input(f"Insert your date of birth here: in the format like so {today} (yyyy-mm-dd):  "))
            birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
            print("\n")
            break
        except ValueError:
            print("Wrong Format, please type again in the correct format yyyy-mm-dd \n")
            
    age = today.year - birthdate.year
    if today.month > birthdate.month and today.day > birthdate.day:
        print("your birthday has already happened. \n")
    else:
        print("your birthday hasn't happened yet. \n")
        age -= 1

    return age

age = calculate_age()
print(f"Your age is: {age}.")
