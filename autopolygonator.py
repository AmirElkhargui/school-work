#Amir El khargui, COP 2500
#autopolygonator.py- This program allows you input the number of sides and total
#length of a polygon, and as a result it would print your desired polygon.

#Input and variable statement
i = int(input("The number of sides of the polygon")) #Input value for sides
y = int(input("The total lenth of the polygon"))     #Input value for total length
P = y/i                                              #Variable for dividing the sides of total length by the sides
l = 0                                                #Variable for range that will be used to stop 

#Imported turtle commands 
import turtle                                        #Command for importing turtle for use

my_screen = turtle.getscreen()                       #All commands for setting up the turtle
my_turtle = turtle.Turtle()                          #for pen size and color and background
                                                      
my_screen.bgcolor("white")
my_turtle.pencolor("black")
my_turtle.pensize(3)
my_turtle.fillcolor("red")

#If command for drawing and stopping
if i >= 3:                                          #If command makes it so that you can't enter a value below 3 and have it run
    for l in range(0,i):                            #For command that allows the sides to stop at the exact value of sides inputed
        my_turtle.forward(P)                        #Allows the turtle to draw forward
        my_turtle.left(360/i)                       #Allows the turtle to turn and make the sides while drawing

