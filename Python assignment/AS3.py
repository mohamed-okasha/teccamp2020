# a program that allowes u to enter a Name and Grade of tenth student,to know thier mark whether it's excellent, very-good, good, or poor.

#with open("AS3.txt") as fabj:
#  bio = fabj.read()
#  print(bio)

i = 0
while i < 11 :
    n = input("Pls, Enter ur Name :")
    grade = int(input("whats ur Grade in %"))

    if grade>=85 and grade<=100:
      print(f" Name of Student :  {n}     Grade is {grade} %   Rate : Excellent")
      Rate = "Excellent"

    elif grade>=70 and grade<85:
       print(f" Name of Student :  {n}     Grade is {grade} %   Rate : Very-good")
       Rate = "Very-good"

    elif grade>=50 and grade<70:
       print(f" Name of Student :  {n}     Grade is {grade} %     Rate : Good")
       Rate = "Good"

    elif grade>=0 and grade<50:
       print(f" Name of Student :  {n}     Grade is {grade} %   Rate : Maybe naext time")
       Rate = "Poor"

    else:
      print("Unkown Result")
    i +=1
else:
  print("We Done")




#x = open("AS3.txt" , "w")
#x.write("AS3.py")
#x.close()