alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type Your Message:\n").lower()
shift = int(input("Type the Shift Number:\n"))
shift = shift % 25
# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The decoded text is {cipher_text}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("You Choose Wrong Type.")

def caesar(text, shift, direction):
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            cipher_text += alphabet[new_position]    
        else:
            cipher_text += char 
    print(f"Your {direction}d text is {cipher_text}")   
caesar(text=text, shift=shift, direction=direction)
result = input("Type 'Yes' if you want to go again. Otherwise Type no.")
if result == "yes":
    again = False
    while not again:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type Your Message:\n").lower()
        shift = int(input("Type the Shift Number:\n"))
        shift = shift % 25
        caesar(text=text, shift=shift, direction=direction)
        result = input("Type 'Yes' if you want to go again. Otherwise Type no.")
        if result == "no":
            again = True
            print("Good Bye.")
else:
    print("Goodbye.")









