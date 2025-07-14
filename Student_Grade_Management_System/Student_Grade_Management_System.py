#Greet users and ask for intent to use the system
print ('Welcome, you can enter student grades for your course.')
go_ahead = input ('Would you like to enter student grades? ')

def student_details(student_info, name, score):
    student_info[name] = score
    list = student_info
    return list

#Initize an empty dictionary to store students name and score
student_info= {}

#confirm intent to use the system
if go_ahead.upper() == "Yes":
    while True:
        #Enter student name
        student_name= input("Please enter a single student's name: ")
        #student_name= student_details
        student_score= input("Please enter that student's score: ")
        #Pass to student detail function
        details = student_details(student_info, student_name, student_score)
        
        #Check if they want to continue
        go_ahead = input("Would you like to continue: ")
        #confirm intent to continue using the system
        if go_ahead.upper() != "Yes":
            break




    #If statement to check if check if user is done entering data
    
#Initize an empty list to store students name and score


#Start data entry loop

#Calculate grade for the score

#Store student record in the list

#Data entry and calculation of class average

#Display table of student data
 
#Display class average