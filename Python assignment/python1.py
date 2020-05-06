class Student:
    def __init__(self,name,grad):
        self.name=name
        self.grad=grad
def TryparesStrToInt(grad):
    try:
        float(grad)
        return True
    except:

        return False
def TryparesIntToStr(name):
    try:
        float(name)
        return False
    except:

        return True
def cheakGrad(grad):
    grad=float(grad)
    gradStr=None
    if grad>100 or grad<0:
        print("you have to edit this grad!")
    elif grad>=85:
        gradStr="Excellent"
    elif grad>=70:
        gradStr="Very good"
    elif grad>=50:
        gradStr= "Good"
    elif grad<50:
        gradStr="Poor" 
    return gradStr

students=[]
print("Enter the names of students. ")
print("type \"done\" when you end")
while True :
    name=input("Enter student name: ")
    if(not TryparesIntToStr(name)):
        print("Syntax Error Pleas Enter student Data again..")
        continue
    if(name=="done" ):
        break

    grad=input("Enter student grad: ")
    if(not TryparesStrToInt(grad)):
        print("Syntax Error Pleas Enter student Data again..")
        continue
    student1=Student(name,grad) 
    students.append(student1)


text=""
for stu in students:
    gradStr=cheakGrad(stu.grad)
    print("%-15s %-15s %-15s" %(stu.name,stu.grad,gradStr))
    #print(stu.name ,stu.grad,gradStr)
    text=text+"%-15s %-15s %-15s" %(stu.name,stu.grad,gradStr) +"\n"
saveFile=open('gradsFile.text','w')
saveFile.write(text)
saveFile.close()
print("end..\n ...\n"+"done! you saved a file of grads on the same directory of the program ")