# Python Program - Calculate Grade of two Student  
class Student:
  def __init__(self, name, mark, grade):
    self.name = name
    self.mark = mark
    self.grade = grade
def grade(mark):
    if(mark>=85 and mark<=100):
    	return("excellent")
    elif(mark>=70 and mark<=84):
    	return("very good")
    elif(mark>=50 and mark<=69):
    	return("good")
    elif(mark>=0 and mark<=49):
    	return("poor")
    else:
      return("it's n't Mark !!!")

student1 = Student(input("Enter Student name : "),int (input("Enter Mark :")),0)
student1.grade =grade(student1.mark)

student2 = Student(input("Enter Student name : "),int (input("Enter Mark :")),0)
student2.grade =grade(student2.mark)


text = open("Grudes of students.txt", "a")

text.write("Grude of Student "+student1.name+" and Mark "+str(student1.mark) +" "+student1.grade+"\n")
text.write("Grude of Student "+student2.name+" and Mark "+str(student2.mark)+" "+student2.grade+"\n")
text.close()

print("Grude of Student "+student1.name+" and Mark "+str(student1.mark) +" "+student1.grade)

print("Grude of Student "+student2.name+" and Mark "+str(student2.mark)+" "+student2.grade)
        