#Amir Elkhargui- COP2500, Section 1
#Courselist2- This program allows a user to input courses separated with commas and have then printed out in a proper
#list, the user then would either have to remove or add courses untill only 5 courses exactly are left in the schedule.

#Functions
def ask_for_courses(thelist, title):                            #Ask_for_Coursses - The function outputs the first list
  print(title)                                                  #in which will be returned and then used for adding or
  course = input("What courses would you like to take? ")       #removing from the list. Thelist is the main list being
  print("You are currently taking these courses: ")             #worked upon in the program. The list with its modifications
  l = course.title()                                            #on capitalization and spacing is returned. Nothing much
  a = l.replace(" ","")                                         #can go wrong.
  t = a.split(",")
  for i in range(len(t)):
    print(i + 1,":",t[i])
  return t

def add_courses(thelist):                                       #add_courses - The function outputs the new list with the
    while len(thelist) < 5:                                     #new courses added upon them. This only happens when the
        course = input("what courses would you like to take? ") #length of the list is less than 5 courses. Thelist para
        print("You are currently taking these courses: ")       #-meter is the main list being worked on. Nothing much
        l = course.title()                                      #can go wrong unless the main list doesn't work.
        a = l.replace(" ","")
        t = a.split(",")
        thelist.extend(t)
        for c in range(len(thelist)):
            print(c + 1, ":", thelist[c])


def delete_courses(thelist):                                   #delete_courses - The function outputs the new list with
    while len(thelist) > 5:                                    #the removed courses taken from the list. This happens when
        course = input("what courses would like to remove? ")  #the length of the list is more than 5 courses. Thelist
        print("You are currently taking these courses: ")      #parameter is the main list being worked on. Nothing much
        l = course.title()                                     #can go wrong unless the main list doesn't work.
        a = l.replace(" ", "")
        t = a.split(",")
        for c in range(len(t)):
            thelist.remove(t[c])
        for c in range(len(thelist)):
            print(c + 1, ":", thelist[c])


def if_correct_courses(thelist):                              #If_correct_courses - The function doesnt change the list
    print("You are currently taking these courses: ")         #at all in anyway, it just confirms that 5 courses and
    if len(thelist) == 5:                                     #only 5 courses are present and stops the program. Thelist
        for c in range(len(thelist)):                         #parameter is the main list being worked on. Nothing much
            print(c + 1, ":", thelist[c])                     #can go wrong unless the main list doesn't work.
        print("done!")



#Blank list being outputed
ourlist = []
#Blank list being made to equal the first list entered
ourlist = ask_for_courses(ourlist,"You aren't taking any courses.")
#Print statements with if statements
if len(ourlist) < 5:
    print(add_courses(ourlist))
if len(ourlist) > 5:
    print(delete_courses(ourlist))
if len(ourlist) == 5:
    print(if_correct_courses(ourlist))