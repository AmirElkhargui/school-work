# Amir El Khargui, COP2500
# Lakearea.py - This program allows for users to insert the radius of the lake of knightrola
# (which is a half circle) and then output the Area. This should allow for people to quickly
# determine the area of knightrola with different radius values.

# Input statement
r = int(input("Enter the radius of the lake in meters:"))  # Input statement that asks for the "r" radius.

# Variables
π = (3.1416)           # Sets the variable π (pi) equal to "3.1416", the number for pi.
A = (π*r**2)/2       # Sets the variable A (Area) to the equation for a semi circle.

# Print
print("The area of lake knightrola is", A)  # Prints out the results for the inputed radius.
