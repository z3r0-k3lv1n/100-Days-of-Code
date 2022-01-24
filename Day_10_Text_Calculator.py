from Day_10_Text_Calculator_Art import logo
import os

# Calculator Logo

# Add - Basic addition function
def add(n1, n2):
  return n1 + n2

# Subtract - Basic subtraction function
def subtract(n1, n2):
  return n1 - n2

# Multiply - Basic multiplication function
def multiply(n1, n2):
  return n1 * n2

# Divide - Basic division function
def divide(n1, n2):
  return n1 / n2

# Basic Mathemathical Functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
  }

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: ")) # It is essential to wrap this input as a int in order for it to be treated as an actal number and not a string.
  for operator in operations:
    print(operator)

  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: ")) # It is essential to wrap this input as a int in order for it to be treated as an actal number and not a string.
    calculation_function = operations[operation_symbol] # creates a variable that stores the selected mathematical operator from the for loop above that loops through the 'operations' dictionary variable
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False # Changes should continue to False and stops the while loop
      calculator() # Recursion is when a function calls itself. Be careful of creating a neverending loop. Make sure some criteria has to be met before a function can call itself.
      os.system("cls" if os.name == "nt" else "clear") # clears the cli

calculator()