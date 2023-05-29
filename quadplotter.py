#Amir Elkhargui, #COP2500 Section 1
#quadplotter.py - This program accepts inputs of quadratic coefficients and then prints out
#the value of y at different points of x from 0 to 9 and 10 to 10000000 on a line.
#Functions
def quadratic(a,b,c,x):                           #Function for the equation of a quadratic function
    y = a*(x**2)+(b*x)+c                          #It also returns the value y from the given values
    return y
def printvalues(x,y):                             #Function that prints the x and y values at each position
    print("At x =",x,",y =",y)                    #of x.

#inputs
a = float(input("Enter coefficient a: "))         #Input for coefficient a
b = float(input("Enter coefficient b: "))         #Input for coefficient b
c = float(input("Enter coefficient c: "))         #Input for coefficient c

#print statement
print("Parabola y =",a,"x^2 +",b,"x +",c)         #Print statement for displaying the Parabola equation

for x in range(0,11):                             #for loop that applies x in a range from 0 to 10
    y = quadratic(a,b,c,x)                        #and its plugged into a quadratic equation finally
    printvalues(x,y)                              #that will print both the x and y value.
while (x <= 1000000):                             #while loop that applies x in a range from 10 to 1000000
    x = x * 10                                    #ascending by 10s and plugs it into the quadratic equation
    y = quadratic(a,b,c,x)                        #to be printed in x and y values
    printvalues(x,y)