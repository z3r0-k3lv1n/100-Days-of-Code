import os
from Day_9_Blind_Auction_Art import logo

os.system("cls" if os.name == "nt" else "clear")

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  # bidding_record = {"Stephen": 123, "Angela": 321}
  for bidder in bidding_record: # When looping through a dictionary you are actually looping through the dictionary keys. These are strings.
    bid_amount = bidding_record[bidder] # bidding_record[bidder] selects the name as the key passed into this bidding record. In this example bidder is the key that the loop has looped through. So each name entered will be the key for each bidding record. This is stored as a variable called bid_amount.
    if bid_amount > highest_bid: # If the value of the bid_amount is higher than the value currently stored in the highest_bid variable...
      highest_bid = bid_amount # this value will now be stored as the highest bid.
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
  name = input("What's your name? ")
  price = int(input("What's your bid? $")) # It is necessary to wrap this as an integer in order to be able to loop through the dictionary.
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes / y' or 'no / n': ").lower()
  if should_continue == "no" or should_continue == "n":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes" or should_continue == "y":
    os.system("cls" if os.name == "nt" else "clear") # clears the cli


