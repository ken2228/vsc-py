############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from os import system
from art_blackjack import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealerhand = []
playerhand = []

def draw_card():
    return random.choice(cards)

def sumOfList(list):
    return sum(list)

def addCardToHand(timesAddCard, handToAdd):
    for x in range(timesAddCard):
        handToAdd.append(draw_card())

def calculate_scores(listhand):
    handsum = sumOfList(listhand)
    #check for blackjack and return 0 if the hand has blackjack
    if len(listhand) == 2 and handsum == 21:
        return 0
    #check if we are over 21 so the ace will become 1 instead off 11
    if handsum > 21:
        if 11 in listhand:
            listhand[listhand.index(11)] = 1
    return sumOfList(listhand)

def newgame():
    system("cls")
    print(logo)
    #playgame = input("Would you like to play a game of blackjack? ")
    dealerhand = []
    playerhand = []
    blackjack = False
    playersum = 0
    dealersum = 0
    keepplaying = 'y'
    addCardToHand(2, dealerhand)
    addCardToHand(1, playerhand)

    print(f"The dealer has the following cards: [{dealerhand[0]}] and the second card is hidden")

    #print(' '.join(map(str, playerhand)))
    while keepplaying == 'y':
        addCardToHand(1, playerhand)
        playersum = calculate_scores(playerhand)
        print(f"You have the following Cards: {playerhand}, current score = {playersum} ")

        if playersum > 21:
            print("Game over you lose!!")
            keepplaying = 'n'
        elif playersum == 0:
            print("BLACKJACK!! you win!")
            blackjack = True
            keepplaying = 'n'
        else:
            keepplaying = input("Would you like another card? Type 'y' for another card or 'n' to pass: ")

    dealersum = calculate_scores(dealerhand)
    #print(f"The dealer has to following cards: {dealerhand}, current score = {dealersum}")
    
    if blackjack == False:
        while dealersum < 17:
            addCardToHand(1,dealerhand)
            dealersum = sumOfList(dealerhand)
    
        print(f"The dealer has to following cards: {dealerhand}, final score = {dealersum}")

        if dealersum > 21:
            print("The Dealer busted you win!!")
        elif playersum > 21:
            print("You busted the dealer wins!")
        elif dealersum < playersum:
            print("You win!!")
        elif dealersum > playersum:
            print("The dealer wins!")
        
    if input("Would you like to play an new game? 'y' or 'n' ") == 'y':
        newgame()
    else:
        quit()

newgame()
##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

