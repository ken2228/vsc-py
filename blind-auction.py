#from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
bidding_dictionary ={}
other_bidders = "yes"


def ask_name_bid():

  name = input("What is your name?: ")
  bid = int(input("What is your bid? € "))
  add_dictonary(name, bid)

def add_dictonary(persons_name, persons_bid):
  bidding_dictionary[persons_name] = persons_bid


print(logo)
print("\n\nWelcome to the secret auction program.\n")

while other_bidders == "yes":
  ask_name_bid()
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  
winner = ""
winning_bid = 0
for key in bidding_dictionary:

  #print(f"{key}: {bidding_dictionary[key]}")
  
  if bidding_dictionary[key] > winning_bid:
    #print(f"new winning bid, old bid = {winning_bid}, new bid = {bidding_dictionary[key]}.\n")
    winner = key
    winning_bid = bidding_dictionary[key]

print(f"The winner is {winner} with a bid of €{bidding_dictionary[winner]}!\n")


quit()