# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# SIMPLE FUNCTIOn

# def greet():
#   print("G'day mate.")
#   print("Howzit goin'?")
#   print("What's your name mate?")

# greet()

# # FUNCTION THAT ALLOWS FOR AN INPUT

# def greet_with_name(name):
#   print(f"G'day {name}.")
#   print("Howzit goin'?")

# greet_with_name("Michael")

# FUNCTION WITH MORE THAN 1 INPUT

def greet_with(name, location):
  print(f"G'day {name}.")
  print(f"What's the weather like in {location}.")

# The following are positional arguments, meaning they will appear in the position designated in the function definition.
greet_with("James", "the giant peach")

# FUNCTIONS USING KEYWORD ARGUMENTS

def greet_with(name, location):
  print(f"G'day {name}.")
  print(f"What's the weather like in {location}.")

# The following are keyword arguments, meaning they will appear in the position designated by the keyword function definition.
greet_with(name="James", location="the giant peach")
# Can now switch these around and it wont matter to the function
greet_with(location="Angela", name="James")
