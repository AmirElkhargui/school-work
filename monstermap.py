#Amir El Khargui, COP2500
#Monstermap.py - This program allows users to input a horozontal and vertical
#multipler along with a constant in which draws out an 10x8 grid of circles in
#various circle radius.

#Input commands
h = float(input("Horozontal multplier?"))   #Input command for Horozontal mutlipler
v = float(input("Vertical multplier?"))     #Input command for Vertical mutliper
c = float(input("constant?"))               #Input command for constant


#Importing of turtle getting it started and setting of colors
import turtle
my_screen = turtle.getscreen()
my_turtle = turtle.Turtle()
my_screen.bgcolor("white")
my_turtle.pencolor("black")
my_turtle.pensize(1)
my_turtle.speed(100)

#For loops for drawing circle
for x in range(0,10):                       #For Loop for Horozontal axis
    my_turtle.penup()                       #in which the pen starts up
    my_turtle.goto(25*x,1)                  #moves to a location on turtle
    my_turtle.pendown()                     #and continues to keep moving 
    for y in range(0,8):                    #For Loop for Vertical axis
        my_turtle.fillcolor("yellow")       #in which the color fill is
        my_turtle.begin_fill()              #set to yellow, equation for the
        my_turtle.circle((h*x)+(v*y)+c)     #radius of the circle is set
        my_turtle.penup()                   #and the pen moves to different
        my_turtle.goto(0-(x*-25),-25*y)     #locations along the y axis creating
        my_turtle.pendown()                 #circles along the entire 10x8 grid
        my_turtle.end_fill()


