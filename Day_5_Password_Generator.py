#Password Generator Project
import random
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_lowercase = int(input("How many lowercase letters would you like in your password?\n")) 
nr_uppercase = int(input("How many uppercase letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_special = int(input(f"How many special characters would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#=====================================================
passwdLen = nr_lowercase + nr_uppercase + nr_numbers + nr_special
chars = lowercase + uppercase + numbers + special
#=====================================================

#=====================================================
#=====================================================
e_passwd = ""

for char in range(1, nr_lowercase + 1):
  e_passwd += random.choice(lowercase)

for char in range(1, nr_uppercase + 1):
  e_passwd += random.choice(uppercase)

for char in range(1, nr_numbers + 1):
  e_passwd += random.choice(numbers)

for char in range(1, nr_special + 1):
  e_passwd += random.choice(special)
   
print(e_passwd)

#=====================================================
#=====================================================

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, nr_lowercase + 1):
  password_list += random.choice(lowercase)

for char in range(1, nr_uppercase + 1):
  password_list += random.choice(uppercase)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

for char in range(1, nr_special + 1):
  password_list += random.choice(special)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")