#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
"""cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = [int(input("Choose Your 1st card "), int(input("Choose YOur 2nd card ")))]
computer_cards = random.choice(cards)"""
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards"""
    """if 11 in cards and 10 in cards and len(cards) == 2
    or"""
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # indicate the user or computer has got a score of blackjack
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    #Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return"It's a draw 😊"
    elif computer_score == 0:
        return"Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "with a blackjack 😎"
    elif user_score > 21:
        return "You went over. You Lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score :
        return "You Wins 😄"
    else:
        return "You Lose 😩" 
def play_game():
    #Hint 5: Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        # new_card = deal_card()  #otherwise new_card = [deal_card]
        # user_cards.extend(new_card) # user_card += new_card     += a shorthand of writing a extend function              ----> use for add a list
        # print(user_cards)   # now the answer is same.
        user_cards.append(deal_card()) #use for add a single item in a existing list 
        computer_cards.append(deal_card())
      #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:
        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, Current Score {user_score}")
        print(f"Computer's First card {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over =True
        else:
            user_should_deal = input("Type 'y' to another card, type 'n' to pass ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
      #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do You want to play a game of Blackjack? Type 'y' or type 'n': ") == "y":
    play_game()

