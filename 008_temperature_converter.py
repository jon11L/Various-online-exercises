# Create a program that converts temperatures between Celsius and Fahrenheit. The user should input the temperature and choose the conversion direction.

def temperature_converter():
    '''Convert Temperature between celsius and fahrenheit.'''
    temp = None
    while temp == None:
        try:
            temp = int(input("enter the degrees here: "))
        except ValueError:
            print("Wrong Format, type again. \n")
    while True:
        temp_type = input("Which type of temperature you want to convert to?C Celsius or Fahrenheit? (Type 'C' or 'F' and press Enter.): ")
        if temp_type in ["c", "C", "Celsius", "celsius"]:
            fahrenheit = temp
            celsius = (fahrenheit -32) / 1.8
            return f"temperature in celsius is {celsius} degrees."
        elif temp_type in ["f", "F", "fahrenheit", "Fahrenheit"]:
            celsius = temp
            fahrenheit = (celsius * 1.8) +32
            return f"temperature in Fahrenheit is {fahrenheit} degrees."
        else:
            print("something went wrong, try again.")

temperature = temperature_converter()
print(temperature)
