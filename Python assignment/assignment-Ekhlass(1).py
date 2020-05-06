import os
import time

f = open("Ekhlass-python.txt" , 'a')

clear = lambda: os.system('clear') # in linux os
# clear = lambda: os.system('cls') 'in windows os'

def getch():
     import sys,tty, termios      
     old_settings = termios.tcgetattr(0) 
     new_settings = old_settings[:]
     new_settings[3] &= ~termios.ICANON 
     try:
          termios.tcsetattr(0, termios.TCSANOW, new_settings)
          ch = sys.stdin.read(1) 
     finally:
          termios.tcsetattr(0, termios.TCSANOW, old_settings)


def instruction():
    print("""
    be confident, you are able to enter data for unlimited number of students,
    when you finish, just type 'Quit' in the Name field.
    >>input :
    """)

def appendGrade(grade):
    students_grades.append(grade)
    f.writelines(f"\t\tGrade : {grade}\n")

def CS ():
    time.sleep(5)
    clear() # in linux , it is cls() in windows 





print("""welcome ...
this program takes many students names & grades from the user, then it
 determines the level of each student and print it on the console,
 the names & grades will be saved in a text file.

 press any key to continue.
""")

getch()
clear()
instruction()


students_grades = []
students_levels = []
students_names = []

while (True ):
    name = input("Name: ").title()
    if name != 'Quit':
        students_names.append(name)
        f.writelines(f'Name : {name}')
    elif name == 'Quit':
        f.close()
        clear()
        print("Thanks, the program is gonna quit")
        CS()
        break

    
    while True:
        grade =float(input("\ngrade: "))
        clear()
            
        if grade>=85 and grade <= 100:
            print('the level is excellent')
            students_levels.append('excellent')
            appendGrade(grade)

            break
        elif grade>=70 and grade < 85:
            print ('the level is very good')
            students_levels.append('very good')
            appendGrade(grade)
            break
        elif grade>=50 and grade < 70:
            print ('the level is good')
            students_levels.append('good')
            appendGrade(grade)
            break
        elif grade>=0 and grade < 50:            
            print ('the level is poor')
            students_levels.append('poor') 
            appendGrade(grade)
            break
        else:            
            print("invalid grade, enter it again") 

    CS()
    instruction()       

   

         


