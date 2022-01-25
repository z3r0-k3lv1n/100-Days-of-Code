import random as r
from Day_12_Numbers_Game_Art import logo
import os

EASY_TURNS = 10
HARD_TURNS = 5
game_over = True

def check_answer(guess, answer, turns):
  '''Checks answer against answer, returns the number of turns remaining'''
  if guess == answer:
    print(f"You got it. The answer was {answer}")
  elif guess > answer:
    print(f"Too high.\nI say no, no no.")
    return turns - 1
  else:
    print(f"Too low.\nI say no, no no.")
    return turns - 1

def difficulty():
  level = input(f"Choose a difficulty level. Type 'easy' or 'hard': ").lower()
  if level == "easy":
    return EASY_TURNS
  elif level == "hard":
    return HARD_TURNS
  else:
    difficulty()

def play_game():
  os.system("cls" if os.name == "nt" else "clear") # clears the cli
  print(logo, "\nWelcome to the Numbers Guessing Game!\nI'm thinking of a number between 1 and 100.")
  answer = r.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")
  turns = difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts to guess the number.\n")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("GAME OVER! You Lose")
      return game_over
    elif guess!= answer:
      print("Try again.")
  play_again()


def play_again():
  if game_over == True:
    if input("Would you like to play again? Type 'y' or 'n': ").lower() == "y":
      play_game()
    else:
      pass

play_game()
play_again()