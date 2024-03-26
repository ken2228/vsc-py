# HL logo
# "Compare A: Neymar, a Footballer, from Brasil.""
# VS logo
# "Against B: Khloé Kardashian, a Reality TV personality and bussineswoman, from the unitedd states."
# "Who has more followers? Type 'A' or 'B': "

# "Sorry, that's wrong. Final score:  

# CLS 
# HL logo  
# "You're right! Current score: 1.
# Compare previous B as A against new B

import random
from art_hl import logo
from art_hl import vs
from hl_gamedata import data 
from os import system

class subject:
    """class to hold the subject information for easier handling in the program.\n
Takes a dictionairy with the following keywords: 'name', 'follower_count', 'description', 'country'"""
    def __init__(self, aDictionary: dict):
        self.name = aDictionary['name']
        self.followers = aDictionary['follower_count']
        self.description = aDictionary['description']
        self.country = aDictionary['country']

def pickFromData():
    """Will return a random data item from the list as a dictionary"""
    return random.choice(data)

def printsubjectinfo(AorB: str, subject: subject):
    """Will print the 'AorB' item and the subjects information except follower_count"""
    if str(AorB).lower() == 'a':
        printstr = "Compare A: "
    if str(AorB).lower() == 'b':
        printstr = "Against B: "
    print(f"{printstr}{subject.name}, a {subject.description}, from {subject.country}.")

def comparesubjectfollowers(subA: subject, subB: subject):
    """returns wich subject has more followers, returns 0 when subA has more, returns 1 when subB has more
    and returns -1 when both failed"""
    if subA.followers > subB.followers:
        return 0
    elif subA.followers < subB.followers:
        return 1
    else:
        return -1

def procesUserInput():
    """Asks the user for an input A or B, if the user gives a wrong input 'errors' and asks again"""
    userinput = input("Who has more followers? Type 'A' or 'B': ")
    if userinput.upper() == 'A':
        return 0
    if userinput.upper() == 'B':
        return 1
    else:
        print("Invalid input detected try again!")
        return procesUserInput()



def new_game():
    system("CLS")
    print(logo)

    keepplaying = True
    score = 0
    subjectA = subject(pickFromData())
    while keepplaying == True:

        subjectB = subject(pickFromData())
        
        print(f"You current score is: {score}.")
        printsubjectinfo('A', subjectA)
        print(vs)
        printsubjectinfo('B', subjectB)

        if comparesubjectfollowers(subjectA,subjectB) == procesUserInput():
            system("CLS")
            print(logo)

            print(f"Correct!")
            score += 1
            subjectA = subjectB
        else:
            print("Too bad!")
            print(f"But your final score is: {score}!")
            keepplaying = False
        print(f"A has {subjectA.followers} followers, while B has {subjectB.followers}.")

    if str(input("Would you like to play another game? 'Y' or 'N'. ")).lower() == 'y':
        new_game()
    

new_game()