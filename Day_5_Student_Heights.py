# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# 156 178 165 171 187
print(student_heights)
print(len(student_heights))
print(sum(student_heights))
print("\n")

total_height = 0
for height in student_heights:
  total_height += height
print(total_height)

num_of_students = 0
for student in student_heights:
  num_of_students += 1

average = total_height / num_of_students
print(round(average))