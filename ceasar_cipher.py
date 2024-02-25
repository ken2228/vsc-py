alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    return_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char.isalpha():
            index = ((alphabet.index(char) + shift_amount) + 26) %  len(alphabet)
            return_text += alphabet[index]
        else:
           return_text += char
    
    print(f"The {cipher_direction}d text is {return_text}")


import art
print(art.logo)
run_program = True

while run_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    keep_goin = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if keep_goin == "no":
        run_program = False
print("Goodbye")
