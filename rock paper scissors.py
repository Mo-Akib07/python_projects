import random


rock = '''
Rock:-
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
Paper:-
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''
Scissors:-
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

print(f"{rock}\n{paper}\n{scissors}")
game = [rock, paper, scissors]
# you_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
# computer_choose = random.choice(game)

# if computer_choose == game[1]:
#     if you_choose == 2:
#         print(f"Computer Chice:{computer_choose}\nYour Chice:\n{game[you_choose]}\nYou Win")
#     elif you_choose == 1:
#         print(f"Computer Choose:{computer_choose}\nYou Choose:{game[you_choose]}\n It's a Draw")
#     else:
#         print(f"Computer Choice:{computer_choose}\nYour Choice:\n {game[you_choose]}\nYou Lose!")
# elif computer_choose == game[0]:
#     if you_choose == 1:
#         print(f"Computer Choice:{computer_choose}\nYour Chice:\n{game[you_choose]}\nYou Win")
#     elif you_choose == 0:
#         print(f"Computer Choose:{computer_choose}\nYou Choose:{game[you_choose]}\n It's a Draw")
#     else:
#         print(f"Computer Choice:{computer_choose}\nYour Choice:\n{game[you_choose]}\nYou Lose!")
# elif computer_choose == game[2]:
#     if you_choose == 0:
#         print(f"Computer Choice:{computer_choose}\nYour Chice:\n{game[you_choose]}\nYou Win")
#     elif you_choose == 2:
#         print(f"Computer Choose:{computer_choose}\nYou Choose:{game[you_choose]}\n It's a Draw")
#     else:
#         print(f"Computer Choice:{computer_choose}\nYour Choice:\n{game[you_choose]}\nYou Lose!")
# else:
#     print("You Choose Wrong, Please Try Again!")


# computer_choose = random.randint(0,2)
# if ((computer_choose == 0 and you_choose == 1) or (computer_choose == 1 and you_choose == 2) or (computer_choose == 2 and you_choose == 0)):
#     print(f"Computer Choose:{game[computer_choose]}\nYou Choose:{game[you_choose]}\n You Win")
# elif (computer_choose > you_choose):
#         print(f"Computer Choose:{game[computer_choose]}\nYou Choose:{game[you_choose]}\n You Lose")
# elif (computer_choose < you_choose):
#      print(f"Computer Choose:{game[computer_choose]}\nYou Choose:{game[you_choose]}\n You Win")
# elif((computer_choose == you_choose)):
#     print(f"Computer Choose:{game[computer_choose]}\nYou Choose:{game[you_choose]}\n It's a Draw")
# else:
#     print(f"Computer Choose:{game[computer_choose]}\nYou Choose: Any Random Number\nYou Lose ")



you_choose = int(input("What Do You Choose? Type 0 for Rock, 1 for Paper or 2 for scissors"))
if you_choose >= 3 or you_choose < 0:
    print("You typed an invalid number, You Lose!")
else:
    print(game[you_choose])

    print(game[you_choose])
    computer_choose = random.randint(0, 2)
    print(f"Computer Choose:\n{game[computer_choose]}")

    if you_choose == 0 and computer_choose == 2:
        print("You win")
    elif computer_choose == 0 and you_choose == 2:
        print("You Lose")
    elif computer_choose > you_choose:
        print("You Lose")
    elif you_choose > computer_choose:
        print("You Win")
    elif computer_choose == you_choose:
        print("It's a Draw")






