# HANGMAN

# STEP 1

import random as r

word_list = ["aardvark", "baboon", "camel"]

# TO DO - 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TO DO - 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TO DO - 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#===============================
# OPTION 1
# index = r.randint(0, 2)
# word = word_list[index]
#===============================
# OPTION 2
word = r.choice(word_list)
#===============================

guess = input("Guess a letter: ").lower()

for letter in word:
  if letter is guess:
    print("Right")
  else:
    print("Wrong")


