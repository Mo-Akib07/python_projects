import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
for blank in range(len(chosen_word)):
    display.append("_")
print(display)
guess = input("Guess a letter: ").lower()
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "-" in display:
        end_of_game = True
        print("You Won")




""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """