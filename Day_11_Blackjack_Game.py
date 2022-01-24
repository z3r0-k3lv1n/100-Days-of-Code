import random
import os
from Day_11_Blackjack_Art import logo

def deal_card(): # Defines a function named deal_card()
  '''Returns a random card from the deck.'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Sets the variable cards as a list containing the values of each of the cards.
  card = random.choice(cards) # Creates the variable card based on a random choice of options from the 'cards' list
  return card # Returns the variable card from the function.

def calculate_score(cards): # Defines a function named calculate_score() which includes the input of the variable "cards" defined as a list of the values of each of the cards used in the deck defined in the function deal_card().
  '''Take alist of cards and return the score calculated from the cards.'''

  if sum(cards) == 21 and len(cards) == 2: # Sets a statement determining if the sum of the variable "cards" is equal to 21 and the length of the variable "cards" is equal to 2.
    return 0 # If these two criteria are met then return the value 0
  
  if 11 in cards and sum(cards) > 21: 
    cards.remove(11)
    cards.append(1)
  return sum(cards) # Returns the sum of the variable cards

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "Player and Dealer BUST. YOU BOTH LOSE."

  if user_score == computer_score:
    return "Draw 🙂"
  elif computer_score == 0:
    return "You Lose. Your Dealer has Blackjack."
  elif user_score == 0:
    return "BLACKJACK... You Win. 😎"
  elif user_score > 21:
    return "BUST... You Lose. 🥲"
  elif computer_score > 21:
    return "DEALER BUSTS. You Win 😛"
  elif user_score > computer_score:
    return "WINNER WINNER CHICKEN DINNER."
  else:
    return "You Lose."

  
def play_game():

  print(logo)

  user_cards = [] # Sets the variable user_cards as an empty list. 
  computer_cards = [] # Sets the variable computer_cards as an empty list.
  is_game_over = False  # Sets the variable is_game_over as a boolean that is = to False.

  for _ in range(2): # range(2) means that the loop will only be run through a total of twice
    user_cards.append(deal_card()) # Adds two random chaices from the 'cards' interval to the 'user_cards' variable
    computer_cards.append(deal_card())  # Adds two random chaices from the 'cards' interval to the 'computer_cards' variable

  while not is_game_over:
    user_score = calculate_score(user_cards) # Calculates the total of the two cards chosen for the user
    computer_score = calculate_score(computer_cards) # Calculates the total of the two cards chosen for the computer
    print(f"User cards = {user_cards}. Current score = {user_score}.\nComputers first card = {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"The users score is {calculate_score(user_cards)}")
  print(f"The computer score is {calculate_score(computer_cards)}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system("cls" if os.name == "nt" else "clear") # clears the cli
  play_game()