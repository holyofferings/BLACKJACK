
import  random

def deal_card():
    """RETURNS THE CARD VALUES """
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    cardss = random.choice(cards)
    return cardss

def calculate_score(cards):
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) >= 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("ITS A DRAW")
    elif computer_score == 0:
        print("You Loose ")
    elif user_score == 0 :
        print("You WIN")
    elif user_score > 21:
        print("You LOOSE")
    elif computer_score >21 :
        print("You WIN")
    elif user_score > computer_score:
        print("You WIN")
    else:
        print("You LOOSE")


def play_game():

      user_cards = []
    computer_cards = []
    is_game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" Your Cards : {user_cards}  Current Score : {user_score}")
        print(f"Computer Cards: {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
       else:
            user = input("Type 'y' to draw an another card. Type 'n' for exiting ").lower()
            if user == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True
       while computer_score != 0 and computer_score < 17 :
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    print(f"Your final Hand is {user_cards} is : {user_score} \n"
          f"Computer's final Hand is {computer_cards} is : {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":

  play_game()

