


def input_students(n):
  students = {}
  for student in range(n):
    student_name = input('Enter the name of student: ')
    student_grade = float(input('Enter the student\'s grade: '))
    if (student_grade > 100 or student_grade < 0):
      student_grade = float(input('Please enter a valid grade: '))
    students[student_name] = grades_test(student_name, student_grade)
    print(students)
  print_to_file(students)
  

def grades_test(student, grade):
  if (grade >= (85)):
     evaluation = 'Excellent'
  elif (grade < 85  and grade > 70):
      evaluation = 'Very Good'
  elif (grade <= 70 and grade > 50):
      evaluation = 'Good'
  else: evaluation = 'Poor'

  return evaluation

def print_to_file(students):
  f = open("students.txt", "w+")
  for key, value in students.items():
    l = [key,'   ', value, '\n']
    f.writelines(l)

# Feel free to control the number of students please :)
input_students(2)
  
