#Amir El khargui, COP2500
#Courselist.py - This program allows a user to insert courses and stop at when typed "EXIT". If more than 5 courses are
#entered the program will ask the user to remove one.
def ask_for_courses(thelist, title):                            #This function is named ask for courses, the function's
  print(title)                                                  #purpose is to set up a range for list to know how many
  for p in range(0, 6, 1):                                      #courses will be in the list, it also allows the user to
    course = input("Enter the Course or Type EXIT to stop: ")   #insert courses and EXIT when they want to stop. The title
    if course == "EXIT":                                        #is the print statement at the beginning and thelist refers
      break                                                     #to the main list we are using to print out the schedule.
    thelist.append(course)                                      #It doesn't return much other than the prompts.

def print_courses_in_numbers(thelist):                          #This function is named print courses in numbers, the
  print("Here's your courses!")                                 #function's purpose is to print out the main list in
  for x in range(len(thelist)):                                 #in a numbered format with the course names, it also
    course = thelist[x]                                         #indentifies that there is more than 5 courses and
    x = x + 1                                                   #prompts the user to remove one of the courses by
    print(f"  {x:1}: {course}")                                 #its number. The parameter "thelist" is just the main
    if x >= 6:                                                  #being worked on in the program that will be printed.
      n = int(input("Looks like you have 6 courses,"
                    " you need to remove one: "))
      thelist.pop(n-1)

def print_new_courses(thelist):                                #This function is named print new courses, the functions
    print("Here is your new schedule!")                        #purpose is to print the new list of courses after
    for f in range(len(thelist)):                              #removing one of the courses. The parameter "thelist" is
        course = thelist[f]                                    #just the main being worked on in the program that will
        f = f + 1                                              #be printed.
        print(f"  {f:1}: {course}")

#The empty list that the user will be inputting into.
ourlist = []
#print statements for functions
ask_for_courses(ourlist, "Enter courses of your choice.")
print_courses_in_numbers(ourlist)
print_new_courses(ourlist)
