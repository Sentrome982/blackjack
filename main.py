import random
from art import logo
import os
import time

clearConsole = lambda: print('\n' * 50)

card_values = {
    "A": 11,
    "K": 10,
    "Q": 10,
    "J": 10,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10
}


def deal_card(player):
    deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A", 2, 3,
            4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J"]
    card = random.choice(deck)
    player.append(card)


def values(cards, player_values):
    for i in cards:
        player_values.append(card_values[i])


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return " \nDraw 🙃"
    elif computer_score == 21:
        return " \nLose, dealer had Blackjack 😱"
    elif user_score == 21:
        return " \nWin with a Blackjack 😎"
    elif user_score > 21:
        return " \nYou went over. You lose 😭"
    elif computer_score > 21:
        return " \nOpponent went over. You win 😁"
    elif user_score > computer_score:
        return " \nYou win 😃"
    else:
        return " \nYou lose 😤"


def play():
    player_cards = []
    dealer_cards = []

    player_values = []
    dealer_values = []

    game_over = False

    time.sleep(0.5)

    print(logo)
    time.sleep(1)
    print("Shuffling. . .")
    time.sleep(2)

    for _ in range(2):
        deal_card(dealer_cards)
        deal_card(player_cards)

    values(player_cards, player_values)
    values(dealer_cards, dealer_values)

    while not game_over:
        player_score = calculate_score(player_values)
        dealer_score = calculate_score(dealer_values)

        print(f"You score: {player_score} \nYour cards: {player_cards}")
        time.sleep(1)
        print(f"Dealer card: {dealer_cards[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
        else:
            hit_or_stay = input("Would you like to (h)it or (s)tay? ")
            if hit_or_stay == "h":
                deal_card(player_cards)
                player_values = []
                values(player_cards, player_values)
            elif hit_or_stay == "s":
                game_over = True
            else:
                print("Invalid entry, type 'h' or 's' ")
                continue
    while dealer_score != 21 and dealer_score < 17:
        deal_card(dealer_cards)
        dealer_values = []
        values(dealer_cards, dealer_values)
        dealer_score = calculate_score(dealer_values)

    print(f" \n\nYour final hand: {player_cards}\nYour final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}\nDealer's final score: {dealer_score}")
    print(compare(player_score, dealer_score))


while input("Do you want to play a game of blackjack?(y/n)") == "y":
    clearConsole()
    play()