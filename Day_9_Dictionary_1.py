programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  123: "You can also use a number instead of a string as the key.",
}

# Retrieving items fromm dictionary
# print(programming_dicitonary["Bug"]) # Prints the value for the key "Bug"
# print(programming_dicitonary[123]) # Prints the value for the key "Bug"
# print(programming_dicitonary) # Prints the value for the entire dictionary

# Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dicitonary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "This is a different definition for a bug"
# print(programming_dicitonary["Bug"])

# Loop through a dictionary
for key in programming_dictionary:
  print(key) # This will just print each of the keys in the dictionary
  print(programming_dictionary[key]) # By putting [key], this will print the value of each key. In effect the definition.
