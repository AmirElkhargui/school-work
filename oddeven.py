#Amir El Khargui, COP2500
# Program that allows the user to guess either odd or even and outputs a random number that may be odd or even
import random

#Variables
i = input("i,m thinking of a number. Is it odd or even?")    #Input statement for where the user inputs even or odd
o = random.randint(1, 256)                                   #The variable for outputing a random number from 1 to 256
odd = "odd"                                                  #The variable odd is set to word "odd"
even = "even"                                                #The variable even is set to word "even"

#if statements
if (o % 2) != 0 and (i == even):                             #If statements that finds the odd number or even number by
        print("my number was", o, "sorry!")                  #dividing by two and making sure there is no remainer.
elif(o % 2) == 0 and (i == even):                            #It also make sure that weather you type even or odd it
        print("my number was", o, "Well Done!")              #it tells you weather you're correct about your guess
elif(o % 2) == 0 and (i == odd):                             #or not. It also puts in a command that forfeits you for
        print("my number was", o, "sorry!")                  #not putting either even or odd.
elif(o % 2) != 0 and (i == odd):
        print("my number was", o, "Well Done!")
elif(i != even or odd):
        print("You didn't enter 'odd' or 'even'. You Forfeit!", "(My number was", o,"if you're wondering.)")