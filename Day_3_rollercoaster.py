

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You are tall enough to ride this rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("The child ticket price is $5")
  elif age <= 18:
    bill = 7
    print("The youth ticket price is $7")
  elif age > 18:
    bill = 12
    print("Adult tickets are $12")
  
  souvenir = input("Do you want a photo souvenir with your ride? Type y or n: ")
  if souvenir == "y":
    # Add $3 to the price if the person says yes to a photo souvenir
    bill += 3

  print(f"Your final ticket price is ${bill}. Enjoy your ride try not to spew all over my equipment.")

else:
  print("Sorry short arse, you will need to grow taller to ride this rollercoaster.")