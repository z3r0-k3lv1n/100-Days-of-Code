import random as r
from turtle import clear
from Day_12_Numbers_Game_Art import logo
import os

attempts = 10

def difficulty():
  global attempts
  level = input(f"Choose a difficulty level. Type 'easy' or 'hard': ").lower()
  if level == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
  elif level == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
  else:
    difficulty()
  return attempts

def play_game():
  os.system("cls" if os.name == "nt" else "clear") # clears the cli
  answer = r.randint(1, 100)
  print(logo, "\nWelcome to the Numbers Guessing Game!\nI'm thinking of a number between 1 and 100.")
  print(f"Pssst, the correct answer is {answer}")
  continue_game = True
  attempts = difficulty()
  while continue_game:
    guess = int(input("Make a guess: "))
    if guess == answer:
      continue_game = False
      print(f"You got it. The answer was {answer}")
    elif attempts <= 1:
      continue_game = False
      print("GAME OVER! You Lose")
    elif guess > answer:
      attempts -= 1
      print(f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.\n")
    elif guess < answer:
      attempts -= 1
      print(f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.\n")
  
  if continue_game == False:
    if input("Would you like to play again? Type 'y' or 'n': ").lower() == "y":
      play_game()
    else:
      pass

play_game()

