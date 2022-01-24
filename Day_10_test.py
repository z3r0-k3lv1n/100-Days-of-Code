from Day_10_Text_Calculator_Art import logo

# Calculator Logo
print(logo)

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

num1 = input("What's the first number?: ")
for operator in operations:
  print(operator)
operation_symbol = input("Pick an operation from the line above: ")
num2 = input("What's the second number?: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")



