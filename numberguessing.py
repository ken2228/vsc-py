# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Welcome to the number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Choose a difficulty. Type 'easy' or 'hard' :
# You have X attempts remaining to guess the number.
# Make a guess0
# hard == 5 guesses
# easy == 10 guesses
import random
from os import system
from art_ngg import logo

def choose_difficulty():
    """ Returns the number of turns according to the choosen diificulty """
    answer = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if answer == 'easy':
        return 10
    elif answer == "hard":
        return 5
    else:
        choose_difficulty()

def read_guess():
    """ reads the input from the user and returns a valid value"""
    try:
        guess = int(input("Make a guess: "))
        return guess
    except ValueError:
        return read_guess()

def pick_random_number():
    """ Returns a randum number between 1 and 100 """
    return random.randint(1,100)

def check_number(targetnumber, guess_number):
    """Check if the guessed number is bigger or smaller then the target and return a string """
    if guess_number < targetnumber:
        return "Too low!"
    if guess_number > targetnumber:
        return "Too high!"
    else:
        return f"You got it! the answer was {targetnumber}."

def new_game():

    system("cls")                                                   # clear the screen in VSC
    print(logo)                                                     # prints the logo
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_of_turns = choose_difficulty()                           # adjust the number of turns according to the difficulty choosen
    randomnumber = pick_random_number()                             # put a randomnumber in randomnumber
    numberguessed = False                                           # Boolean to track if the number is guessed, false by default

    while numberguessed == False and number_of_turns > 0:                               # main game loop
        print(f"You have {number_of_turns} attempts remaining to guess the number.")    # print the amount of guesses left
        guessednumber = read_guess()                                                    # put the guessed number in a variable
        result = check_number(randomnumber,guessednumber)                               # check the result
        number_of_turns -= 1                                                            # decrease the number of turns left
        print(result)                                                                   # print the result

        if number_of_turns == 0:                                                        # check if there are turns left
            print(f"The target number was: {randomnumber}. Better luck next time.")     # if no turns left return the randomnumber

        if randomnumber == guessednumber:                                               # if the guessed number matches the randomnumber exit the game loop
            numberguessed = True

    if input("Would you like to go again? 'y' or 'n'. ") == 'y':
        new_game()


new_game()