############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
# #  for i in range(1, 20):
#     if i == 20:                             # 20 will never be reached as in range the first number is inclusive and the 2nd number is exclusive, 
#       print("You got it")                   # the last number in the range will be 19
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)                        # <--- fix
# #dice_num = randint(1, 6)                        # randint will include both given endpoints wich results in index 0 never being outputted
#                                                  # also the dice_imgs list will error out when 6 is chosen
# print(dice_imgs[dice_num - 1])                  

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1995:                 
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18: 
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])