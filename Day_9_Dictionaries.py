# SECRET AUCTION PROGRAM - Python Dictionaries

# In Python a Dictionary follows the follwoing syntax
# {"Key": "Value"}
{"Bug": "An error in a program that prevents the pr0gram from running as expected."}

# Separate multiple dictionary entries with a comma
{"Bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again.",
"Loop": "The action of doing something over and over again."}

# NESTING
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

# NESTING A LIST IN A DICTIONARY
# A dictionary can only have one key and one value per entry. You can maintain this structure by nesting a list within the dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# You can also nest lists within lists.
["A", "B", ["C", "D"]]

# NESTING A DICTIONARY IN A DICTIONARY
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Gernmany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
  }

# NESTING A DICTIONARY INSIDE A LIST
# In a dictionary an entry is located by its Key. Whereas in a list an entry is located by its index position.
# By putting the dictionary entries inside a list you can create as many dictionaries as you want and make them iterable.
travel_log = [
  { # Separating the entries in the dictionary just makes it easier to read.
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12},
  {
    "country": "Gernmany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5},
]

def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = country_visited
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)
  # print(travel_log)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

