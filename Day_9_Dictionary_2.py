from multiprocessing.sharedctypes import Value


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
#======================================================================
# MY SOLUTION
for score in student_scores:
  student_grades[score] = student_scores[score]
  if student_grades[score] >= 91:
    student_grades[score] = "Outstanding"
  elif student_grades[score] >= 81 and student_grades[score] <= 90:
    student_grades[score] = "Exceeds Expections"
  elif student_grades[score] >= 71 and student_grades[score] <= 80:
    student_grades[score] = "Acceptable"
  elif student_grades[score] <= 70:
    student_grades[score] = "Fail"

#======================================================================
# Doc Angelas Solution
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expections"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"



# 🚨 Don't change the code below 👇
print(student_grades)
print(student_scores)





