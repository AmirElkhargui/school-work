#Amir El Khargui, COP2500
#lineplotter.py - This program allows a user to input both a slope and Intercept an get an output from
#0 to 10 and 10, 100, 1000, 10000, and 100000.

#INPUTS
I = float(input("Enter the slope:"))                #Input statement for slope
E = float(input("Enter the intercept:"))            #Input statement for intercept

#IF statement
if(I > 0 and E > 0):                                #If statement for printing out the line of the equation
    print("Line y =",I,"x","+",E,":")

#For and While statement
for x in range(0,11):                               #For statement that prints out the slope number from 0-10
    print("At x =",x,", y =", I * x + E)            #and then calculates the resulting Y point after performing
                                                    #the slope formula.

while (x <= 10000):                                 #While statement that multiplies the x point after 10 by 10
    x = x * 10                                      #until 10000 and calculates the resulting y point after performing
    print("At x =",x,", y =", I * x + E)            #slope formula.