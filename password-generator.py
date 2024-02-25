#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total_number = nr_letters + nr_numbers + nr_symbols
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passlist = []

# add the letters
for counter in range(1, nr_letters + 1):
    passlist.insert(random.randint(0,total_number - 1), random.choice(letters))

    

# add the symbols
for counter in range(1, nr_symbols + 1):
   passlist.insert(random.randint(0, total_number - 1), random.choice(symbols))

#add numbers
for counter in range(1, nr_numbers + 1):
    passlist.insert(random.randint(0, total_number - 1), random.choice(numbers))

pass_string = "" 
for char in passlist:
    pass_string += char

print(pass_string)