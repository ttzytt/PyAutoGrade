


import random

random.seed

from Poker_squares_functions import *


board = [ [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '] ]

time = 0
cards_list = []

name = input("player, what's your name? ")

while True:
    card = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    cards_list.append(card)
    draw_board(board)
    give_cards(card)
    move = input(name + ', choose your move: ')
    success = make_move(move, card, board)
    time += 1

    while not success:
        print('That is not a valid move.')
        next_move = input(name + 'choose your move: ')
        success = make_move(next_move, card, board)

    if time == 25:
        print('your square are full!')
        draw_board(board)
        print("Your total score is " + str(score(board)) + '. Congratulation!')
        print("Game is over.")
        break
 
