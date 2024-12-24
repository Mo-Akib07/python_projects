import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
'L', 'M', 'N', 'O', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', '"', '<', ',', '>', '.', '?', '/']

print("Welcome to the PyPassword Generator!")
sh = input("Which Level of password you want? For simple type 'S', for medium type 'M' or for hard type 'H'\n")

if sh == "s":
    which = input("which password you Want? for (letter) type 'L', for (symbol) type 'S', for (number) type 'N', for (any generated password) type 'any' or for (parsional password) type 'P'\n").lower()
    if which == "l":
        letter = int(input("How many Letters Would You Like In your Password?\n"))
        password1 = ""
        for char in range(1, letter + 1):
            password1 += random.choice(letters)
        print(f"Your Password is:\n{password1}")
    elif which == "n":
        number = int(input("How many numbers Would You Like In your Password?\n"))
        password2 = ""
        for table in range(1, number + 1):
            password2 += random.choice(numbers)
        print(f"Your Password is:\n{password2}")
    elif which == "s":
        symbol = int(input("How many Symbols Would You Like In your Password?\n"))
        password3 = ""
        for sign in range(1, symbol + 1):
            password3 += random.choice(symbols)
        print(f"Your Password is:\n{password3}")
    elif which == "any":
        char = int(input("How many character Would You Like In your Password:\n"))
        password1 = ""
        for char in range(1, char + 1):
            password1 += random.choice(letters)
        password2 = ""
        for char in range(1, char + 1):
            password2 += random.choice(numbers)
        password3 = ""
        for char in range(1, char + 1):
            password3 += random.choice(symbols)
        password = [password1, password2, password3]
        print(random.choice(password))
    elif which == "p":
        numberofpersional = int(input("How many character Would You Like In your Password?\n"))
        persional = input("Enter Your Password:\n")
        if len(persional) == numberofpersional:
            print(persional)
        else:
            print("You Choose character out of limit, Please try again!")
    else:
        print("You Dont choose any Password, Please Try again.")    
elif sh == "m":
    letter = int(input("How many Letters Would You Like In your Password?\n"))
    symbol = int(input("How many Symbols Would You Like In your Password?\n"))
    number = int(input("How many numbers Would You Like In your Password?\n"))
    password = ""
    for char in range(1, letter + 1):
        password += random.choice(letters)
    for char in range(1, symbol + 1):
        password += random.choice(symbols)
    for char in range(1, number + 1):
        password += random.choice(numbers)
    print(f"Your password is:\n{password}")
elif sh == "h":
    letter = int(input("How many Letters Would You Like In your Password?\n"))
    symbol = int(input("How many Symbols Would You Like In your Password?\n"))
    number = int(input("How many numbers Would You Like In your Password?\n"))
    password_list = []
    for char in range(1, letter + 1):
        password_list.append(random.choice(letters))
    for sign in range(1, symbol + 1):
        password_list.append(random.choice(symbols))
    for table in range(1, number + 1):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    print(f"Your Password is:\n{password}")
else:
    print("You Don't Choose Any Password, Please Try Again!")









    
    









