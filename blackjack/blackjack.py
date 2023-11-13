import random
from replit import clear
import art

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif player_score == 0:
        return "You win. You have a Blackjack"
    elif player_score > 21:
        return "You Lose."
    elif computer_score > 21:
        return "You Win."
    elif player_score > computer_score:
        return "Opponent went over. You win"
    else:
        return "You lose"

def play_blackjack():
    logo = art.logo
    print(logo)
    #computer and user gets 2 cards each
    player_cards = []
    computer_cards = []

    for num in range(0, 2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards):
        """Take a list of cards and return calculate card"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0    
        elif sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score is: {player_score} ")
        print(f"computer's first card: {computer_cards[0]} ")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else: 
            add_card = input("Do you want to get another card? Type 'yes' or 'no': ")
            if add_card == "yes".lower():
                player_cards.append(deal_card())
                print("player cards: ", player_cards)
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final cards: {player_cards}, and final socre is: {player_score}")
    print(f"Computer final cards: {computer_cards}, and final socre is: {computer_score}")
    print(compare(player_score, computer_score) )  

play_again = input("Do you want to play a Blackjack? Type 'yes' or 'no': ")
if play_again == 'yes'.lower():
    clear()
    play_blackjack()


