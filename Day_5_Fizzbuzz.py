# Say the numbers from 1 - 100,
# Each time a number is divisible evenly by 3 say fizz
# Each time a number is divisible evenly by 5 say buzz
# Each time a number is divisible evenly by 3 and by 5 say fizzbuzz
# 

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("Fizzbuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
