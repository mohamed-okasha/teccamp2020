Number_of_student = int(input("PLEASE ENTER HOW MANY STUDENT YOU WANT TO SAVE : "))
Number_of_element = 2

list1 =  [[0 for x in range(Number_of_element)] for x in range(Number_of_student)] 
with open('Student.txt' , 'w') as f:
    for i in range(len(list1)):
        j = 0   
        list1[i][j] = input("INSERT THE NAME OF STUDENT NUMBER "+ str(i+1) + ": ")
        temp = list1[i][j]
        j +=1
        grade = int(input("INSERT THE GRADE OF "+ temp + ": "))
        if grade >= 85:
            result = "excellent"
        elif 75 <= grade < 85:
            result = "very good"
        elif 65 <= grade < 75:
            result = "good"
        else:
            result = "fail"
        list1[i][j] = result
        f.write(temp + ' : ')
        f.write(result + '\n')
        print('\n')

print("\n\t THE STUDENT ARE : \n")
for i in range(len(list1)):  
    for j in range(len(list1[i])):  
        print('\t    '+list1[i][j], end=" ") 
    print()

print("\nSAVED COMPLETE IN THE STUDENT FILE")