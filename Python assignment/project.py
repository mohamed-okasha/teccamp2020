
names = []

marks = []   



n = int(input("Enter how many Students : "))


for i in range(n):
    names.append(input("Enter name of student: "))  
    



for i in range(n):
    x=int(input("Enter mark : "))
    marks.append(x)

text=""
markRate=None
k=1
for i in range(n): 
        if marks[i] >= 85 and marks[i] <= 100:
            print("student "+str(k)+" mark is : Excellent")
            markRate="  Excellent"
        elif marks[i] < 85 and marks[i] > 70:
            print("student "+str(k)+" mark is : very good")
            markRate="  very good"
        elif marks[i] > 50 and marks[i] <= 70:
            print("student "+str(k)+" mark is : good" )
            markRate="  good"
        elif marks[i] >= 0 and marks[i] <= 50:
            print("student "+str(k)+" mark is :poor")
            markRate="  poor"
        k+=1
        print(names[i]+markRate)
        text=text+names[i]+" "+markRate

Sfile=open('marksFile.txt','w')
Sfile.write(text)
Sfile.close()