#Amir El khargui, COP2500
#Movies.py - This program allows for the user to insert the number of moviegoers which will print out
#the price per ticket.

#Input statement and Variables
p = float(input("Enter the number of moviegoers: "))  #Statement that allows for input of number of movie goers
i = 9.50                                              #Sets the variable "i" as the individual ticket prices
r = i + (p * 12) - 12                                 #Sets the variable "r" as the ticket price for anyone else as 12
x = p * 7.25                                          #Sets the variable "x" as the ticket prices for more than 25 people

#if statement
if(p == 1):                                           #The if statement that prints the price of 1 ticket
    print("The total ticket price is:$", i)
elif(25 > p > 1):                                     #The if statement that prints the price of more than 1
    print("The total ticket price is:$", r)           #but less than 25 tickets
else:
    print("The total ticket price is:$", x)           #The else statement that prints the price of more than 25 tickets