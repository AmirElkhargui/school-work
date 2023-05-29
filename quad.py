#Amir El khargui, COP#2500
#quad.py- This program allows you to input the a, b, and c coefficients of a quadratic equation
#and determines the weather the quadratic has 2 roots, 1 real root, or 2 complex roots and outputs the
#roots accordingly.

#Functions
def determinant(a,b,c):                                   #Function for the determinant that finds whether
    d = b**2-4*a*c                                        #there is 2 roots, 1 real root, or 2 complex roots
    return d

def first_root(a,b,c):                                    #Function for determining the first root with the
    d1 = (-b + (b**2 - 4 * a * c) ** 0.5)/(2*a)           #coefficients being plugged in on the addition side
    return d1                                             #of the quadratic equation.

def second_root(a,b,c):                                   #function for determining the second root with the
    d2 = (-b - (b**2 - 4 * a * c) ** 0.5)/(2*a)           #coefficients being plugged in on the subtraction
    return d2                                             #side of the quadratic equation.

#Input statements for coefficients
a = float(input("Enter coefficient a: "))                 #Input for coefficient a
b = float(input("Enter coefficient b: "))                 #Input for coefficient b
c = float(input("Enter coefficient c: "))                 #Input for coefficient c

#variables
d = determinant(a,b,c)                                    #Variable that calls function for determinant
d1 = first_root(a,b,c)                                    #Variable that calls function for first_root
d2 = second_root(a,b,c)                                   #Variable that calls function for second_root

#if statements
if d == 0:                                                #conditional for if the determinant has 1 real root
    print("That quadratic has on root: ", d1)             #and pritns out the roots.
elif d > 0:                                               #condtional for if the determinant has 2 real roots
    print("That quadratic has two root: ", d1,"and",d2)   #and prints out the roots.
elif d < 0:                                               #conditional for if the determinant has complex roots
    print("Sorry, that quadratic has complex roots")      #in which case it will not solve the equation.