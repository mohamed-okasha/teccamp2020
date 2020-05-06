from array import *

name = array('u',[])

marks = array('i',[])   

n = int(input("Enter how many Students : "))


for i in range(n):
    name = input("Enter name of student: ")

for i in range(n):
    x=int(input("Enter mark : "))
    marks.append(x)

for i in range(n): 
        if marks[i] >= 85 and marks[i] <= 100:
            print("student mark is : Excellent")
        elif marks[i] < 85 and marks[i] > 70:
            print("student mark is : very good")
        elif marks[i] > 50 and marks[i] <= 70:
            print("student mark is : good" )
        elif marks[i] >= 0 and marks[i] <= 50:
            print("student mark is :poor")
