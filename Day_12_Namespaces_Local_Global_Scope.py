# ========================== SCOPE ===================================
# Anything that you give a name to has a namespsace and this applies within certain scopes


# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# LOCAL SCOPE

# def drink_potion():
#   potion_strength = 2 # The scope of this variable is that it is only available within the walls of the function.
#   print(potion_strength)

# drink_potion()
# print(potion_strength)


# GLOBAL SCOPE

player_health = 10

# def drink_potion():
#   potion_strength = 2 # The scope of this variable is that it is only available within the walls of the function.
#   print(player_health) # The scope of the player_health variable is global as it has been declared outside the function and can be used anywhere within the code.

# drink_potion()

def game():
  def drink_potion():
    potion_strength = 2 # The scope of this variable is that it is only available within the walls of the function.
    print(player_health) # The scope of the player_health variable is global as it has been declared outside the function and can be used anywhere within the code.

  drink_potion() # This method call must be inside the function game() in order to be recognised by the code. It is a local scope variable.

###### There is no BLOCK SCOPE in Python ######
###### It is a terrible idea to name two different variables the same thing when one of them has only a local scope inside a function or method ######


# game_level = 3
# # enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#   # enemies = 0
#   new_enemy = enemies[0]

# ===================================================================================
enemies = 1

def increase_enemies():
  global enemies # Brings the enemies variable from outside the function. Only do this in rare occassions. Try to avoid it to avoid confusion or problems.
  enemies += 1 # Allowing you to modify the variable on a local scale
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outsiude function: {enemies}")

# ===================================================================================


# May be a better option to return the value of the variable in the function instead of importing a global variable
def up_the_enemies(): # Creating a function that returns the increase in the value of the enemies list means you can have it sitting anywhere in the code waiting to be called upon to use it.
  print(f"Enemies inside function: {enemies}")
  return enemies + 1

enemies = up_the_enemies()
print(f"Enemies outside the function: {enemies}")


# ========================== GLOBAL CONSTANTS ===================================
# Constants have one value and never change such as the value of pi.
pi = 3.14159
# The naming convention in python is to name constants in uppercase.
PI = 3.14159
URL = "https://www.franklinmedia.com.au"
TWITTERHANDLE = "@franklinmediaau" # with spaces represented by "_" (underscores)