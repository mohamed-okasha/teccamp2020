
def grade(G):
    if G >= 85:
        grade = "excellent"
    elif G < 85 and G > 70 :
        grade = "very good"
    elif G <=70 and G > 50 :
        grade = "good"
    elif G <= 50:
        grade = "poor"
    return grade
            

rows, cols = 2, int(input("Please enter the number of student: "))
print("")

Matrix = [[0 for x in range(rows)] for i in range(cols)]



for counter in range(cols):
    for c in range(rows):
        if c==0:
            Matrix[counter][c] = input("Enter the student {} name: ".format(counter + 1))
        elif c==1:
            Matrix[counter][c] = input("Enter the student {} grade: ".format(counter + 1))


print("")    

for counter in range(cols):
    for c in range(rows):
        if c==0:
            print("The student {} grade is {}".format(Matrix[counter][c],grade(float(Matrix[counter][1]))) )
print("") 
f = open("student.txt", "w")
for counter in range(cols):
    for c in range(rows):
        if c==0:
            f.writelines("The student {} grade is {} \n".format(Matrix[counter][c],Matrix[counter][1]))
f.close()    
   
if input("Enter '0' to close ")=="0":
    print("bye")
