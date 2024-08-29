# Write a python script that imports the math module and uses it to calculate the area and circumference of a circle based on a user-provided radius.
from math import pi

radius = float(input("type the radius of the circle: "))
circumference = (2 * pi) * radius
area = pi * radius**2

print(f"the circumference of the circle is: {round(circumference, 2)}\n")
print(f"the area of the circle is: {round(area, 2)}")
