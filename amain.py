from agame_data import data
import random

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

#choose any person from data


def check_answer(guess, choose1, choose2):
    """Take the user guess and follower counts and returns if they got it right"""
    if a > b:
        return guess == "a" #return true if this cndition is fulfill else false
    else:
        return guess == "b"

score = 0
game_should_continue = True
choose2 = random.choice(data)

while game_should_continue:
    choose1 = choose2
    choose2 = random.choice(data)
    
    while choose1 == choose2:
        choose2 = random.choice(data)
    print(f"Compare A: {format_data(choose1)}.")
    print("VS")
    print(f"Compare B: {format_data(choose2)}.")
        # print(f"Compare A: {choose1["name"]}, a {choose1["description"]}, from {choose1["country"]}")
        # print("VS")
        # print(f"Against B: {choose2["name"]}, a {choose2["description"]}, from {choose2["country"]} ")
    guess = input("Who has more followers? Type 'A' or 'B': \n").lower()

    #Get follower of each other
    a = choose1["follower_count"]
    b = choose2["follower_count"]
    is_correct = check_answer(guess, choose1, choose2)

    if is_correct:
        score += 1
        print(f"You're right! Cureent score: {score}\n")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")


