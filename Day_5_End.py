# For Loops using Range Function

for number in range(1, 11, 1): # The first digit is the lowest end of the range. The second digit is the highest number in the range however it will not be utilised. The third digit is how many steps you wish to make in the loop - Default is 1.
  print(number)

# Gauss trick for adding the numbers 1 - 100
total1 = 0
for number in range(1, 101): #For the range to include the number 100 the max param must be 101.
  total1 += number

print(f"The total sum of the numbers of 1 - 100 is: {total1}")

# Calculate the sum of all of the even numbers between 1 - 100
total2 = 0
for number in range(2, 101, 2): #For the range to include the number 100 the max param must be 101.
  total2 += number

print(f"The total sum of the even numbers of 1 - 100 is: {total2}")

# Alternativce method for calculating the sum of all the even numbers between 1 - 100
total3 = 0
for number in range(1, 101): #For the range to include the number 100 the max param must be 101.
  if number % 2 == 0:
    total3 += number

print(f"The total sum of the even numbers of 1 - 100 is: {total2}")
