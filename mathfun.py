#Amir Elkhargui, Cop2500 section 1
#Mathfun.py - In this program the user is allowed to input the hypotenuse, adjacent angle, opposite side
#adjacnet side to find the adjacent length, opposite length, and adjacent angle.

import math
#functions
def adjacent_length_of_right_triangle(hypo,adj_ang):      #Function for finding the length of a adjacent
    l = math.cos(math.radians(adj_ang)) * hypo            #side of a right triangle found by multiplying the cosine
    return (l)                                            #of the adjacent angle and the hypotenuse

def opposite_length_of_right_triangle(hypo,adj_ang):      #Function for finding the length of a opposite
    o = math.sin(math.radians(adj_ang)) * hypo            #side of a right triangle found by multiplying the sine
    return (o)                                            #of the adjacent angle and the hypotenuse

def adjacent_angle_of_right_triangle_1(hypo,opp):         #Function for finding the adjacent angle of a right triangle
    g = math.asin(opp/hypo)                               #by dividing opposite by hypotenuse applying arcsin to it,
    return math.degrees(g)                                #then turning it to degrees.

def adjacent_angle_of_right_triangle_2(opp,adj):          #Functions for finding the adjacent angle of a right triangle
    g = math.atan(opp/adj)                                #by dividing opposite by adjacent side and applying arctan to
    return math.degrees(g)                                #it, then turning it to degrees.

#Inputs for the sides and angles
hypo = float(input("whats the hypotenuse: "))             #Input for hypotenuse
adj_ang = float(input("whats the adjacent_angle: "))      #Input for adjacent angle
opp = float(input("whats the opposite side: "))           #Input for opposite side
adj = float(input("whats the adjacent side: "))           #Input for adjacent side

#Variables for functions to be printed
p = adjacent_length_of_right_triangle(hypo,adj_ang)
m = opposite_length_of_right_triangle(hypo,adj_ang)
e = adjacent_angle_of_right_triangle_1(hypo,opp)
v = adjacent_angle_of_right_triangle_2(opp,adj)

#Print commands
print("The adjacent length", p)
print("The opposite length", m)
print("The adjacent angle with opp and hypo", e)
print("The adjacent angle with adj and opp", v)