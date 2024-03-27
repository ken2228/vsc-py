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


class Subject:
    """class to hold the subject information for easier handling in the program.\n
Takes a dictionairy with the following keywords: 'name', 'follower_count', 'description', 'country'"""
    def __init__(self, adictionary: dict):
        self.name = adictionary['name']
        self.followers = adictionary['follower_count']
        self.description = adictionary['description']
        self.country = adictionary['country']


def pick_from_data():
    """Will return a random data item from the list as a dictionary"""
    return random.choice(data)


def print_subject_info(a_or_b: str, subject: Subject):
    """Will print the 'AorB' item and the subjects information except follower_count"""
    print_string = ""
    if str(a_or_b).lower() == 'a':
        print_string = "Compare A: "
    if str(a_or_b).lower() == 'b':
        print_string = "Against B: "
    print(f"{print_string}{subject.name}, a {subject.description}, from {subject.country}.")


def compare_subject_followers(sub_a: Subject, sub_b: Subject):
    """returns wich subject has more followers, returns 0 when subA has more, returns 1 when subB has more
    and returns -1 when both failed"""
    if sub_a.followers > sub_b.followers:
        return 0
    elif sub_a.followers < sub_b.followers:
        return 1
    else:
        return -1


def process_user_input():
    """Asks the user for an input A or B, if the user gives a wrong input 'errors' and asks again"""
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    if user_input.upper() == 'A':
        return 0
    if user_input.upper() == 'B':
        return 1
    else:
        print("Invalid input detected try again!")
        return process_user_input()


def new_game():
    system("cls")
    print(logo)

    keep_playing = True
    score = 0
    subject_a = Subject(pick_from_data())
    while keep_playing:

        subject_b = Subject(pick_from_data())
        
        print(f"You current score is: {score}.")
        print_subject_info('A', subject_a)
        print(vs)
        print_subject_info('B', subject_b)

        if compare_subject_followers(subject_a, subject_b) == process_user_input():
            system("cls")
            print(logo)

            print(f"Correct!")
            score += 1
            subject_a = subject_b
        else:
            print("Too bad!")
            print(f"But your final score is: {score}!")
            keep_playing = False
        print(f"A has {subject_a.followers} followers, while B has {subject_b.followers}.")

    if str(input("Would you like to play another game? 'Y' or 'N'. ")).lower() == 'y':
        new_game()
    

new_game()