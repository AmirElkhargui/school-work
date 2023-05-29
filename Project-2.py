#Amir El Khargui, COP2500
#Project.py - explantation below.
#In the knightrola Region, Doctors are having problems keeping track of the many patients the do walkins
#and schedules from phone calls, causing overlap between the 2 kinds of patients resulting in many dissatisfied
#patients having to wait for a doctors visit longer than they scheduled in advannce. This program allows nurses to input
#each patient (both walk ins and phone calls) that schedules with the office. The input taken would be the Date, Walkin
#or Phone call, name of patient, and approximate length of the patients visit. The list will have its input be turned into
#proper capitalization and strings to catogorize each input in the schedule. It will allow the removal and addition of
#patients from the list. This should allow the nurses to properly put in the correct amount of patients each week, which
#for the doctor is a maximum of 15 patients, and approximize the time properly within those constraints.

#Functions
def patients(thelist, title):                                                 #Function name: Patients; This function
    print(title)                                                              #initates the list and returns the first
    print("Type in all the patients first and"                                #value that is entered in the schedule
    " then end the addition phase and begin "                                 #and moves onto the additon phase. This
    "the removal phase or to end the program.")                               #function takes the input from the user
    print("Remember, the doctor can only handle 15 "                          #of a patients name, date, schedule type,
          "patients a week, be merciful!")                                    #and how long the visit is for and converts
    name = input("Name of Patient: ")                                         #joins it all together and places strings
    Date = input("Date: ")                                                    #in between each input to indicate what is
    modality = input("Which scheduling type? Walk In or Phonecall?: ")        #what. The parameters of the function is
    time = input("How long will the patient's visit : ")                      #just the list and title. The list is the
    Schedule = (" | ".join(["Name: " + name.title(), "Scheduling type: "      #main thing being worked upon function,
        + modality.title(), "Date: " + Date.title(), time + " mins"]))        #which is being added upon. The title is
    f = Schedule.split(",")                                                   #just the statement being printed at
    return f                                                                  #the beginning of the statement. The list
                                                                              #gets returned from this function for it
                                                                              #for it to be added upon and removed from.
                                                                              #You can only really enter strings, so
                                                                              #people can ignore writing mins in the time
                                                                              #spot. Otherwise nothing can reasonably go
                                                                              #wrong.

def add_patients(thelist):                                                    #Function name: Add patients; This function
    e = 1                                                                     #adds upon the current list started in the
    while e == 1:                                                             #first function. It prints the same format
        name = input("Name of Patient: ")                                     #as the first function, but here it gives
        Date = input("Date: ")                                                #prompts asking if the user wants to cont-
        modality = input("Which scheduling type? Walk In or Phonecall?: ")    #-inue or stop the program to begin removing
        time = input("How long will the patient's visit in minutes be?: ")    #from the list. This function also lets
        Schedule = (" | ".join(["Name: " + name.title(), "Scheduling type: "  #only 15 entries to be made, and once the
            + modality.title(), "Date: " + Date.title(), time + " mins"]))    #limit is passed, it would prompt the
        f = Schedule.split(",")                                               #removal phase of the program. It also
        thelist.append(f)                                                     #only allows for the users to input the
        stop = input("Want to continue? Type STOP to stop adding "            #commands that the prompt tells the user
                     "to the schedule other wise type CONTINUE: ")            #to insert, so if a user was to type
        if stop == "STOP" or len(thelist) > 14:                               #anything other than CONTINUE or STOP
            print("Heres the schedule: ")                                     #the list will be printed and the program
            for c in range(len(thelist)):                                     #will end automatically. The parameters of
                print(c + 1, ":", thelist[c])                                 #the function is only the list, which is
            print(remove_patients(ourlist))                                   #the main list being worked on, and in
        if stop == "CONTINUE":                                                #this function, the list being added upon.
            print(add_patients(ourlist))                                      #A list of schedules added to the list is
        if stop != "STOP" or "CONTINUE":                                      #returned from this function. The user
            print("Heres the schedule: ")                                     #can possibly make the function go wrong
            for c in range(len(thelist)):                                     #if the words STOP or CONTINUE are not
                print(c + 1, ":", thelist[c])                                 #inputted in it proper case sensitivity.
            exit()

def remove_patients(thelist):                                                 #Function name: Remove patients; The
    removenow = input("Type REMOVE if you want to Remove "                    #Funtion continues after the addition 
                      "OR type ADD to continue to add more,"                  #phase and starts by prompting the user
                      " or anything elses to end the program: ")              #to choose weather to ADD, REMOVE, or
    if removenow != "REMOVE" or "ADD":                                        #anything else other than the two to end
        print("Heres the schedule: ")                                         #the program and print the list. If the
        for c in range(len(thelist)):                                         #user chooses to add, the program will
            print(c + 1, ":", thelist[c])                                     #go back to the add_patient function to
                                                                              #which the user can continue to add. If
    while removenow == "REMOVE":                                              #the user chooses to remove, the function
        d = int(input("Choose the number of the"                              #will prompt the user to choose the number
                    " appointment you want to remove: "))                     #of the schedule to be removed, chosing
        thelist.pop(d-1)                                                      #the number will remove the schedule from
        for c in range(len(thelist)):                                         #the list and result in the list being
            print(c + 1, ":", thelist[c])                                     #printed without the removed. The user can
        j = input("Would you like to remove another?, "                       #choose to continue to remove by typing 
                 "if not type STOP or ADD to add more"                        #anything, or STOP to print the schedule
          ", otherwise press type anything to continue: ")                    #and finish the program or ADD to begin
        if j == "STOP":                                                       #adding to the schedule again. The only
            print("Here is the schedule!")                                    #parameter to this function is thelist
            for c in range(len(thelist)):                                     #is the main list being worked upon, in
                print(c + 1, ":", thelist[c])                                 #this case, being removed from. A list
            exit()                                                            #of removed schedules picked by the user
        while j == "ADD":                                                     #is returned back. This function can
            if len(thelist) > 14:                                             #hardly go wrong, only if the user fails
                exit()                                                        #to insert what the program askes of them,
            print(add_patients(ourlist))                                      #but the only consequence is the program
            print(remove_patients(ourlist))                                   #ending. The same with the rest of the
    while removenow == "ADD":                                                 #functions.
        if len(thelist) > 14:
            exit()
        print(add_patients(ourlist))
        print(remove_patients(ourlist))


#Blank list being outputed
ourlist = []

#Blank list being made to equal the first list entered, which helps the add function.
ourlist = patients(ourlist,"Enter patient schedule details. "
                           "Remember to note the time and get "
                           "enough patients within the day.")

#Print statments for each of the functions
print(add_patients(ourlist))
print(remove_patients(ourlist))