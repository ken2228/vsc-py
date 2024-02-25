rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choices = [rock, paper, scissors]
choice_names= ["Rock", "Paper", "Scissors"]
players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if players_choice >=0 and players_choice <=2:
    print(f"\n\nYour choice: --{choice_names[players_choice]}--")
    print(choices[players_choice])

    cpu_choice = random.randint(0, 2)
    print(f"\n\nThe computer chose: --{choice_names[cpu_choice]}--")

    print(choices[cpu_choice])

    if players_choice == cpu_choice:
        print("Nobody Wins it's a draw!")
        quit()

    if players_choice == 0 and cpu_choice == 2:
        print("You Win!!")
    elif players_choice == 1 and cpu_choice == 0:
        print("You Win!!")
    elif players_choice == 2 and cpu_choice == 1:
        print("You Win!!")
    else:
        print("You lose!!")


'''if players_choice == 0:
  if cpu_choice == 1:
    print("The computer wins!")
    quit()
  else:
    print("You Win!!")
    quit()
elif players_choice == 1:
  if cpu_choice == 2:
    print("The computer wins!")
    quit()
  else:
    print("You Win!!")
    quit()
else:
  if cpu_choice == 0:
    print("The computer wins!")
    quit()
  else:
    print("You Win!!")
    quit()'''
    