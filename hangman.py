import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# create a veriable called lives to keep track of the number of lives left.
#set 'lives' to equal 6
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
#create blanks
display = []
for _ in range(len(chosen_word)):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #cheack guessed letter
    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      # print(f"Current Position: {position}\nCurrent letter: {letter}\n Guessed Letter: {guess}")
      if letter == guess:
        display[position] = letter
    #TODO-2: - if guess is not a letter in the chosen_word
    #if lives goes down to 0 then the game should stop and it should print "You Lose"
    if guess not in chosen_word:
        print(display)
guess = input("Guess a letter: ").lower()
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    # print(f"Current Position: {position}\nCurrent letter: {letter}\n Guessed Letter: {guess}")
    if letter == guess:
        display[position] = letter
print(display)
# if guess is not a letter in the chosen_word,
#then reduce 'lives' by 1.
#if lives goes down to 0 the the game should stop and it should print "you lose".
if guess not in chosen_word:
  lives -= 1
  if lives == 0:
      end_of_game = True
      print("You Lose.")

#join all the elements in the list and turn it into a string.
print(f"{' '.join(display)}")

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